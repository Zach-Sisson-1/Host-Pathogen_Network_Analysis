#!/usr/bin/env python

import argparse
import numpy as np
import pandas as pd
import tensorflow as tf
import networkx as nx
from tensorflow.keras.models import load_model
from stellargraph.layer import MeanAggregator, LinkEmbedding
import pickle5 as pkl
from stellargraph import StellarGraph
from stellargraph.mapper import GraphSAGELinkGenerator
from stellargraph.data import EdgeSplitter
from stellargraph.mapper import GraphSAGELinkGenerator, FullBatchLinkGenerator
from stellargraph.layer import GraphSAGE, HinSAGE, link_classification, GCN, LinkEmbedding

print('Loaded Imports')

# Supply arguments to be used in the script
def get_args():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument('-g', '--graph', help='Upload a NetworkX Graph you would like predictions done on for link/edge prediction.', required=True)
    arg_parse.add_argument('-m', '--model', help='Supply the trained model for link/edge prediction', required=True)
    arg_parse.add_argument('-o', '--output', help='Supply new graph name.', required=True)
    return arg_parse.parse_args()

# Grab arguments passed
args = get_args()

print('Init Load Model')

# Load in model
model = load_model(args.model, custom_objects={'MeanAggregator':MeanAggregator, 'LinkEmbedding': LinkEmbedding})

def load_graph(file_path):
	# Load in graph
	with open(file_path, 'rb') as fh:
		G = pkl.load(fh)

	# Pull out edges
	edge_df = nx.to_pandas_edgelist(G)

	# Transform networkx nodes to dataframe
	nodelist = list(G.nodes(data=True))
	
	# Set up each array for pandas import
	nodes = list() 
	bio_proces, mol_fun, cell_comp, intra, sub_loc, topo, path = list(), list(), list(), list(), list(), list(), list()
	for n,d in nodelist:
		nodes.append(n)
		bio_proces.append(d['Gene_ontology_(biological_process)'].split(';')[0])
		mol_fun.append(d['Gene_ontology_(molecular_function)'].split(';')[0] if type(d['Gene_ontology_(molecular_function)']) != float else 'None')
		cell_comp.append(d['Gene_ontology_(cellular_component)'].split(';')[0])
		intra.append(d['Intramembrane'])
		sub_loc.append(d['Subcellular_location_[CC]'])
		topo.append(d['Topological_domain'])
		path.append(d['Pathway'])

	node_df = pd.DataFrame({'proteins': nodes, 
		'Gene_ontology_(biological_process)': bio_proces, 
		'Gene_ontology_(molecular_function)': mol_fun, 
		'Gene_ontology_(cellular_component)': cell_comp, 
		'Intramembrane': intra, 
		'Subcellular_location_[CC]': sub_loc, 
		'Topological_domain': topo, 
		'Pathway': path})


	# Add the hotcode columns back
	hot_df = pd.concat([node_df, 
	pd.get_dummies(node_df['Gene_ontology_(molecular_function)']), 
	pd.get_dummies(node_df['Gene_ontology_(cellular_component)']), 
	pd.get_dummies(node_df['Gene_ontology_(biological_process)']),
	pd.get_dummies(node_df.Intramembrane),
	pd.get_dummies(node_df['Subcellular_location_[CC]']),
	pd.get_dummies(node_df.Topological_domain),
	pd.get_dummies(node_df.Pathway)], 
	axis=1)
	hot_df.drop(['Gene_ontology_(biological_process)', 
	'Gene_ontology_(molecular_function)', 
	'Gene_ontology_(cellular_component)', 
	'Intramembrane', 
	'Subcellular_location_[CC]', 
	'Topological_domain', 
	'Pathway'], inplace=True, axis=1)
	new_hot = hot_df.set_index('proteins')

	print('dummies created')
	# Create matrix dataframe
	matrix_graph = nx.to_pandas_adjacency(G, nodelist=list(new_hot.index))
	print(matrix_graph.shape)
	# Combine dataframes on protein ids
	combo_matrix = new_hot.merge(matrix_graph, left_index=True, right_index=True)

	# Create stellargraph object
	graph = StellarGraph(nodes=combo_matrix,
		       edges=edge_df,
		       node_type_default='proteins',
		       edge_type_default='interactions')


	return graph, graph.nodes(), graph.edges(), G, new_hot, combo_matrix 


# Call the function from above
G, node_list, edge_list, nx_graph, df, mat_df = load_graph(args.graph)


##### Split the data into train and test samples, also randomly create negative and positive edge matrixes 

# Define an edge splitter on the original graph G:
edge_splitter_test = EdgeSplitter(G)

# Randomly sample a fraction p=0.1 of all positive links, and same number of negative links, from G, and obtain the
# reduced graph G_test with the sampled links removed:
G_test, edge_ids_test, edge_labels_test = edge_splitter_test.train_test_split(p=0.9999, method="global", keep_connected=False)

# Set the number of samples per batch size, epochs, and batch size
num_samples = [10]
batch_size = 100 

test_gen = GraphSAGELinkGenerator(G_test, batch_size, num_samples)
test_flow = test_gen.flow(edge_ids_test, edge_labels_test, shuffle=False)


pred_model = model.predict(test_flow)
new = np.where(pred_model < 0.5, 0, pred_model)
new_new = np.where(new >=0.5, 1, new)
sum_correct = 0
for i1, i2 in zip(new_new, edge_labels_test):
	if i1 == i2:
		sum_correct += 1
print(new_new)
print(sum_correct)
print(sum_correct/pred_model.size)


# Create new predictions
data = pd.DataFrame({'predictions': new_new.tolist()}, index=edge_ids_test)
print(data)

data.to_pickle('{}.pkl'.format(args.output))

print('Done.')

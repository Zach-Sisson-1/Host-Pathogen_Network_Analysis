#!/usr/bin/env python

import stellargraph as sg
import pandas as pd
import networkx as nx
import pickle5 as pickle
import argparse
import numpy as np

from stellargraph.data import EdgeSplitter
from stellargraph.mapper import GraphSAGELinkGenerator, FullBatchLinkGenerator
from stellargraph.layer import GraphSAGE, HinSAGE, link_classification, GCN, LinkEmbedding

import tensorflow as tf
from tensorflow import keras
from sklearn import preprocessing, feature_extraction, model_selection

from stellargraph import globalvar
from stellargraph import datasets
from IPython.display import display, HTML
from stellargraph import StellarGraph

# Argparse network pickle
def get_args():
	args = argparse.ArgumentParser()
	args.add_argument('-f', '--file', help='Pass in Networkx pickle file', required=True)
	args.add_argument('-o', '--output', help='What do you want the model to be called? Do not need to add .h5. This model will be saved within the model folder.', required=True)
	return args.parse_args()

# Grab args
args = get_args()

############### Load in data 
# Create an import to pandas dataframe function
def load_graph(gdrive_location):

	with open(gdrive_location, "rb") as fh:
		data = pickle.load(fh)

	# Create an edge df
	edge_df = nx.to_pandas_edgelist(data)

	# Transform networkx nodes to dataframe
	nodelist = list(data.nodes(data=True))
	
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
	matrix_graph = nx.to_pandas_adjacency(data, nodelist=list(new_hot.index))

	# Combine dataframes on protein ids
	combo_matrix = new_hot.merge(matrix_graph, left_index=True, right_index=True)

	# Create stellargraph object
	graph = StellarGraph(nodes=combo_matrix,
		       edges=edge_df,
		       node_type_default='proteins',
		       edge_type_default='interactions')


	return graph, graph.nodes(), graph.edges(), data, new_hot, matrix_graph


# Call the function from above
G, node_list, edge_list, nx_graph, df, mat_df = load_graph(args.file)

print(G.info())

##### Split the data into train and test samples, also randomly create negative and positive edge matrixes 

# Define an edge splitter on the original graph G:
edge_splitter_test = EdgeSplitter(G)

# Randomly sample a fraction p=0.1 of all positive links, and same number of negative links, from G, and obtain the
# reduced graph G_test with the sampled links removed:
G_test, edge_ids_test, edge_labels_test = edge_splitter_test.train_test_split(p=0.1, method="global", keep_connected=True)


# Define an edge splitter on the reduced graph G_test:
edge_splitter_train = EdgeSplitter(G_test)

# Randomly sample a fraction p=0.1 of all positive links, and same number of negative links, from G_test, and obtain the
# reduced graph G_train with the sampled links removed:
G_train, edge_ids_train, edge_labels_train = edge_splitter_train.train_test_split(p=0.1, method="global", keep_connected=True)



# Set the number of samples per batch size, epochs, and batch size
num_samples = [10]
batch_size = 100 
epochs = 120


# Create Link Generator object
train_gen = GraphSAGELinkGenerator(G_train, batch_size, num_samples, seed=1)
train_flow = train_gen.flow(edge_ids_train, edge_labels_train, shuffle=True)

test_gen = GraphSAGELinkGenerator(G_test, batch_size, num_samples, seed=1)
test_flow = test_gen.flow(edge_ids_test, edge_labels_test)


# Set up layers and GraphSAGE object
layer_sizes = [10]
graphsage = GraphSAGE(layer_sizes=layer_sizes, generator=train_gen, bias=True, dropout=0.3, normalize='none')
# Normalize = 'l2' not used right now

# Build the model and expose input and output sockets of graphsage model
# for link prediction
x_inp, x_out = graphsage.in_out_tensors()

# Build a link prediction classifier 
prediction = link_classification(output_dim=1, output_act="relu", edge_embedding_method="ip")(x_out)

# Build the keras model and then compile the model 
model = keras.Model(inputs=x_inp, outputs=prediction)

model.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-3), loss=keras.losses.binary_crossentropy, metrics=["acc"])

# Inital training section
init_train_metrics = model.evaluate(train_flow)
init_test_metrics = model.evaluate(test_flow)


print("\nTrain Set Metrics of the initial (untrained) model:")
for name, val in zip(model.metrics_names, init_train_metrics):
   print("\t{}: {:0.4f}".format(name, val))

print("\nTest Set Metrics of the initial (untrained) model:")
for name, val in zip(model.metrics_names, init_test_metrics):
   print("\t{}: {:0.4f}".format(name, val))

# Specify callback options for while training model
callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath='./models/{}.h5'.format(args.output),
						monitor='val_loss')

# Fit the model
history = model.fit(train_flow, epochs=epochs, validation_data=test_flow, verbose=2, callbacks = [callback, checkpoint])


# Re-evaluate
train_metrics = model.evaluate(train_flow)
test_metrics = model.evaluate(test_flow)

print("\nTrain Set Metrics of the trained model:")
for name, val in zip(model.metrics_names, train_metrics):
    print("\t{}: {:0.4f}".format(name, val))

print("\nTest Set Metrics of the trained model:")
for name, val in zip(model.metrics_names, test_metrics):
    print("\t{}: {:0.4f}".format(name, val))

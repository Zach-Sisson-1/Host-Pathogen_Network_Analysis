#!/usr/bin/env python

import pandas as pd
import networkx as nx
import pickle5 as pickle
import argparse
import numpy as np
from tqdm import tqdm

import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn import preprocessing, feature_extraction, model_selection


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

	return list(data.nodes()), list(data.edges()), data, new_hot, matrix_graph, combo_matrix


# Call the function from above
node_list, edge_list, nx_graph, df, mat_df, G_df_onehot = load_graph(args.file)

print(nx.info(nx_graph))

##### Split the data into train and test samples, also randomly create negative and positive edge matrixes 

# Create an adjacency matrix for train/test split
adj_G = nx.to_numpy_matrix(nx_graph, nodelist = node_list)

### Create list of negative training samples

# Get unconnected node-pairs
all_unconnected_pairs = list()

# Traverse adjacency matrix
offset = 0
for i in tqdm(range(adj_G.shape[0])):
	for j in range(offset, adj_G.shape[1]):
		if i != j:
			if adj_G[i, j] == 0:
				all_unconnected_pairs.append((node_list[i], node_list[j]))
	offset = offset + 1

# Print out the total amount of unconnected pairs within the network
print(len(all_unconnected_pairs))


# Create dataframe to store negative and postive training datasets
node1_unlinked = [i[0] for i in all_unconnected_pairs]
node2_unlinked = [i[1] for i in all_unconnected_pairs]

dfPosNeg = pd.DataFrame({'node1': node1_unlinked,
	'node2': node2_unlinked})

# set them to negative samples
dfPosNeg['link'] = 0

# Set the node count
init_countnodes = len(nx_graph.nodes)

# edge df
edge_df = nx.convert_matrix.to_pandas_edgelist(nx_graph)
edge_df.columns = ['node1', 'node2']

# copy of df
edge_temp = edge_df.copy()

# list to store removable links
removable_links = list()

for i in tqdm(edge_temp.index.values):
	# remove node pair and build a new graph
	G_temp = nx.from_pandas_edgelist(edge_temp.drop(index=i), "node1", "node2", create_using=nx.Graph())

	# check to see that the number of nodes are the same and the graph isn't split
	if (nx.number_connected_components(G_temp) == 22) and (len(G_temp.nodes) == init_countnodes):
		removable_links.append(i)
		edge_temp = edge_temp.drop(index = i)
# create a sub dataframe
df_ghost = edge_df.loc[removable_links]

# add a positive label to the df
df_ghost['link'] = 1

# add these edges to the dataframe so we have a full positive and negative
dfPosNeg = dfPosNeg.append(df_ghost[['node1', 'node2', 'link']], ignore_index=True)

print(dfPosNeg['link'].value_counts())

# Split data into training segmenets
xdata = [[G_df_onehot[i], G_df_onehot[j]] for i, j in zip(dfPosNeg['node1'], dfPosNeg['node2'])]
ydata = list(dfPosNeg['link'])


xtrain, xtest, ytrain, ytest = model_selection.train_test_split(xdata, ydata, test_size = 0.3, random_state=36)

print(len(xtrain), len(xtest), len(ytrain), len(ytest))

#input dimensions
inp_x = len(G_df_onehot.columns)

# Model Building
model = Sequential()


model.add(Dense(inp_x, input_dim=inp_x, activation='relu'))
model.add(Dense(inp_x/2, activation='relu'))
model.add(Dense(750, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

print(model.summary())

# Compile model with binary and adam optimizer
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

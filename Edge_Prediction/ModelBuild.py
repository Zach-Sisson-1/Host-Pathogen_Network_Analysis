#!/usr/bin/env python

###need to input healthy graph with all cleaned attribs

import stellargraph as sg
import pandas as pd
import networkx as nx
import pickle5 as pickle
import argparse
import numpy as np


#imports according to Stellargraph documentation from https://stellargraph.readthedocs.io/en/stable/demos/link-prediction/graphsage-link-prediction.html
from stellargraph.data import EdgeSplitter
from stellargraph.mapper import GraphSAGELinkGenerator
from stellargraph.layer import GraphSAGE, HinSAGE, link_classification

import tensorflow as tf
from tensorflow import keras
from sklearn import preprocessing, feature_extraction, model_selection

from stellargraph import globalvar
from stellargraph import datasets
from IPython.display import display, HTML
from stellargraph import StellarGraph

from stellargraph import globalvar
from stellargraph import datasets
from IPython.display import display, HTML
from stellargraph import StellarGraph

#Setup Argparse for inputting pickle files (graphs)
def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', help = 'Pickle file containing the input graph for NetworkX', required=True)
	parser.add_argument('-o', '--output', help = 'Output name/path', required=True)
	return parser.parse_args()

args = get_args()

#Define all functions that will be used in this script
def graph_loader():
	"""Function inputs a NetworkX pickle file containing a graph and transforms it into a pandas dataframe
	 and outputs the Stellargraph objects. """

	with open(pickle_file), "rb") as file:
		graph = pickle.load(file)

	#Create separate dataframes for edges and nodes
	edge_df = nx.to_pandas_edgelist(graph)
	node_list = list(graph.nodes(data=True))

	#Creating dataframe to house all relevant attribute data for nodes
	nodes = list() 
	biological_process, molecular_function, cellular_component, intramembrane, subcell_location, topological_domain, pathway = list(), list(), list(), list(), list(), list(), list()
	for node,attrib in node_list:
		nodes.append(node)
		biological_process.append(attrib['Gene_ontology_(biological_process)'])
		molecular_function.append(attrib['Gene_ontology_(molecular_function)'])
		cellular_component.append(attrib['Gene_ontology_(cellular_component)'])
		intramembrane.append(attrib['Intramembrane'])
		subcell_location.append(attrib['Subcellular_location_[CC]'])
		topological_domain.append(attrib['Topological_domain'])
		pathway.append(attrib['Pathway'])
	#^ Requires that I push the cleaned attribute full graph (and create diseased graph as well).

	node_df = pd.DataFrame({
		"Proteins":nodes,
		'Gene_ontology_(biological_process)': biological_process, 
		'Gene_ontology_(molecular_function)': molecular_function, 
		'Gene_ontology_(cellular_component)': cellular_component, 
		'Intramembrane': intramembrane, 
		'Subcellular_location_[CC]': subcell_location, 
		'Topological_domain': topological_domain, 
		'Pathway': pathway
		})

	#One-hot-encode labels for each attribute, adding each column to the original dataframe
	hot_encode_df = pd.concat([node_df,
	pd.get_dummies(node_df['Gene_ontology_(biological_process)']),
	pd.get_dummies(node_df['Gene_ontology_(molecular_function)']), 
	pd.get_dummies(node_df['Gene_ontology_(cellular_component)']), 
	pd.get_dummies(node_df['Intramembrane']),
	pd.get_dummies(node_df['Subcellular_location_[CC]']),
	pd.get_dummies(node_df['Topological_domain']),
	pd.get_dummies(node_df['Pathway'])], 
	axis=1)

	#Drop original label columns, retaining only the one-hot-encoding data columns
	hot_encode_df.drop(['Gene_ontology_(biological_process)', 
	'Gene_ontology_(molecular_function)', 
	'Gene_ontology_(cellular_component)', 
	'Intramembrane', 
	'Subcellular_location_[CC]', 
	'Topological_domain', 
	'Pathway'], inplace=True, axis=1)

	#Replace index numbers with protein ID's
	hot_encode_final_df = hot_encode_df.set_index('Proteins')

	#Next convert the one-hot-encoding dataframe to an adjacency matrix which can be used to create a StellarGraph Object
	adj_matrix = nx.to_pandas_adjacency(graph, nodelist = list(graph.nodes()))
	adj_matrix_final = hot_encode_final_df.merge(adj_matrix, left_index=True, right_index=True)

	#Stellargraph object creation
	stellargraph = StellarGraph(nodes=adj_matrix_final, edges=edge_df, node_type_default='Proteins',edge_type_default='interactions')

	#Return stellargraph object
	return(stellargraph)
#################################################################

#Create stellarobject from input graph
G = graph_loader(args.file)

#### Split input graph into test/training data

#Create EdgeSplitter instance used for sampling edges
edge_split_test = EdgeSplitter(G)

#returns reduced graph (positive edges removed)
G_test, edge_ids_test, edge_labels_test = edge_split_test.train_test_split(
	p=0.1, #returns 10% of edges
	method='global', #nodes are selected at random
	keep_connected=True) #when positive edges are removed care is taken that the reduced graph remains connected
#The reduced graph G_test, together with the test ground truth set of links (edge_ids_test, edge_labels_test), will be used for testing the model.

#Repeat the same for the training set, sampling from the testing set
edge_split_train = EdgeSplitter(G_test)
G_train, edge_ids_train, edge_labels_train = edge_split_train.train_test_split(
	p=0.1,
	method='global',
	keep_connected=True)

#G_train, together with the train ground truth set of links (edge_ids_train, edge_label_train), will be used for training the model.

#set hyperparameters for gradient descent
num_samples = [10] # number of samples per batch size
batch_size = 100 # controls the number of training samples to work through before the model’s internal parameters are updated.
epochs = 120 # number of passes of the entire training dataset the algorithm has completed

#Create link generators for mapping pairs of nodes to the input of GraphSAGE
train_gen = GraphSAGELinkGenerator(G_train, batch_size, num_samples)
train_flow = train_gen.flow(edge_ids_train, edge_labels_train, shuffle=True)

test_gen = GraphSAGELinkGenerator(G_test, batch_size, num_samples, seed=1)
test_flow = test_gen.flow(edge_ids_test, edge_labels_test)

#Specify GraphSage layer size and create object
layer_sizes = [10]
graphsage = GraphSAGE(layer_sizes=layer_sizes, generator=train_gen, bias=True, dropout=0.3, normalize='none')

# Build the model and expose input and output sockets of graphsage model
# for link prediction
x_inp, x_out = graphsage.in_out_tensors()

#build link predictor classifier 
prediction = link_classification(output_dim=1, output_act="relu", edge_embedding_method="ip"
)(x_out)

#Build and compile keras model
model = keras.Model(inputs=x_inp, outputs=prediction)

model.compile(optimizer=keras.optimizers.Adam(lr=1e-3),loss=keras.losses.binary_crossentropy,metrics=["acc"],
)

# Inital training section
init_train_metrics = model.evaluate(train_flow)
init_test_metrics = model.evaluate(test_flow)


print("\nTrain Set Metrics of the initial (untrained) model:")
for name, val in zip(model.metrics_names, init_train_metrics):
   print("\t{}: {:0.4f}".format(name, val))

print("\nTest Set Metrics of the initial (untrained) model:")
for name, val in zip(model.metrics_names, init_test_metrics):
   print("\t{}: {:0.4f}".format(name, val))



# Specify callback options for while training model to save files outputs
callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath='../models/{}.h5'.format(args.output), monitor='val_loss')


# Fit model 
history = model.fit(train_flow, epochs=epochs, validation_data=test_flow, verbose=2, callbacks = [callback, checkpoint])


#Re-evaluate model
train_metrics = model.evaluate(train_flow)
test_metrics = model.evaluate(test_flow)


print("\nTrain Set Metrics of the trained model:")
for name, val in zip(model.metrics_names, train_metrics):
    print("\t{}: {:0.4f}".format(name, val))

print("\nTest Set Metrics of the trained model:")
for name, val in zip(model.metrics_names, test_metrics):
    print("\t{}: {:0.4f}".format(name, val))
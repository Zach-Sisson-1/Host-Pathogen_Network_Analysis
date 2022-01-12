#!/usr/bin/env python

import argparse
import pandas as pd
import networkx as nx
import numpy as np
import pickle5 as pkl
from tqdm import tqdm

import matplotlib.pyplot as plt

# Define arguments
def parse():
	arg = argparse.ArgumentParser()
	arg.add_argument('-p', '--pickle', help='Upload the dataframe that is a pickle.', required=True)
	arg.add_argument('-g', '--graph', help='Load complete Healhty or Disease networkx pickle.', required=True)
	arg.add_argument('-o', '--output', help='Name of newly created graph with predicted edges added in.', required=True)
	return arg.parse_args()

# grab args
args = parse()


# load pickle 
df = pd.read_pickle(args.pickle)

print('Size of edges before removing edges:', len(df), sep='\t')

# drop non connections
nonZeroDf = df[df.predictions == np.array(1.0)]

print('Size of edges once grabbing only postive edges:', len(nonZeroDf), sep='\t')

# now pull out the edges
edge_nonZeroDf = list(nonZeroDf.index)

# Load in the graph from the args.pickle
with open(args.graph, 'rb') as fh:
	healthy_G = pkl.load(fh) 

print(healthy_G)

# pull out the edges from the healthy Graph
G_edges = nx.to_pandas_edgelist(healthy_G)

print(G_edges)

# compare edge_nonZeroDf to G_edges
print('###############################')
print('Calculating New Predicted Edges')
print('###############################')
not_in_G_edges = list()
for edge in tqdm(edge_nonZeroDf):
	tuple_list = [(p1,p2) for p1,p2 in zip(G_edges.source, G_edges.target)]
	if edge not in tuple_list:
		e1, e2 =  edge
		not_in_G_edges.append((e1, e2, {'color': 'red'}))

print('Edges Calculated') 

numHealthy = len(healthy_G.edges())
healthy_G.add_edges_from(not_in_G_edges)


print('Old graph has {} edges and the new graph now has {} edges'.format(numHealthy, len(healthy_G.edges())))


# update edge colors (red is predicted, black is original)
for edge in healthy_G.edges(data=True):
	if edge[2] == dict():
		edge[2]['color'] = 'black'


nx.write_gpickle(healthy_G, path='{}.pkl'.format(args.output))

#plt.figure(figsize=(12,12))
#
#pos = nx.spring_layout(healthy_G, iterations=20, seed=20)
#
#colors = [c for u,v,c in healthy_G.edges(data='color')]
#
#nx.draw_networkx_nodes(healthy_G, pos, node_size=50) 
#
#nx.draw_networkx_edges(healthy_G, pos, edge_color=colors)
#
#plt.show()

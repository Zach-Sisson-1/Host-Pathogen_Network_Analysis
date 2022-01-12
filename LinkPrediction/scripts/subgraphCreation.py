#!/usr/bin/env python

import argparse
import pandas as pd
import networkx as nx
import pickle5 as pkl
import matplotlib.pyplot as plt


# Get args
def get_args():
	arg = argparse.ArgumentParser()
	arg.add_argument('-g', '--graph', help='Mtb Specific disease network. (pickle file)', required=True)
	arg.add_argument('-o', '--output', help='Name of outputed subgraph file (.png file)', required=True)
	return arg.parse_args()

args = get_args()


# Load in data
G = nx.read_gpickle(args.graph)

# Pull out just mtb nodes
mtb_list = [(n,G.nodes()[n]) for n,d in G.nodes(data=True) if d['Subcellular_location_[CC]'] == 'Mtb']

# List to hold neighbors
neighbors = list()
child_neighbors = list()

#List to hold edges
full_edge_list = list()

# Now lets pull out their edges/child nodes
for mtb_node in mtb_list:
    for neighbor_node in G.edges(mtb_node[0]):
        neighbors.append(neighbor_node[1])
        full_edge_list.append(neighbor_node)

# Lets pull out the child nodes to these child nodes
for child_node in neighbors:
    for child_edges in G.edges(child_node):
        child_neighbors.append(child_edges[1])
        full_edge_list.append(child_edges)
        
        
# Combine the two neighbor lists now
neighbors.extend(child_neighbors)

# Create inter connection within subgraph
for edge in G.edges():
	if edge[0] in neighbors and edge[1] in neighbors and edge not in full_edge_list:
		full_edge_list.append(edge)


H = G.edge_subgraph(full_edge_list).copy()
color_dict = {
    "Apical cell membrane":'grey',
    "Basolateral cell membrane":'darkgray',
    "Cell junction":'lightgrey',
    "Cell membrane":'gainsboro',
    "Cell projection":'rosybrown',
    "Cell surface":'lightcoral',
    "Chromosome":'brown',
    "Cytoplasm":'maroon',
    "Cytoplasmic granule":'red',
    "Cytoplasmic granule membrane":'mistyrose',
    "Cytoplasmic vesicle":'tomato',
    "Cytoplasmic vesicle membrane":'darksalmon',
    "Early endosome":'sienna',
    "Early endosome membrane":'chocolate',
    "Endomembrane system":'saddlebrown',
    "Endoplasmic reticulum":'sandybrown',
    "Endoplasmic reticulum lumen":'peachpuff',
    "Endoplasmic reticulum membrane":'linen',
    "Endoplasmic reticulum-Golgi intermediate compartment membrane":'bisque',
    "Endosome membrane":'darkorange',
    "Golgi apparatus":'burlywood',
    "Golgi apparatus membrane":'tan',
    "Golgi outpost":'papayawhip',
    "Host cell membrane":'orange',
    "Host cytoplasm":'wheat',
    "Host endoplasmic reticulum membrane":'moccasin',
    "Host membrane":'blanchedalmond',
    "Host nucleus":'darkgoldenrod',
    "Host nucleus inner membrane":'goldenrod',
    "Late endosome membrane":'cornsilk',
    "Lysosome":'gold',
    "Lysosome membrane":'lemonchiffon',
    "Membrane":'darkkhaki',
    "Microsome":'lightyellow',
    "Microsome membrane":'olivedrab',
    "Midbody":'beige',
    "Mitochondrion":'olivedrab',
    "Mitochondrion inner membrane":'yellowgreen',
    "Mitochondrion intermembrane space":'darkolivegreen',
    "Mitochondrion matrix":'darkseagreen',
    "Mitochondrion membrane":'palegreen',
    "Mitochondrion outer membrane":'forestgreen',
    "Myelin membrane":'darkgreen',
    "Nucleus":'deepskyblue',
    "Nucleus envelope":'steelblue',
    "Nucleus inner membrane":'lightblue',
    "Nucleus matrix":'cadetblue',
    "Nucleus membrane":'cyan',
    "Nucleus outer membrane":'darkcyan',
    "Nucleus speckle":'darkturquoise',
    "Perikaryon":'slategrey',
    "Peroxisome":'aquamarine',
    "Peroxisome membrane":'mediumaquamarine',
    "Photoreceptor inner segment":'cornflowerblue',
    "Recycling endosome":'navy',
    "Recycling endosome membrane":'mediumblue',
    "Rough endoplasmic reticulum":'blueviolet',
    "Rough endoplasmic reticulum membrane":'indigo',
    "Sarcoplasmic reticulum lumen":'plum',
    "Secreted":'fuchsia',
    "Unknown":'black',
    "Vacuole membrane":'slateblue',
    "Virion":'crimson',
    "Virion membrane":'palevioletred',
    "Virion tegument":'lightpink',
    "Mtb":'lime'
}


# Create louvain community dictionary numbering system
louv = {'O43586': 1, 'Q15287': 4, 'Q14005': 1, 'P16403': 1, 'Q9NP66': 1, 'Q02930': 2, 'Q99750': 2, 'P49639': 2, 'Q15654': 2, 'Q93062': 2, 'P08631': 2, 'P22681': 3, 'P59046': 4, 'O76024': 2, 'Q8NEC5': 2, 'Q14847': 1, 'Q63HR2': 2, 'Q9H257': 4, 'Q16543': 4, 'Q9BYV2': 4, 'P43405': 3, 'P40763': 5, 'P15498': 3, 'P41220': 6, 'P12956': 6, 'Q8TB24': 6, 'Q96QH2': 4, 'P10412': 4, 'O75400': 1, 'O95466': 1, 'Q9UIA0': 4, 'Q15154': 4, 'O43741': 8, 'Q7L591': 8, 'Q06187': 3, 'Q9Y616': 5, 'Q15233': 5, 'Q7Z5R6': 9, 'Q9C005': 9, 'Q13077': 8, 'Q92529': 8, 'Q9NQ94': 8, 'O43447': 8, 'O60333': 8, 'O60496': 8, 'O75603': 8, 'P04792': 8, 'P10606': 8, 'P46108': 6, 'Q5VZ18': 8, 'Q86UW9': 8, 'Q8NEU8': 8, 'Q8TEW6': 8, 'Q92625': 8, 'Q99704': 8, 'Q99932': 8, 'Q9HB20': 8, 'Q9P104': 8, 'Q9UKG1': 8, 'Q9Y3C5': 8, 'P07949': 8, 'P07333': 3, 'Q9P2A4': 5, 'P50552': 5, 'Q9UI08': 5, 'P07948': 3, 'P20339': 6, 'P14598': 6, 'Q15080': 6, 'Q01130': 6, 'P11161': 0, 'P51610': 0, 'P04440': 2, 'P51828': 6, 'Q16548': 7, 'Q07812': 7, 'P06126': 3, 'Q9NXV2': 3, 'P09086': 6, 'Q96LT7': 1, 'P62820': 1, 'Q03463': 1, 'Q9UL01': 7, 'O60488': 7, 'Apa': '', 'LpqR': '', 'Rv1827': '', 'Rv1075C': '', 'Rv1074c': '', 'Rv3033': '', 'LpqN': '', 'TB8.4': '', 'Rv3668c': '', 'EspR': '', 'ESAT6': '', 'PE25': ''}

for n in H.nodes():
	if n not in louv.keys():
		louv[n] = ''


# Set the figure size
plt.figure(figsize=(25,25))

# Set the plot
ax = plt.subplot(111)

# Generate out position
normal_pos = nx.spring_layout(H, iterations=20, seed=20)


# Draw everything
nx.draw_networkx_nodes(H, normal_pos, nodelist=[n for n,d in H.nodes(data='Subcellular_location_[CC]') if d != 'Mtb'], node_size=40, node_color=[color_dict[d] for n,d in H.nodes(data='Subcellular_location_[CC]') if d != 'Mtb'])

# Pull out only the Mtb nodes
mtb_sub_nodes = [node for node, part in H.nodes(data='Subcellular_location_[CC]') if part == 'Mtb']

# Lets emphasize the Mtb nodes
nx.draw_networkx_nodes(H, normal_pos, nodelist=mtb_sub_nodes, node_size=100, node_color='lime')

lab_dict = dict()
for key in louv:
	lab_dict[key] = louv[key] 	
# add the labels ontop of the MTb nodes
nx.draw_networkx_labels(H, normal_pos, labels=lab_dict, font_size=15)

mtb_dict = dict()
for mtb in mtb_sub_nodes:
	mtb_dict[mtb] = mtb

nx.draw_networkx_labels(H, normal_pos, labels=mtb_dict) 
# draw edges with colors (black normal, red predicted)
nx.draw_networkx_edges(H, normal_pos, edge_color=[c for u,v,c in H.edges(data='color')])
nx.draw_networkx_edges(H, normal_pos, edgelist=[(u,v) for u,v,c in H.edges(data='color') if c == 'red'], width=3, edge_color='red')
# Scatter plot so I can have a legend
for v in set([c for n,c in H.nodes(data='Subcellular_location_[CC]')]):
    plt.scatter([],[], c=color_dict[v], label='{}'.format(v))
    
# Shrink current axis's height by 10% on the bottom
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=3)

plt.savefig('{}.png'.format(args.output))

# Write out Mtb Subgraph
nx.write_gpickle(H,'MtbSubgraph.pkl')

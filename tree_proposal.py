import random
import networkx as nx
from new_seeds import tree_part2, recursive_tree_part
from proposals import propose_random_flip


def propose_tree(partition):
	edge = random.choice(tuple(partition['cut_edges']))
	#print(edge)
	et=[partition.assignment[edge[0]],partition.assignment[edge[1]]]
	#print(et)
	sgn=[]
	for n in partition.graph.nodes():
		if partition.assignment[n] in et:
			sgn.append(n)
			
	#print(len(sgn))
	sgraph = nx.subgraph(partition.graph,sgn)
	
	edd={0:et[0],3:et[1]}
	
	#print(edd)
    
	clusters = recursive_tree_part(sgraph,2,"population",.01,2)
	#print(len(clusters))
	flips={}
	for val in clusters.keys():
		flips[val]=edd[clusters[val]]
	
	#print(len(flips))
	#print(partition.assignment)
	#print(flips)
	return flips
	
	
def mixed_proposal(partition):

	if random.random() <.02:
		flips=propose_tree(partition)
	else: 
		flips = propose_random_flip(partition)
		
	return flips
	
 



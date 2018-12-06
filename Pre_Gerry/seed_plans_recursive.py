# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:01:27 2018

@author: daryl
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:14:38 2018

@author: daryl
"""

from new_seeds_recursive import *
from make_graph import construct_graph
import matplotlib.pyplot as plt
import networkx as nx
import geopandas as gp
graph_path ="./Data/AR_Full/AR_with_data.json"
df = gp.read_file("./Data/AR_Full/AR_Full.shp")
#df=df.set_index("ID")




#plt.ioff()



graph = construct_graph(graph_path, id_col="ID",  pop_col="POP10", district_col="CD",
                        data_source_type="json")


df.plot(column="CD",cmap="tab20")
plt.show()



def recursive_bi_part(graph, parts, pop_col, epsilon,node_repeats=20,):
    newlabels={}
    pop_target=0
    for node in graph.nodes():
        pop_target+=graph.nodes[node][pop_col]
    pop_target=pop_target/parts
    
    remaining_nodes=list(graph.nodes())
    for n in newlabels.keys():
        remaining_nodes.remove(n)
    sgraph=nx.subgraph(graph,remaining_nodes)
    
    for i in range(parts-1):
        #update=tree_part2(sgraph, pop_col, pop_target, epsilon,node_repeats)#should be part2
        #update = minflow_part(sgraph, pop_col, pop_target, epsilon)
        #update = minflow_part1(sgraph, pop_col, pop_target, epsilon)
        #update =  edge_removal_part(sgraph, pop_col, pop_target, epsilon)#inefficient
        #update = part2path2(sgraph, pop_col, pop_target, epsilon)
        #update = part2path3(sgraph, pop_col, pop_target, epsilon)
        #update = part2path(sgraph, pop_col, pop_target, epsilon)
        #update = part2snake(sgraph, pop_col, pop_target, epsilon)
        #update = part2blob(sgraph, pop_col, pop_target, epsilon)
        update = hier_part(sgraph, pop_col, pop_target, epsilon)
        for x in list(update[1]):
            newlabels[x]=i
        #update pop_target?
        remaining_nodes=list(graph.nodes())
        for n in newlabels.keys():
            remaining_nodes.remove(n)
        
        sgraph=nx.subgraph(graph,remaining_nodes)
        #print("Built District #", i)
        
    td=set(newlabels.keys())
    for nh in graph.nodes():
        if nh not in td:
            newlabels[nh]=parts-1#was +1 for initial testing
    return newlabels




for i in range(5):
    j = 2#random.randint(3,4)
    print(j)
    newtree = recursive_bi_part(graph,j,"POP10",.1,2)
    df["newtree"+str(i)]=df["ID"].map(newtree)
    df.plot(column="newtree"+str(i),cmap="tab20")
    plt.show()


#savefig("./Outputs/Tree/AR0.png")
#plt.close()

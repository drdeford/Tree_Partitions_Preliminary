# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 11:26:46 2018

@author: daryl
"""
from new_seeds import *
import json
from rundmcmc.make_graph import construct_graph
import time

start_time=time.time()

#graph_path ="./Data/Arkansas_graph_with_data.json"
#df =gp.read_file("./Data/AR_Full.shp")

graph_path ="./Data/VA_2018/Virginia_Enacted_Trimmed.json"
df =gp.read_file("./Data/VA_2018/Enacted_Trimmed.shp")


pop_col="POP10"
id_col="BLOCKID10"
graph = construct_graph(graph_path, id_col="BLOCKID10",  pop_col="POP10", district_col="VAENACTED",
                        data_source_type="json")


        
#sgraph = nx.subgraph(graph,sgn)


pop_target=0
for node in graph.nodes():
    pop_target+=graph.nodes[node][pop_col]
        
pop_target = pop_target/33



print("loaded data")

#
#ctree = tree_part2(graph,pop_col,pop_target, .02)
###print(ctree)
#cdtree={}
##
#for x in list(ctree[1]):
#    cdtree[x]=2
#for x in list(ctree[-1]):
#    cdtree[x]=1
#
#df["nctree"]=df[id_col].map(cdtree)
#
##df.plot(column="nctree")
#df.fillna(0)
#df.plot(column="VAENACTED",cmap='tab20')
#gf=df.loc[df['nctree'].isin([0,1,2,3,4,5,-1])]
#gf.plot(column="VAENACTED",cmap='tab20')
#df.plot(column="nctree",cmap='tab20')
#gf.plot(column="nctree",cmap='tab20')
#


newtree = recursive_tree_part(graph,33,"POP10",.001,1)

with open("./Outputs/VAassignment_supersmall.json", 'w') as jf1:
			json.dump(newtree, jf1)

df["newtree"]=df["BLOCKID10"].map(newtree)

#df.plot(column="newtree",cmap="tab20")
#df.plot(column="newtree")
#df.plot(column="newtree",cmap="nipy_spectral")


print("--- %s seconds ---" % (time.time() - start_time))


#
#
#
#eflow = edge_removal_part(sgraph,"POP10",(1/2)*pop_target, .1)
##print(ctree)
#edflow={}
#
#for x in list(eflow[1]):
#    edflow[x]=1
#for x in list(eflow[-1]):
#    edflow[x]=2
#
#
#df["ecflow"]=df["ID"].map(edflow)
#df.fillna(0)
#df.plot(column="CD",cmap='tab20')
#gf=df.loc[df['ecflow'].isin([1,2,3,4,5,-1])]
#gf.plot(column="CD",cmap='tab20')
#df.plot(column="ecflow",cmap='tab20')
#gf.plot(column="ecflow",cmap='tab20')
#
#
#
#cflow = minflow_part(sgraph,"POP10",(1/2)*pop_target, .1)
##print(ctree)
#cdflow={}
#
#for x in list(cflow[1]):
#    cdflow[x]=1
#for x in list(cflow[-1]):
#    cdflow[x]=2
#for x in list(cflow[2]):
#    cdflow[x]=3
#for x in list(cflow[3]):
#    cdflow[x]=4
#for x in list(cflow[4]):
#    cdflow[x]=5
#    
#
#df["ncflow"]=df["ID"].map(cdflow)
#df.fillna(0)
#df.plot(column="CD",cmap='tab20')
#gf=df.loc[df['ncflow'].isin([1,2,3,4,5,-1])]
#gf.plot(column="CD",cmap='tab20')
#df.plot(column="ncflow",cmap='tab20')
#gf.plot(column="ncflow",cmap='tab20')
#plt.show()
#new_clusters3 = part2path2(graph,"POP10",pop_target, .1)
#
#cd3={}
#kl =list(new_clusters3.keys())#
#
#for x in list(new_clusters3[kl[0]]):
#    cd3[x]=0
#for x in list(new_clusters3[kl[1]]):
#    cd3[x]=1
#    
#
#df["nc3"]=df["ID"].map(cd3)
#
#df.plot(column="nc3")
#plt.show()
#
#
#new_clusters2 = part2blob(graph,"POP10",pop_target, .1)
#cd2={}
#kl =list(new_clusters2.keys())
#
#for x in list(new_clusters2[kl[0]]):
#    cd2[x]=0
#for x in list(new_clusters2[kl[1]]):
#    cd2[x]=1
#    
#
#df["nc2"]=df["ID"].map(cd2)
#
#df.plot(column="nc2")
#plt.show()
##
##
##
#new_clusters = hier_part(graph,"POP10",pop_target, .1)
#
##
#
#
#kl =list(new_clusters.keys())
#
#cd ={}
#for x in list(new_clusters[kl[0]][0]):
#    cd[x]=0
#for x in list(new_clusters[kl[1]][0]):
#    cd[x]=1
#    
#df["nc"]=df["ID"].map(cd)
#
#df.plot(column="nc")
#
#
#
#        
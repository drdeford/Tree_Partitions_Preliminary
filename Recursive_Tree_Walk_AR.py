# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:14:38 2018

@author: daryl
"""

from new_seeds import *
import json
import random
from rundmcmc.make_graph import construct_graph
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import geopandas as gp
graph_path ="./Data/Arkansas_graph_with_data.json"
df = gp.read_file("./Data/AR_Full.shp")
#df=df.set_index("ID")



plt.ioff()


graph = construct_graph(graph_path, id_col="ID",  pop_col="POP10", district_col="CD",
                        data_source_type="json")


df.plot(column="CD",cmap="tab20")
plt.savefig("./Outputs/Tree/AR0.png")
plt.close()


et=[0,0]

#build a list then use that list to update

assignment=df["CD"].tolist

el=list(graph.edges())
df["newtree0"]=df["CD"]

for its in range(1,100):
    et=[0,0]
    while et[0]==et[1]:
        ed=random.choice(el)
        et=[int(df.loc[df["ID"]==ed[0],"newtree"+str(its-1)]),int(df.loc[df["ID"]==ed[1],"newtree"+str(its-1)])]
        
    
    sgn=[]
    for n in graph.nodes():
        if int(df.loc[df["ID"]==n,"newtree"+str(its-1)]) in et:
            sgn.append(n)
            
            
    sgraph = nx.subgraph(graph,sgn)
    
    edd={0:et[0],3:et[1]}
    
    newtree_partial = recursive_tree_part(sgraph,2,"POP10",.05,2)
    newtree={}
    for n in graph.nodes():
        if n not in sgn:
            newtree[n]=int(df.loc[df["ID"]==n,"newtree"+str(its-1)])
        else:
            newtree[n]=edd[newtree_partial[n]]
    
    
    
    

    df["newtree"+str(its)]=df["ID"].map(newtree)
    #df["newtree"+str(its)]=pd.to_numeric(df["newtree"+str(its)])

    df.plot(column="newtree"+str(its),cmap="tab20")
    plt.savefig("./Outputs/Tree/AR"+str(its)+".png")
    plt.close()

    
    #ffmpeg -framerate 3 -i AR%2d.png AR_Tree.gif
    
    

    

                     



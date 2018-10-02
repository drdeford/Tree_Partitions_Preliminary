# Import for I/O

import os
import random
import json
import geopandas as gp
import functools
import datetime
import matplotlib.pyplot as plt
import numpy as np
import csv

# Imports for RunDMCMC components
# You can look at the list of available functions in each
# corresponding .py file.

from tree_proposal_spaced_AR import *

from rundmcmc.accept import always_accept

from rundmcmc.chain import MarkovChain

from rundmcmc.make_graph import (construct_graph,
                                 get_assignment_dict_from_graph,add_data_to_graph)

from rundmcmc.partition import Partition

from rundmcmc.proposals import propose_random_flip

from rundmcmc.updaters import (Tally, boundary_nodes, cut_edges,
                               cut_edges_by_part, exterior_boundaries,
                               perimeters, polsby_popper,
                               votes_updaters,
                               interior_boundaries,
                               CountySplit,county_splits)

from rundmcmc.validity import (L_minus_1_polsby_popper,
                               L1_reciprocal_polsby_popper,
                               Validator, single_flip_contiguous,
                               within_percent_of_ideal_population,
                               SelfConfiguringLowerBound,
                               LowerBound, UpperBound, refuse_new_splits,
							   non_bool_where, proposed_changes_still_contiguous)

from rundmcmc.scores import (efficiency_gap, mean_median,
                             mean_thirdian, how_many_seats_value,
                             number_cut_edges, worst_pop,
                             L2_pop_dev,
                             worst_pp, best_pp,
                             node_flipped, flipped_to, bvap_vector)

from rundmcmc.output import (p_value_report, hist_of_table_scores,
                             trace_of_table_scores, pipe_to_table)


# Here is where you have to input a few things again

# Set Random Seed
random.seed(1769) #1861

# Type the name of your state
state_name = "Virginia_Treeseed_23merge"

# Input the path to the JSON graph and the GEOJSON for plotting
graph_path = "./Data/VA_2018/Virginia_Enacted_Trimmed.json"
plot_path = "./Data/VA_2018/Enacted_Trimmed.shp"
vote_path = "./Data/VA_block_prorate/Prorated.shp"
tree_plan = "./Data/VA_New_Tree_Plans/VA_Tree_small0123.json"

# Names of graph columns go here
unique_label = "BLOCKID10"
pop_col = "POP10"
#district_col = "VAENACTED"
county_col =  "COUNTYFP10"
area_col = "areas"

# Type the number of elections here
num_elections = 6

vf=gp.read_file(vote_path)
vf.set_index(unique_label)

df= gp.read_file(plot_path)
df.set_index(unique_label)

#df['G_DEM_17_y'] = df[unique_label].map(vf['G_DEM_17_y'])
#df['G_REP_17_y'] = df[unique_label].map(vf['G_REP_17_y'])
#df['LG_DEM_1_1'] = df[unique_label].map(vf['LG_DEM_1_1'])
#df['LG_REP_1_1'] = df[unique_label].map(vf['LG_REP_1_1'])
#df['AG_DEM_1_1'] = df[unique_label].map(vf['AG_DEM_1_1'])
#df['AG_REP_1_1'] = df[unique_label].map(vf['AG_REP_1_1'])
#df['P_DEM_16_y'] = df[unique_label].map(vf['P_DEM_16_y'])
#df['P_REP_16_y'] = df[unique_label].map(vf['P_REP_16_y'])

df['G_DEM_17_y'] = vf['G_DEM_17_y']
df['G_REP_17_y'] = vf['G_REP_17_y']
df['LG_DEM_1_1'] = vf['LG_DEM_1_1']
df['LG_REP_1_1'] = vf['LG_REP_1_1']
df['AG_DEM_1_1'] = vf['AG_DEM_1_1']
df['AG_REP_1_1'] = vf['AG_REP_1_1']
df['P_DEM_16_y'] = vf['P_DEM_16_y']
df['P_REP_16_y'] = vf['P_REP_16_y']

df['G_DEM_17_y'].fillna(0)
df['G_REP_17_y'].fillna(0)
df['LG_DEM_1_1'].fillna(0)
df['LG_REP_1_1'].fillna(0)
df['AG_DEM_1_1'].fillna(0)
df['AG_REP_1_1'].fillna(0)
df['P_DEM_16_y'].fillna(0)
df['P_REP_16_y'].fillna(0)



vf = None

# Type the names of the elections here
election_names =["BVAP_2010","BPOP_2010",'Gov17','Lt_Gov17','AG17','Pres16']
election_columns = [["VABVAP","VAnBVAP"],["VABlack","VAnBPOP"]]

# Choose a proposal from proposals.py
proposal_method = propose_merge2_tree

# Choose an acceptance method from accept.py
acceptance_method = always_accept

# Choose how many steps to run the chain
steps = 10000000

# For outputs type the number of times you would like the values written to the console,
# the frequency to collect stats about the run, and the number of plots to generate
number_to_display = 1000
bin_interval = 1
num_plots = 1000


# That was (almost) everything!
# The code below constructs and runs the Markov chain
# You may want to adjust the binary constraints -
# they are located below in the section labelled ``Validators''


# Make a folder for the output
current = datetime.datetime.now()
newdir = "./Outputs/VA_BVAP/" + state_name + "run" + str(current)[:10] + "-" + str(current)[11:13]\
         + "-" + str(current)[14:16] + "-" + str(current)[17:19] + "/"

os.makedirs(os.path.dirname(newdir + "init.txt"), exist_ok=True)
with open(newdir + "init.txt", "w") as f:
    f.write("Created Folder")


# This builds a graph
graph = construct_graph(graph_path, id_col="id", area_col=area_col,
                        pop_col=pop_col, #district_col=district_col,
                        data_cols=[county_col] + [cols
                                                  for pair in election_columns for cols in pair],
                        data_source_type="json")


tree_col = "tree_col"
district_col = tree_col

with open(tree_plan, 'r') as f:
        tree_dict = json.load(f)


tree_dict = dict(tree_dict)
df[tree_col] = df[unique_label].map(tree_dict)
election_columns = [['G_DEM_17_y','G_REP_17_y'],
 ['LG_DEM_1_1', 'LG_REP_1_1'],['AG_DEM_1_1','AG_REP_1_1'],['P_DEM_16_y','P_REP_16_y']]

add_data_to_graph(df, graph, [cols for pair in election_columns for cols in pair],id_col=unique_label)
add_data_to_graph(df, graph, [tree_col])

#df.plot(column=tree_col,cmap="tab20")
#plt.show()

# Get assignment dictionary
assignment = tree_dict#get_assignment_dict_from_graph(graph, tree_col)

election_columns = [["VABVAP","VAnBVAP"],["VABlack","VAnBPOP"],['G_DEM_17_y','G_REP_17_y'],
 ['LG_DEM_1_1', 'LG_REP_1_1'],['AG_DEM_1_1','AG_REP_1_1'],['P_DEM_16_y','P_REP_16_y']]

# Necessary updaters go here
updaters = {'population': Tally('population'),
  #          'perimeters': perimeters,
            'exterior_boundaries': exterior_boundaries,
            'interior_boundaries': interior_boundaries,
            'boundary_nodes': boundary_nodes,
            'cut_edges': cut_edges,
 #           'areas': Tally('areas'),
  #          'polsby_popper': polsby_popper,
            'cut_edges_by_part': cut_edges_by_part,
   #         'County_Splits': county_splits('County_Splits',county_col)
   }


# Add the vote updaters for multiple plans
for i in range(num_elections):
    updaters = {**updaters, **votes_updaters(election_columns[i], election_names[i])}


# This builds the partition object
initial_partition = Partition(graph, assignment, updaters)

# Choose which binary constraints to enforce
# Options are in validity.py

#non_bool_where(initial_partition)

pop_limit = .02
population_constraint = within_percent_of_ideal_population(initial_partition, pop_limit)

non_bool_where(initial_partition)
#compactness_constraint_Lm1 = LowerBound(L_minus_1_polsby_popper, .85*L_minus_1_polsby_popper(initial_partition))

edge_constraint = UpperBound(number_cut_edges, 2*number_cut_edges(initial_partition))

#county_constraint = refuse_new_splits("County_Splits")

validator = Validator([])#,county_constraint])#edge_constraint])


#validator = Validator([single_flip_contiguous, population_constraint,
#                       edge_constraint])#,county_constraint])#edge_constraint])

# Names of validators for output
# Necessary since bounds don't have __name__'s
list_of_validators = []

# Geojson for plotting
#df_plot = gp.read_file(plot_path)
#df_plot["NCD"]=df["NCD"]
#df_plot["initial"] = df_plot[unique_label].map(assignment)
#df_plot.plot(column="initial", cmap='tab20')
#plt.axis('off')
#plt.savefig(newdir + district_col + "_initial.png")
#plt.close()

print("setup chain")

# This builds the chain object for us to iterate over
chain = MarkovChain(proposal_method, validator, acceptance_method,
                    initial_partition, total_steps=steps)

print("built chain")

bvap_vec=[]
bpop_vec=[]
pop_vec=[]
cut_vec=[]
bvap_triple = []
bpop_triple = []
mmg=[]
mmlg=[]
mmag=[]
mmp=[]
egg=[]
eglg=[]
egag=[]
egp=[]


#print(initial_partition["VABVAP%"])


num_dists=len(initial_partition["VABVAP%"])

#plt.close()





#
# tree_col = "tree_col"
# district_col = tree_col
#
# with open(tree_plan, 'r') as f:
#         tree_dict = json.load(f)
#
#
# tree_dict = dict(tree_dict)
# df[tree_col] = df[unique_label].map(tree_dict)
#
# add_data_to_graph(df, graph, [tree_col])
#
# assignment = tree_dict


initial_cut = len(initial_partition["cut_edges"])
initial_bvap = bvap_vector(initial_partition,"VABVAP%")
initial_bpop = bvap_vector(initial_partition,"VABlack%")
initial_pop = bvap_vector(initial_partition, "population")
initial_assignment = assignment.copy()


#p = plt.plot(range(num_dists), initial_bvap, 'r+')
#plt.show()

plt.plot(range(num_dists), initial_bvap, 'r+')
plt.plot([0,num_dists], [.55, .55], 'g')
plt.plot([0,num_dists], [.37, .37], 'g')
plt.savefig(newdir + state_name + "BVAPInitial.png")
plt.close()









print("finished_intiial_plot")
#p = plt.plot(range(num_dists), initial_bvap, 'ro')

#print(initial_bvap)
t=0
count=0
for part in chain:

	bvap_vec.append(bvap_vector(part,"VABVAP%"))
	bpop_vec.append(bvap_vector(part,"VABlack%"))
	pop_vec.append(bvap_vector(part,"population"))
	cut_vec.append(len(part["cut_edges"]))
	bvap_triple.append([sum([x<.37 for x in bvap_vec[-1]]),sum([.37<x<.55 for x in bvap_vec[-1]]),sum([x>.55 for x in bvap_vec[-1]])])
	bpop_triple.append([sum([x<.37 for x in bpop_vec[-1]]),sum([.37<x<.55 for x in bpop_vec[-1]]),sum([x>.55 for x in bpop_vec[-1]])])
	mmg.append(mean_median(part,'G_DEM_17_y%'))
	mmlg.append(mean_median(part,'LG_DEM_1_1'))
	mmag.append(mean_median(part,'G_DEM_17_y%'))
	mmp.append(mean_median(part,'G_DEM_17_y%'))
	egg.append(efficiency_gap(part, col1='G_DEM_17_y%', col2='G_REP_17_y'))
	eglg.append(efficiency_gap(part, col1='LG_DEM_1_1', col2='LG_REP_1_1'))
	egag.append(efficiency_gap(part, col1='AG_DEM_1_1', col2='AG_REP_1_1'))
	egp.append(efficiency_gap(part, col1='P_DEM_16_y', col2='P_REP_16_y'))
	t+=1
	if t%1000==0:
		print(t)
		with open(newdir+"bvap"+str(t)+".csv",'w') as tf1:
			writer = csv.writer(tf1,lineterminator="\n")
			writer.writerows(bvap_vec)
		with open(newdir+"bpop"+str(t)+".csv",'w') as tf1:
			writer = csv.writer(tf1,lineterminator="\n")
			writer.writerows(bpop_vec)
		with open(newdir+"pop"+str(t)+".csv",'w') as tf1:
			writer = csv.writer(tf1,lineterminator="\n")
			writer.writerows(pop_vec)
		with open(newdir+"bvaptriple"+str(t)+".csv",'w') as tf1:
			writer = csv.writer(tf1,lineterminator="\n")
			writer.writerows(bvap_triple)
		with open(newdir+"bpoptriple"+str(t)+".csv",'w') as tf1:
			writer = csv.writer(tf1,lineterminator="\n")
			writer.writerows(bpop_triple)

		vecs=[cut_vec,mmg,mmlg,mmag,mmp,egg,eglg,egag,egp]

		with open(newdir+"scalars"+str(t)+".csv",'w') as tf1:
			writer = csv.writer(tf1,lineterminator="\n")
			writer.writerows(vecs)

		with open(newdir+"assignment"+str(t)+".json", 'w') as jf1:
			json.dump(part.assignment, jf1)

		bvap_vec=[]
		bpop_vec=[]
		pop_vec=[]
		cut_vec=[]
		bvap_triple = []
		bpop_triple = []
		mmg=[]
		mmlg=[]
		mmag=[]
		mmp=[]
		egg=[]
		eglg=[]
		egag=[]
		egp=[]
		vecs=[]

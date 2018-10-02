import geopandas as gpd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json
#new version for VA

newdir = "./Outputs/VA_BVAP_PLOTS/NEWCOLORS/VA_TREE31_MERGE_Short/"
datadir = "./Outputs/VA_BVAP/Virginia_Treeseed_31mergerun2018-09-25-19-16-42/"
#Virginia_Treeseed_31mergemixrun2018-09-25-19-01-52/"
#Virginia_Treeseed_23mergemixrun2018-09-25-19-02-33/"
#
#Virginia_Treeseed_23mergerun2018-09-25-19-17-07/"
#Virginia_Treeseed_84run2018-09-25-18-51-42/"
#Virginia_Treeseed_72run2018-09-25-18-52-03/"
#Virginia_Treeseed_71run2018-09-25-18-52-35/"
#Virginia_Treeseed_31run2018-09-25-18-49-32/"
#Virginia_Treeseed_1run2018-09-25-18-47-12/"
#Virginia_Treeseed_66run2018-09-25-18-50-17/"
#Virginia_Treeseed_99run2018-09-25-18-51-20/" 
#Virginia_Treeseed_18run2018-09-25-18-48-15/"



max_steps = 20000#20000#5000000
step_size = 1000#1000#100000

ts =[x*step_size for x in range(1,int(max_steps/step_size)+1)]

#ts=[10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

# for t in ts:
	# with open(datadir+"assignment"+str(t)+".json", 'r') as f:
		# assignment = json.load(f)
	# assignment = dict(assignment)
	# df[str(t)] = df["BLOCKID10"].map(assignment)

	# df.plot(column=str(t), cmap = "tab20")
	# plt.axis('off')
	# plt.title(str(t) + " Map")
	# plt.savefig(newdir + str(t) +"map.png")

	# plt.close()
	# print("Figure:", t)

assignment = None
df = None


a = np.zeros([9,max_steps])

for t in ts:
	temp = np.loadtxt(datadir+"scalars"+str(t)+".csv", delimiter=',')
	a[:,t-step_size:t]=temp

plt.plot(a[0,:])
plt.plot([0,max_steps],[a[0,0],a[0,0]],color='r')
plt.title("Cut Edges")
plt.savefig(newdir+"cutedges.png")
plt.close()

plt.plot(a[1,:])
plt.plot([0,max_steps],[a[1,0],a[1,0]],color='r')

plt.title("Mean Median Gov")
plt.savefig(newdir+"mmgov.png")
plt.close()


plt.plot(a[2,:])
plt.plot([0,max_steps],[a[2,0],a[2,0]],color='r')

plt.title("Mean Median Lt Gov")
plt.savefig(newdir+"mmlg.png")
plt.close()

plt.plot(a[3,:])
plt.plot([0,max_steps],[a[3,0],a[3,0]],color='r')

plt.title("Mean Median AG")
plt.savefig(newdir+"mmag.png")
plt.close()

plt.plot(a[4,:])
plt.plot([0,max_steps],[a[4,0],a[4,0]],color='r')

plt.title("Mean Median Pres")
plt.savefig(newdir+"mmp.png")
plt.close()


plt.plot(a[5,:])
plt.plot([0,max_steps],[a[5,0],a[5,0]],color='r')

plt.title("Efficiency Gap Gov")
plt.savefig(newdir+"eggov.png")
plt.close()


plt.plot(a[6,:])
plt.plot([0,max_steps],[a[6,0],a[6,0]],color='r')

plt.title("Efficiency Gap Lt Gov")
plt.savefig(newdir+"eglg.png")
plt.close()

plt.plot(a[7,:])
plt.plot([0,max_steps],[a[7,0],a[7,0]],color='r')

plt.title("Efficiency Gap AG")
plt.savefig(newdir+"egag.png")
plt.close()

plt.plot(a[8,:])
plt.plot([0,max_steps],[a[8,0],a[8,0]],color='r')

plt.title("Efficiency Gap Pres")
plt.savefig(newdir+"egp.png")
plt.close()


plt.hist(a[0,:])
plt.title("Cut Edges")
plt.axvline(x=a[0,0],color='r')
plt.savefig(newdir+"cutedgeshist.png")
plt.close()

plt.hist(a[1,:],bins=1000)
plt.title("Mean Median Gov")
plt.axvline(x=a[1,0],color='r')

plt.savefig(newdir+"mmgovhist.png")
plt.close()


plt.hist(a[2,:],bins=1000)
plt.title("Mean Median Lt Gov")
plt.axvline(x=a[2,0],color='r')

plt.savefig(newdir+"mmlghist.png")
plt.close()

plt.hist(a[3,:],bins=1000)
plt.title("Mean Median AG")
plt.axvline(x=a[3,0],color='r')

plt.savefig(newdir+"mmaghist.png")
plt.close()

plt.hist(a[4,:],bins=1000)
plt.title("Mean Median Pres")
plt.axvline(x=a[4,0],color='r')

plt.savefig(newdir+"mmphist.png")
plt.close()


plt.hist(a[5,:],bins=1000)
plt.title("Efficiency Gap Gov")
plt.axvline(x=a[5,0],color='r')

plt.savefig(newdir+"eggovhist.png")
plt.close()


plt.hist(a[6,:],bins=1000)
plt.title("Efficiency Gap Lt Gov")
plt.axvline(x=a[6,0],color='r')

plt.savefig(newdir+"eglghist.png")
plt.close()

plt.hist(a[7,:],bins=1000)
plt.title("Efficiency Gap AG")
plt.axvline(x=a[7,0],color='r')

plt.savefig(newdir+"egaghist.png")
plt.close()

plt.hist(a[8,:],bins=1000)
plt.title("Efficiency Gap Pres")
plt.axvline(x=a[8,0],color='r')

plt.savefig(newdir+"egphist.png")
plt.close()



a=None

a=np.zeros([max_steps,33])

for t in ts:
	temp=np.loadtxt(datadir+"bvap"+str(t)+".csv", delimiter=',')
	a[t-step_size:t,:]=temp

# plt.boxplot(a,whis=[10,90])
# #plt.plot(range(1,34), a[0,:], 'ro')
# plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
# , 'ro', label='Enacted')
# plt.plot(range(1,34),[0.11285994764397905, 0.11923800918605526, 0.13897052649256864, 0.15476480623933708, 0.16074647274535397, 0.16448098456572177, 0.1924158221641059, 0.20748078731476377, 0.2389974186557889, 0.247833944163894, 0.2492809364548495, 0.24964654261802227, 0.26311193301484564, 0.26698328522521314, 0.3289734116249918, 0.32909409158231023, 0.3425087866629343, 0.3499765322802531, 0.3698742706878133, 0.38867736303932165, 0.40328054298642535, 0.4191690178691388, 0.43597163215468504, 0.4438127358869349, 0.4490251331585034, 0.451499388004896, 0.463070511068598, 0.46434859154929575, 0.4681934272618101, 0.49059480627868907, 0.5000960491771788, 0.5379312500977005, 0.570986567004151]
# , 'bo', label='Princeton')
# plt.plot(range(1,34), [0.10824003731840597, 0.13539411689800077, 0.13711169698855355, 0.1485726789200835, 0.15400372121605244, 0.15964176113233544, 0.16692439297229716, 0.1714120178778348, 0.17672291013890518, 0.2112792472024415, 0.21340934034432488, 0.2258110938774205, 0.22767239760290928, 0.24239331194711772, 0.25123302994864494, 0.2732269699021939, 0.2802270884022709, 0.3047803894000061, 0.3342634208283905, 0.33525600505689, 0.4240456445754232, 0.4797818705628151, 0.4936303619414126, 0.5012558819788885, 0.5085824894818511, 0.514421058943455, 0.5180834320390713, 0.5225580889610064, 0.5269443588037711, 0.5294892751109184, 0.5353813664186369, 0.5542911182914335, 0.5726470920201874]
# , 'yo', label='Democratic')
# plt.plot([0,34], [.55, .55], 'g')
# plt.plot([0,34], [.37, .37], 'g')
#
# plt.title("BVAP%")
# plt.legend()
# plt.savefig(newdir+"bvapbox.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bvapbox2.png", dpi=500)
#
# plt.close()
medianprops = dict( color='green')
#linestyle='-', linewidth=1.5,
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[1,99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'purple', label='Enacted')
plt.plot(range(1,34),[0.11285994764397905, 0.11923800918605526, 0.13897052649256864, 0.15476480623933708, 0.16074647274535397, 0.16448098456572177, 0.1924158221641059, 0.20748078731476377, 0.2389974186557889, 0.247833944163894, 0.2492809364548495, 0.24964654261802227, 0.26311193301484564, 0.26698328522521314, 0.3289734116249918, 0.32909409158231023, 0.3425087866629343, 0.3499765322802531, 0.3698742706878133, 0.38867736303932165, 0.40328054298642535, 0.4191690178691388, 0.43597163215468504, 0.4438127358869349, 0.4490251331585034, 0.451499388004896, 0.463070511068598, 0.46434859154929575, 0.4681934272618101, 0.49059480627868907, 0.5000960491771788, 0.5379312500977005, 0.570986567004151]
, 'o', color='orange', label='Princeton')
plt.plot(range(1,34), [0.10824003731840597, 0.13539411689800077, 0.13711169698855355, 0.1485726789200835, 0.15400372121605244, 0.15964176113233544, 0.16692439297229716, 0.1714120178778348, 0.17672291013890518, 0.2112792472024415, 0.21340934034432488, 0.2258110938774205, 0.22767239760290928, 0.24239331194711772, 0.25123302994864494, 0.2732269699021939, 0.2802270884022709, 0.3047803894000061, 0.3342634208283905, 0.33525600505689, 0.4240456445754232, 0.4797818705628151, 0.4936303619414126, 0.5012558819788885, 0.5085824894818511, 0.514421058943455, 0.5180834320390713, 0.5225580889610064, 0.5269443588037711, 0.5294892751109184, 0.5353813664186369, 0.5542911182914335, 0.5726470920201874]
, 'o', color = 'pink', label='Democratic')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox99.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox992.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.1,99.9], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'purple', label='Enacted')
plt.plot(range(1,34),[0.11285994764397905, 0.11923800918605526, 0.13897052649256864, 0.15476480623933708, 0.16074647274535397, 0.16448098456572177, 0.1924158221641059, 0.20748078731476377, 0.2389974186557889, 0.247833944163894, 0.2492809364548495, 0.24964654261802227, 0.26311193301484564, 0.26698328522521314, 0.3289734116249918, 0.32909409158231023, 0.3425087866629343, 0.3499765322802531, 0.3698742706878133, 0.38867736303932165, 0.40328054298642535, 0.4191690178691388, 0.43597163215468504, 0.4438127358869349, 0.4490251331585034, 0.451499388004896, 0.463070511068598, 0.46434859154929575, 0.4681934272618101, 0.49059480627868907, 0.5000960491771788, 0.5379312500977005, 0.570986567004151]
, 'o', color='orange', label='Princeton')
plt.plot(range(1,34), [0.10824003731840597, 0.13539411689800077, 0.13711169698855355, 0.1485726789200835, 0.15400372121605244, 0.15964176113233544, 0.16692439297229716, 0.1714120178778348, 0.17672291013890518, 0.2112792472024415, 0.21340934034432488, 0.2258110938774205, 0.22767239760290928, 0.24239331194711772, 0.25123302994864494, 0.2732269699021939, 0.2802270884022709, 0.3047803894000061, 0.3342634208283905, 0.33525600505689, 0.4240456445754232, 0.4797818705628151, 0.4936303619414126, 0.5012558819788885, 0.5085824894818511, 0.514421058943455, 0.5180834320390713, 0.5225580889610064, 0.5269443588037711, 0.5294892751109184, 0.5353813664186369, 0.5542911182914335, 0.5726470920201874]
, 'o', color = 'pink', label='Democratic')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox999.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox9992.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.01,99.99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted')
plt.plot(range(1,34),[0.11285994764397905, 0.11923800918605526, 0.13897052649256864, 0.15476480623933708, 0.16074647274535397, 0.16448098456572177, 0.1924158221641059, 0.20748078731476377, 0.2389974186557889, 0.247833944163894, 0.2492809364548495, 0.24964654261802227, 0.26311193301484564, 0.26698328522521314, 0.3289734116249918, 0.32909409158231023, 0.3425087866629343, 0.3499765322802531, 0.3698742706878133, 0.38867736303932165, 0.40328054298642535, 0.4191690178691388, 0.43597163215468504, 0.4438127358869349, 0.4490251331585034, 0.451499388004896, 0.463070511068598, 0.46434859154929575, 0.4681934272618101, 0.49059480627868907, 0.5000960491771788, 0.5379312500977005, 0.570986567004151]
, 'o', color='orange', label='Princeton')
plt.plot(range(1,34), [0.10824003731840597, 0.13539411689800077, 0.13711169698855355, 0.1485726789200835, 0.15400372121605244, 0.15964176113233544, 0.16692439297229716, 0.1714120178778348, 0.17672291013890518, 0.2112792472024415, 0.21340934034432488, 0.2258110938774205, 0.22767239760290928, 0.24239331194711772, 0.25123302994864494, 0.2732269699021939, 0.2802270884022709, 0.3047803894000061, 0.3342634208283905, 0.33525600505689, 0.4240456445754232, 0.4797818705628151, 0.4936303619414126, 0.5012558819788885, 0.5085824894818511, 0.514421058943455, 0.5180834320390713, 0.5225580889610064, 0.5269443588037711, 0.5294892751109184, 0.5353813664186369, 0.5542911182914335, 0.5726470920201874]
, 'o', color = 'blue', label='Democratic')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox9999.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox99992.png", dpi=500)

plt.close()



fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a, whis=[1,99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'purple', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='orange', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'pink', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'yellow', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox99g.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox992g.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.1,99.9], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'purple', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='orange', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'pink', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'yellow', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox999g.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox9992g.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.01,99.99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'purple', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='orange', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'pink', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'yellow', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox9999g.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox99992g.png", dpi=500)

plt.close()



fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[1,99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='gray', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'gray', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox99gb.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox992gb.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.1,99.9], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='gray', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'gray', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox999gb.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox9992gb.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.01,99.99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='gray', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'gray', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox9999gb.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox99992gb.png", dpi=500)

plt.close()
a=None
# a=np.zeros([max_steps,33])
#
# for t in ts:
# 	temp=np.loadtxt(datadir+"bpop"+str(t)+".csv", delimiter=',')
# 	a[t-step_size:t,:]=temp
#
# plt.boxplot(a,whis=[10,90])
# plt.plot(range(1,34), a[0,:], 'ro')
# plt.plot([0,32], [.55, .55], 'g')
# plt.plot([0,32], [.37, .37], 'g')
#
# plt.title("BPOP%")
# plt.savefig(newdir+"bpopbox.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bpopbox2.png", dpi=500)
#
# plt.close()
a=None

a=np.zeros([max_steps,33])

for t in ts:
	 temp=np.loadtxt(datadir+"pop"+str(t)+".csv", delimiter=',')
	 a[t-step_size:t,:]=temp

plt.boxplot(a,whis=[.1,99.9])
plt.plot(range(1,34), a[0,:], 'ro')
 #plt.plot([0,32], [.55, .55], 'g')
 #plt.plot([0,32], [.37, .37], 'g')

plt.title("Population")
plt.savefig(newdir+"popbox.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"popbox2.png", dpi=500)

plt.close()




plt.plot(a[:,32])
plt.plot([0,max_steps],[a[0,32],a[0,32]],color='r')

plt.title("Largest Population")
plt.savefig(newdir+"lgpop.png")
plt.close()


plt.hist(a[:,32])
plt.title("Largest Population")
plt.axvline(x=a[0,32],color='r')
plt.savefig(newdir+"lgpophist.png")
plt.close()

plt.plot(a[:,0])
plt.plot([0,max_steps],[a[0,0],a[0,0]],color='r')

plt.title("Smallest Population")
plt.savefig(newdir+"smpop.png")
plt.close()


plt.hist(a[:,0])
plt.title("Smallest Population")
plt.axvline(x=a[0,0],color='r')
plt.savefig(newdir+"smpophist.png")
plt.close()


a=None
a= np.zeros([max_steps,3])

for t in ts:
	temp=np.loadtxt(datadir+"bvaptriple"+str(t)+".csv", delimiter=',')
	a[t-step_size:t,:]=temp


plt.boxplot(a,whis=[10,90])
plt.plot([1,2,3],a[0,:],'ro')

plt.title("BVAP Thirdians")

plt.savefig(newdir+"bvapthirds.png")
fig = plt.gcf()
fig.set_size_inches((8.5, 11), forward=False)
fig.savefig(newdir+"bvapthirds2.png", dpi=500)

plt.close()

a=None

a= np.zeros([max_steps,3])

for t in ts:
	temp=np.loadtxt(datadir+"bpoptriple"+str(t)+".csv", delimiter=',')
	a[t-step_size:t,:]=temp


plt.boxplot(a,whis=[10,90])
plt.plot([1,2,3],a[0,:],'ro')

plt.title("BPOP Thirdians")

plt.savefig(newdir+"bpopthirds.png")
fig = plt.gcf()
fig.set_size_inches((8.5, 11), forward=False)
fig.savefig(newdir+"bpopthirds2.png", dpi=500)

plt.close()




a=None
#
# a=np.zeros([max_steps,33])
#
# for t in ts:
# 	temp=np.loadtxt(datadir+"bvap"+str(t)+".csv", delimiter=',')
# 	a[t-step_size:t,:]=temp
#
# medians = np.median(a, axis=0)
#
# l2s=[]
# l1s=[]
#
# for i in range(max_steps):
# 	l2s.append(np.linalg.norm(a[i,:]-medians))
# 	temp=0
# 	for j in range(33):
# 		temp+=abs(a[i,j]-medians[j])
# 	l1s.append(temp)
#
# plt.plot(l2s)
# plt.plot([0,max_steps],[l2s[0],l2s[0]],color='r')
# plt.title("BVAP% L2 Deviation")
# plt.savefig(newdir+"bvapl2trace.png")
# plt.close()
#
# plt.plot(l1s)
# plt.plot([0,max_steps],[l1s[0],l1s[0]],color='r')
# plt.title("BVAP% L1 Deviation")
# plt.savefig(newdir+"bvapl1trace.png")
# plt.close()
#
# plt.hist(l2s,bins=1000)
# plt.axvline(x=np.linalg.norm(np.array(a[0,:])-medians),color='r')
#
# plt.title("BVAP% L2 Deviation")
# plt.savefig(newdir+"bvapl2.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bvapl22.png", dpi=500)
#
# plt.close()
#
# plt.hist(l1s,bins=1000)
# plt.axvline(x=sum([abs(a[0,x]-medians[x]) for x in range(33)]),color='r')
#
# plt.title("BVAP% L1 Deviation")
# plt.savefig(newdir+"bvapl1.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bvapl12.png", dpi=500)
#
# plt.close()
#
# l2sa=np.array(l2s)
#
# import seaborn as sns
#
# sns.set_style('darkgrid')
# sns.distplot(l2sa)
# plt.axvline(x=sum([abs(a[0,x]-medians[x]) for x in range(33)]),color='r')
#
# plt.show()
#
#
#
# a=None
#
# a=np.zeros([max_steps,33])
#
# for t in ts:
# 	temp=np.loadtxt(datadir+"bpop"+str(t)+".csv", delimiter=',')
# 	a[t-step_size:t,:]=temp
#
# medians = np.median(a, axis=0)
#
# l2s=[]
# l1s=[]
#
# for i in range(max_steps):
# 	l2s.append(np.linalg.norm(a[i,:]-medians))
# 	temp=0
# 	for j in range(33):
# 		temp+=abs(a[i,j]-medians[j])
# 	l1s.append(temp)
#
# plt.plot(l2s)
# plt.plot([0,max_steps],[l2s[0],l2s[0]],color='r')
# plt.title("BPOP% L2 Deviation")
# plt.savefig(newdir+"bpopl2trace.png")
# plt.close()
#
# plt.plot(l1s)
# plt.plot([0,max_steps],[l1s[0],l1s[0]],color='r')
# plt.title("BPOP% L1 Deviation")
# plt.savefig(newdir+"bpopl1trace.png")
# plt.close()
# plt.hist(l2s,bins=1000)
# plt.axvline(x=np.linalg.norm(np.array(a[0,:])-medians),color='r')
#
# plt.title("BPOP% L2 Deviation")
# plt.savefig(newdir+"bpopl2.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bpopl22.png", dpi=500)
#
# plt.close()
#
# plt.hist(l1s,bins=1000)
# plt.axvline(x=sum([abs(a[0,x]-medians[x]) for x in range(33)]),color='r')
#
# plt.title("BPOP% L1 Deviation")
# plt.savefig(newdir+"bpopl1.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bpopl12.png", dpi=500)
#
# plt.close()

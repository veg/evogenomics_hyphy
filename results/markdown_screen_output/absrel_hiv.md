
Analysis Description
--------------------
aBSREL (Adaptive branch-site random effects likelihood) uses an adaptive
random effects branch-site model framework to test whether each branch
has evolved under positive selection, using a procedure which infers an
optimal number of rate categories per branch.

- __Requirements__: in-frame codon alignment and a phylogenetic tree

- __Citation__: Less Is More: An Adaptive Branch-Site Random Effects Model for Efficient
Detection of Episodic Diversifying Selection (2015). Mol Biol Evol 32
(5): 1342-1353

- __Written by__: Sergei L Kosakovsky Pond, Ben Murrell, Steven Weaver and Temple iGEM /
UCSD viral evolution group

- __Contact Information__: spond@temple.edu

- __Analysis Version__: 1.0



>A tree was found in the data file: `(0564_7,(((((0564_11,0564_4)Node20,(0564_1,(0564_21,0564_5)Node25)Node23)Node19,0564_17)Node18,((0564_13,(0564_15)Node32)Node30,((0564_22,0564_6)Node36,0564_3)Node35)Node29)Node17,0564_9)Node16,(((0557_24,0557_4,0557_2)Node9,0557_12)Node8,((0557_21,0557_6,0557_9,0557_11,0557_13,0557_26,(0557_5,0557_7)Node53)Node6,0557_25)Node7)Separator)`

>Would you like to use it (y/n)? Y


Selected the following branches for testing
	0564_7
	0564_11
	0564_17
	Node18
	0564_13
	0564_15
	Node32
	Node30
	0564_22
	0564_6
	Node36
	0564_3
	0564_4
	Node35
	Node29
	Node17
	0564_9
	Node16
	0557_24
	0557_4
	0557_2
	Node9
	0557_12
	Node20
	Node8
	0557_21
	0557_6
	0557_9
	0557_11
	0557_13
	0557_26
	0557_5
	0557_7
	Node53
	0564_1
	Node6
	0557_25
	Node7
	Separator
	0564_21
	0564_5
	Node25
	Node23
	Node19
[PHASE 0] Fitting the local MG94 (no site-to-site variation) to obtain initial parameter estimates

Log L = -5402.303648294675 with 102 degrees of freedom. IC = 11009.5329761347

Branch omega values

	Count    = 44
	Mean     = 3.933376086091392
	Median   = 0.8132623202663276
	Variance = 20.25168177915332
	Std.Dev  = 4.500186860470721
	COV      = 1.144102867860411
	Sum      = 173.0685477880212
	Sq. sum  = 1551.566003627561
	Skewness = 2.703180275706684
	Kurtosis = 25.38054986365963
	Min      = 0
	2.5%     = 0
	97.5%    = 10
	Max      = 10

[PHASE 1] Fitting Branch Site REL models to one branch at a time

[PHASE 1] Branch 0564_22 log(L) = -5402.314, IC = 11013.589
	2 rate classes
	Node: mixtureTree.0564_22
	Length parameter = 0.01895985424641857
	Class 1
		omega = 0.494
		weight = 0.499
	Class 2
		omega = 1.982
		weight = 0.501

[PHASE 1] Branch 0564_7 log(L) = -5402.304, IC = 11013.570
	2 rate classes
	Node: mixtureTree.0564_7
	Length parameter = 0.03081893655812705
	Class 1
		omega = 0.600
		weight = 0.984
	Class 2
		omega = 0.751
		weight = 0.016

[PHASE 1] Branch Separator log(L) = -5397.465, IC = 11003.892
	2 rate classes
	Node: mixtureTree.Separator
	Length parameter = 0.004261492428285727
	Class 1
		omega = 0.000
		weight = 0.959
	Class 2
		omega = 191.994
		weight = 0.041

[PHASE 1] Branch Separator log(L) = -5397.547818456307, IC = 11008.09515222436
	3 rate classes
	Node: mixtureTree.Separator
	Length parameter = 0.006005913613726777
	Class 1
		omega = 0.000
		weight = 0.954
	Class 2
		omega = 0.000
		weight = 0.000
	Class 3
		omega = 115.736
		weight = 0.046

[PHASE 1] Branch 0564_4 log(L) = -5394.336, IC = 11001.672
	2 rate classes
	Node: mixtureTree.0564_4
	Length parameter = 0.03095913354144237
	Class 1
		omega = 0.011
		weight = 0.980
	Class 2
		omega = 29.462
		weight = 0.020

[PHASE 1] Branch 0564_4 log(L) = -5394.331549355441, IC = 11005.70059926171
	3 rate classes
	Node: mixtureTree.0564_4
	Length parameter = 0.03065518504311318
	Class 1
		omega = 0.000
		weight = 0.976
	Class 2
		omega = 0.000
		weight = 0.003
	Class 3
		omega = 28.835
		weight = 0.022

[PHASE 1] Branch 0564_3 log(L) = -5388.585, IC = 10994.207
	2 rate classes
	Node: mixtureTree.0564_3
	Length parameter = 0.007514779420369777
	Class 1
		omega = 0.000
		weight = 0.970
	Class 2
		omega = 134.222
		weight = 0.030

[PHASE 1] Branch 0564_3 log(L) = -5388.584720874243, IC = 10998.24563935987
	3 rate classes
	Node: mixtureTree.0564_3
	Length parameter = 0.007466257903270094
	Class 1
		omega = 0.000
		weight = 0.961
	Class 2
		omega = 0.000
		weight = 0.008
	Class 3
		omega = 133.645
		weight = 0.031

[PHASE 1] Branch 0564_9 log(L) = -5388.366, IC = 10997.809
	2 rate classes
	Node: mixtureTree.0564_9
	Length parameter = 0.02185808215441468
	Class 1
		omega = 0.000
		weight = 0.918
	Class 2
		omega = 10.485
		weight = 0.082

[PHASE 1] Branch 0564_1 log(L) = -5388.591, IC = 10998.258
	2 rate classes
	Node: mixtureTree.0564_1
	Length parameter = 0.0174858720956459
	Class 1
		omega = 0.795
		weight = 0.710
	Class 2
		omega = 1.725
		weight = 0.290

[PHASE 1] Branch 0564_17 log(L) = -5388.585, IC = 10998.246
	2 rate classes
	Node: mixtureTree.0564_17
	Length parameter = 0.02626384952142774
	Class 1
		omega = 0.600
		weight = 0.405
	Class 2
		omega = 0.502
		weight = 0.595

[PHASE 1] Branch 0564_6 log(L) = -5388.585, IC = 10998.246
	2 rate classes
	Node: mixtureTree.0564_6
	Length parameter = 0.03433942485518252
	Class 1
		omega = 0.397
		weight = 0.500
	Class 2
		omega = 0.249
		weight = 0.500

[PHASE 1] Branch 0564_13 log(L) = -5388.585, IC = 10998.245
	2 rate classes
	Node: mixtureTree.0564_13
	Length parameter = 0.03964118826130018
	Class 1
		omega = 0.196
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch 0564_11 log(L) = -5386.378, IC = 10993.832
	2 rate classes
	Node: mixtureTree.0564_11
	Length parameter = 0.02332658353538009
	Class 1
		omega = 0.000
		weight = 0.986
	Class 2
		omega = 40.620
		weight = 0.014

[PHASE 1] Branch 0564_11 log(L) = -5386.378691286451, IC = 10997.87298925455
	3 rate classes
	Node: mixtureTree.0564_11
	Length parameter = 0.02308266536755266
	Class 1
		omega = 0.000
		weight = 0.982
	Class 2
		omega = 0.000
		weight = 0.004
	Class 3
		omega = 43.389
		weight = 0.014

[PHASE 1] Branch 0564_15 log(L) = -5383.290, IC = 10991.695
	2 rate classes
	Node: mixtureTree.0564_15
	Length parameter = 0.01748039875214196
	Class 1
		omega = 0.000
		weight = 0.992
	Class 2
		omega = 72.163
		weight = 0.008

[PHASE 1] Branch 0564_15 log(L) = -5383.29003726927, IC = 10995.73580248847
	3 rate classes
	Node: mixtureTree.0564_15
	Length parameter = 0.01737346000783575
	Class 1
		omega = 0.000
		weight = 0.991
	Class 2
		omega = 0.000
		weight = 0.001
	Class 3
		omega = 74.868
		weight = 0.008

[PHASE 1] Branch 0557_12 log(L) = -5383.290, IC = 10995.736
	2 rate classes
	Node: mixtureTree.0557_12
	Length parameter = 0.01322564172806205
	Class 1
		omega = 0.401
		weight = 0.748
	Class 2
		omega = 0.754
		weight = 0.252

[PHASE 1] Branch 0564_5 log(L) = -5383.386, IC = 10995.927
	2 rate classes
	Node: mixtureTree.0564_5
	Length parameter = 0.0004180646056402411
	Class 1
		omega = 0.960
		weight = 0.000
	Class 2
		omega = 27.526
		weight = 1.000

[PHASE 1] Branch Node20 log(L) = -5383.284, IC = 10995.723
	2 rate classes
	Node: mixtureTree.Node20
	Length parameter = 6.782737083511655e-06
	Class 1
		omega = 1.000
		weight = 0.812
	Class 2
		omega = 8064.549
		weight = 0.188

[PHASE 1] Branch Node19 log(L) = -5383.294, IC = 10995.743
	2 rate classes
	Node: mixtureTree.Node19
	Length parameter = 0.00434603524407038
	Class 1
		omega = 0.644
		weight = 0.950
	Class 2
		omega = 28.000
		weight = 0.050

[PHASE 1] Branch 0557_25 log(L) = -5383.289, IC = 10995.734
	2 rate classes
	Node: mixtureTree.0557_25
	Length parameter = 0.008784837945265814
	Class 1
		omega = 0.601
		weight = 0.752
	Class 2
		omega = 0.998
		weight = 0.248

[PHASE 1] Branch Node35 log(L) = -5371.376, IC = 10971.907
	2 rate classes
	Node: mixtureTree.Node35
	Length parameter = 0.006129325301453111
	Class 1
		omega = 0.288
		weight = 0.999
	Class 2
		omega = 10000.000
		weight = 0.001

[PHASE 1] Branch Node35 log(L) = -5371.375659390067, IC = 10975.94788038472
	3 rate classes
	Node: mixtureTree.Node35
	Length parameter = 0.006130901612723994
	Class 1
		omega = 0.288
		weight = 0.999
	Class 2
		omega = 0.357
		weight = 0.000
	Class 3
		omega = 10000.000
		weight = 0.001

[PHASE 1] Branch Node9 log(L) = -5371.376, IC = 10975.948
	2 rate classes
	Node: mixtureTree.Node9
	Length parameter = 0.008800411044129272
	Class 1
		omega = 0.600
		weight = 0.934
	Class 2
		omega = 0.998
		weight = 0.066

[PHASE 1] Branch Node17 log(L) = -5371.432, IC = 10976.060
	2 rate classes
	Node: mixtureTree.Node17
	Length parameter = 0.0002467932361402386
	Class 1
		omega = 0.998
		weight = 0.000
	Class 2
		omega = 27.747
		weight = 1.000

[PHASE 1] Branch 0557_11 log(L) = -5372.692, IC = 10978.581
	2 rate classes
	Node: mixtureTree.0557_11
	Length parameter = 0.004944553379096365
	Class 1
		omega = 1.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node30 log(L) = -5372.413, IC = 10978.023
	2 rate classes
	Node: mixtureTree.Node30
	Length parameter = 0.003969421440630088
	Class 1
		omega = 1.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node23 log(L) = -5371.375, IC = 10975.946
	2 rate classes
	Node: mixtureTree.Node23
	Length parameter = 0.008772126953101356
	Class 1
		omega = 0.200
		weight = 0.751
	Class 2
		omega = 0.499
		weight = 0.249

[PHASE 1] Branch Node36 log(L) = -5371.374, IC = 10975.944
	2 rate classes
	Node: mixtureTree.Node36
	Length parameter = 0.004201705820497188
	Class 1
		omega = 0.605
		weight = 0.751
	Class 2
		omega = 2.019
		weight = 0.249

[PHASE 1] Branch 0564_21 log(L) = -5371.376, IC = 10975.948
	2 rate classes
	Node: mixtureTree.0564_21
	Length parameter = 0.004378473517114173
	Class 1
		omega = 0.801
		weight = 0.901
	Class 2
		omega = 1.008
		weight = 0.099

[PHASE 1] Branch Node8 log(L) = -5371.408, IC = 10976.013
	2 rate classes
	Node: mixtureTree.Node8
	Length parameter = 0.0001477224859174477
	Class 1
		omega = 0.955
		weight = 0.000
	Class 2
		omega = 34.653
		weight = 1.000

[PHASE 1] Branch Node6 log(L) = -5371.374, IC = 10975.946
	2 rate classes
	Node: mixtureTree.Node6
	Length parameter = 0.004406532615453821
	Class 1
		omega = 0.800
		weight = 0.499
	Class 2
		omega = 0.749
		weight = 0.501

[PHASE 1] Branch 0557_5 log(L) = -5371.402, IC = 10976.000
	2 rate classes
	Node: mixtureTree.0557_5
	Length parameter = 4.893259361435976e-05
	Class 1
		omega = 1.000
		weight = 0.766
	Class 2
		omega = 446.871
		weight = 0.234

[PHASE 1] Branch Node29 log(L) = -5374.954, IC = 10983.104
	2 rate classes
	Node: mixtureTree.Node29
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node18 log(L) = -5378.960, IC = 10991.116
	2 rate classes
	Node: mixtureTree.Node18
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node7 log(L) = -5371.406, IC = 10976.009
	2 rate classes
	Node: mixtureTree.Node7
	Length parameter = 0.0001357198729548026
	Class 1
		omega = 0.999
		weight = 0.000
	Class 2
		omega = 32.879
		weight = 1.000

[PHASE 1] Branch Node25 log(L) = -5371.376, IC = 10975.948
	2 rate classes
	Node: mixtureTree.Node25
	Length parameter = 0.008748045193895489
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch 0557_26 log(L) = -5371.376, IC = 10975.948
	2 rate classes
	Node: mixtureTree.0557_26
	Length parameter = 0.004408145413040281
	Class 1
		omega = 0.400
		weight = 0.951
	Class 2
		omega = 0.198
		weight = 0.049

[PHASE 1] Branch 0557_4 log(L) = -5371.376, IC = 10975.948
	2 rate classes
	Node: mixtureTree.0557_4
	Length parameter = 0.00437946608352191
	Class 1
		omega = 0.400
		weight = 0.899
	Class 2
		omega = 0.289
		weight = 0.101

[PHASE 1] Branch 0557_24 log(L) = -5371.376, IC = 10975.948
	2 rate classes
	Node: mixtureTree.0557_24
	Length parameter = 0.004379519972078364
	Class 1
		omega = 0.400
		weight = 0.950
	Class 2
		omega = 0.179
		weight = 0.050

[PHASE 1] Branch Node16 log(L) = -5371.353, IC = 10975.903
	2 rate classes
	Node: mixtureTree.Node16
	Length parameter = 0.004604717975658302
	Class 1
		omega = 0.000
		weight = 0.901
	Class 2
		omega = 0.743
		weight = 0.099

[PHASE 1] Branch 0557_9 log(L) = -5371.376, IC = 10975.948
	2 rate classes
	Node: mixtureTree.0557_9
	Length parameter = 0.004410532281439168
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch 0557_13 log(L) = -5371.376, IC = 10975.948
	2 rate classes
	Node: mixtureTree.0557_13
	Length parameter = 0.004407738329588441
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch 0557_2 log(L) = -5371.376, IC = 10975.948
	2 rate classes
	Node: mixtureTree.0557_2
	Length parameter = 0.004379542666595398
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node53 log(L) = -5371.705, IC = 10976.606
	2 rate classes
	Node: mixtureTree.Node53
	Length parameter = 0.001235189186942155
	Class 1
		omega = 1.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch 0557_6 log(L) = -5371.398, IC = 10975.994
	2 rate classes
	Node: mixtureTree.0557_6
	Length parameter = 0.0001004469766519375
	Class 1
		omega = 0.950
		weight = 0.000
	Class 2
		omega = 17.000
		weight = 1.000

[PHASE 1] Branch Node32 log(L) = -5371.375, IC = 10975.947
	2 rate classes
	Node: mixtureTree.Node32
	Length parameter = 6.51579250572735e-05
	Class 1
		omega = 0.000
		weight = 0.461
	Class 2
		omega = 28.000
		weight = 0.539

[PHASE 1] Branch 0557_7 log(L) = -5371.376, IC = 10975.948
	2 rate classes
	Node: mixtureTree.0557_7
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch 0557_21 log(L) = -5371.376, IC = 10975.948
	2 rate classes
	Node: mixtureTree.0557_21
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020


[INFERRED MODEL COMPLEXITY]
	mixtureTree.0564_7 has 1 site rate classes
	mixtureTree.0564_11 has 2 site rate classes
	mixtureTree.0564_4 has 2 site rate classes
	mixtureTree.Node20 has 1 site rate classes
	mixtureTree.0564_1 has 1 site rate classes
	mixtureTree.0564_21 has 1 site rate classes
	mixtureTree.0564_5 has 1 site rate classes
	mixtureTree.Node25 has 1 site rate classes
	mixtureTree.Node23 has 1 site rate classes
	mixtureTree.Node19 has 1 site rate classes
	mixtureTree.0564_17 has 1 site rate classes
	mixtureTree.Node18 has 1 site rate classes
	mixtureTree.0564_13 has 1 site rate classes
	mixtureTree.0564_15 has 2 site rate classes
	mixtureTree.Node32 has 1 site rate classes
	mixtureTree.Node30 has 1 site rate classes
	mixtureTree.0564_22 has 1 site rate classes
	mixtureTree.0564_6 has 1 site rate classes
	mixtureTree.Node36 has 1 site rate classes
	mixtureTree.0564_3 has 2 site rate classes
	mixtureTree.Node35 has 2 site rate classes
	mixtureTree.Node29 has 1 site rate classes
	mixtureTree.Node17 has 1 site rate classes
	mixtureTree.0564_9 has 1 site rate classes
	mixtureTree.Node16 has 1 site rate classes
	mixtureTree.0557_24 has 1 site rate classes
	mixtureTree.0557_4 has 1 site rate classes
	mixtureTree.0557_2 has 1 site rate classes
	mixtureTree.Node9 has 1 site rate classes
	mixtureTree.0557_12 has 1 site rate classes
	mixtureTree.Node8 has 1 site rate classes
	mixtureTree.0557_21 has 1 site rate classes
	mixtureTree.0557_6 has 1 site rate classes
	mixtureTree.0557_9 has 1 site rate classes
	mixtureTree.0557_11 has 1 site rate classes
	mixtureTree.0557_13 has 1 site rate classes
	mixtureTree.0557_26 has 1 site rate classes
	mixtureTree.0557_5 has 1 site rate classes
	mixtureTree.0557_7 has 1 site rate classes
	mixtureTree.Node53 has 1 site rate classes
	mixtureTree.Node6 has 1 site rate classes
	mixtureTree.0557_25 has 1 site rate classes
	mixtureTree.Node7 has 1 site rate classes
	mixtureTree.Separator has 2 site rate classes


[PHASE 2] Fitting the full LOCAL alternative model (no constraints)

Log L = -5370.694734544505 with 114 degrees of freedom, IC = 10970.54519703894
(0564_7:0.007088454582317966,(((((0564_11:0.005283070448909893,0564_4:0.007122540289258089)Node20:0.002256831578493856,(0564_1:0.005829494154689593,(0564_21:0.001215430620776803,0564_5:0.002669136546904656)Node25:0.0007972997562556671)Node23:0.001422675699985768)Node19:0.001912253255984987,0564_17:0.006054849567061774)Node18:0.001001141473680648,((0564_13:0.005308302431894629,(0564_15:0.003981209018738723)Node32:0.0002433610506589929)Node30:0.001889278185291872,((0564_22:0.006862778737626155,0564_6:0.005821816122346699)Node36:0.001258108703535457,0564_3:0.007959952917791396)Node35:0.01778034904339071)Node29:0.001039938169252163)Node17:0.001569598682729929,0564_9:0.005513323419443984)Node16:0.0007833381620451614,(((0557_24:0.0007874780473273053,0557_4:0.000787795949853966,0557_2:0.0003991144901201514)Node9:0.002063060710140481,0557_12:0.002676171483839827)Node8:0.001182385938526674,((0557_21:0,0557_6:0.0003917108246791967,0557_9:0.0004019443589702551,0557_11:0.001569238054786945,0557_13:0.000401607002512399,0557_26:0.0007934725924027982,(0557_5:0.001176293377774562,0557_7:0)Node53:0.0003917965601129415)Node6:0.00118053400223825,0557_25:0.002204275461279037)Node7:0.001032401971171487)Separator:0.008179460483872228)

Node: mixtureTree.0564_7
	Length parameter = 0.03106541992549355
	Class 1: omega =     0.6140, weight = 1.

Node: mixtureTree.0564_11
	Length parameter = 0.02339827233227691
	Class 1
		omega = 0.000
		weight = 0.986
	Class 2
		omega = 42.382
		weight = 0.014
...Testing for selection at this branch

Node: mixtureTree.0564_11
	Length parameter = 0.02550382774594972
	Class 1
		omega = 0.000
		weight = 0.632
	Class 2
		omega = 1.000
		weight = 0.368
p-value = 0.05067621014262741

Node: mixtureTree.0564_4
	Length parameter = 0.03121472895493074
	Class 1
		omega = 0.000
		weight = 0.979
	Class 2
		omega = 28.591
		weight = 0.021
...Testing for selection at this branch

Node: mixtureTree.0564_4
	Length parameter = 0.03533350146670629
	Class 1
		omega = 0.000
		weight = 0.617
	Class 2
		omega = 1.000
		weight = 0.383
p-value = 0.03292577515587841

Node: mixtureTree.Node20
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node20
	Length parameter = 0.00725024320110249
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.07173983869012199

Node: mixtureTree.0564_1
	Length parameter = 0.01767868452316691
	Class 1: omega =     1.0666, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.0564_1
	Length parameter = 0.01853304999630758
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.4887088065159598

Node: mixtureTree.0564_21
	Length parameter = 0.00440438158263353
	Class 1: omega =     0.8269, weight = 1.

Node: mixtureTree.0564_5
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.0564_5
	Length parameter = 0.008502948600092021
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.03799188272337667

Node: mixtureTree.Node25
	Length parameter = 0.008821717159773876
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node23
	Length parameter = 0.008852759190424142
	Class 1: omega =     0.3134, weight = 1.

Node: mixtureTree.Node19
	Length parameter = 0.004398723875676172
	Class 1: omega =     1.5344, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node19
	Length parameter = 0.006047040828282396
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.4184619902992749

Node: mixtureTree.0564_17
	Length parameter = 0.02647987465797049
	Class 1: omega =     0.6162, weight = 1.

Node: mixtureTree.Node18
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node18
	Length parameter = 0.003030085315888874
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.171735134747737

Node: mixtureTree.0564_13
	Length parameter = 0.0399616281416774
	Class 1: omega =     0.1892, weight = 1.

Node: mixtureTree.0564_15
	Length parameter = 0.01780532363490646
	Class 1
		omega = 0.000
		weight = 0.992
	Class 2
		omega = 72.163
		weight = 0.008
...Testing for selection at this branch

Node: mixtureTree.0564_15
	Length parameter = 0.02015163748489334
	Class 1
		omega = 0.000
		weight = 0.609
	Class 2
		omega = 1.000
		weight = 0.391
p-value = 0.0308769838944386

Node: mixtureTree.Node32
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node32
	Length parameter = 0.0005711607549367886
	Class 1: omega =     0.9713, weight = 1.
p-value = 0.5

Node: mixtureTree.Node30
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node30
	Length parameter = 0.005506809929958164
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.0909866105820745

Node: mixtureTree.0564_22
	Length parameter = 0.01891869142408899
	Class 1: omega =     1.2137, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.0564_22
	Length parameter = 0.02184266755635216
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.431920242696882

Node: mixtureTree.0564_6
	Length parameter = 0.03491190209336761
	Class 1: omega =     0.3403, weight = 1.

Node: mixtureTree.Node36
	Length parameter = 0.004221969664588807
	Class 1: omega =     0.9251, weight = 1.

Node: mixtureTree.0564_3
	Length parameter = 0.007866505596165387
	Class 1
		omega = 0.025
		weight = 0.970
	Class 2
		omega = 134.222
		weight = 0.030
...Testing for selection at this branch

Node: mixtureTree.0564_3
	Length parameter = 0.02033326384163266
	Class 1
		omega = 1.000
		weight = 0.981
	Class 2
		omega = 1.000
		weight = 0.019
p-value = 0.0003050423351747544

Node: mixtureTree.Node35
	Length parameter = 0.006247275947452194
	Class 1
		omega = 0.000
		weight = 0.999
	Class 2
		omega = 10000.000
		weight = 0.001
...Testing for selection at this branch

Node: mixtureTree.Node35
	Length parameter = 0.01515861865697306
	Class 1
		omega = 0.000
		weight = 0.744
	Class 2
		omega = 1.000
		weight = 0.256
p-value = 4.060589981036422e-06

Node: mixtureTree.Node29
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node29
	Length parameter = 0.002575757982303865
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.188100181193604

Node: mixtureTree.Node17
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node17
	Length parameter = 0.005011930813713058
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.1015315342846008

Node: mixtureTree.0564_9
	Length parameter = 0.02189309829075847
	Class 1: omega =     0.7194, weight = 1.

Node: mixtureTree.Node16
	Length parameter = 0.00466925607694316
	Class 1: omega =     0.3448, weight = 1.

Node: mixtureTree.0557_24
	Length parameter = 0.004414768019874817
	Class 1: omega =     0.3921, weight = 1.

Node: mixtureTree.0557_4
	Length parameter = 0.004416355588960351
	Class 1: omega =     0.3921, weight = 1.

Node: mixtureTree.0557_2
	Length parameter = 0.004415999275783443
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node9
	Length parameter = 0.008871554392652059
	Class 1: omega =     0.6335, weight = 1.

Node: mixtureTree.0557_12
	Length parameter = 0.01330733843801253
	Class 1: omega =     0.4934, weight = 1.

Node: mixtureTree.Node8
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node8
	Length parameter = 0.003768588296365975
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.1425270214621213

Node: mixtureTree.0557_21
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.0557_6
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.0557_6
	Length parameter = 0.00125282395054211
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.2987880605037365

Node: mixtureTree.0557_9
	Length parameter = 0.004447310338403239
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.0557_11
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.0557_11
	Length parameter = 0.005016161190416183
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.1003506218053049

Node: mixtureTree.0557_13
	Length parameter = 0.004443577660411204
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.0557_26
	Length parameter = 0.004443624868603909
	Class 1: omega =     0.3929, weight = 1.

Node: mixtureTree.0557_5
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.0557_5
	Length parameter = 0.003761421722444685
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.1427038910063564

Node: mixtureTree.0557_7
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node53
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node53
	Length parameter = 0.001253824541119446
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.2987794250025005

Node: mixtureTree.Node6
	Length parameter = 0.004449641873623388
	Class 1: omega =     0.7795, weight = 1.

Node: mixtureTree.0557_25
	Length parameter = 0.008858370245614512
	Class 1: omega =     0.7061, weight = 1.

Node: mixtureTree.Node7
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node7
	Length parameter = 0.003087826049324969
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.1677442536456643

Node: mixtureTree.Separator
	Length parameter = 0.004366618326246096
	Class 1
		omega = 0.000
		weight = 0.959
	Class 2
		omega = 191.994
		weight = 0.041
...Testing for selection at this branch

Node: mixtureTree.Separator
	Length parameter = 0.02117451663476626
	Class 1
		omega = 1.000
		weight = 0.981
	Class 2
		omega = 1.000
		weight = 0.019
p-value = 0.0002913312075021879


Summary of branches under episodic selection (44 were tested, of which 22 required optimizations) :
	Node35 p = 0.000182726549146639
	Separator p = 0.01281857313009627
	0564_3 p = 0.01311682041251444


 === CPU TIME REPORT === 
	MG94xREV model fit : 00:00:18
	Rate class complexity analysis : 00:02:24
	Adaptive model fit : 00:00:15
	Individual branch selection testing : 00:05:58
	Total time : 00:08:56

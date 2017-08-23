
Analysis Description
--------------------
FEL (Fixed Effects Likelihood) estimates site-wise synonymous (&alpha;)
and non-synonymous (&beta;) rates, and uses a likelihood ratio test to
determine if beta &neq; alpha at a site. The estimates aggregate
information over all branches, so the signal is derived from pervasive
diversification or conservation. A subset of branches can be selected
for testing as well, in which case an additional (nuisance) parameter
will be inferred -- the non-synonymous rate on branches NOT selected for
testing. Multiple partitions within a NEXUS file are also supported for
recombination - aware analysis. 

- __Requirements__: in-frame codon alignment and a phylogenetic tree

- __Citation__: Not So Different After All: A Comparison of Methods for Detecting Amino
Acid Sites Under Selection (2005). _Mol Biol Evol_ 22 (5): 1208-1222

- __Written by__: Sergei L Kosakovsky Pond and Simon DW Frost

- __Contact Information__: spond@temple.edu

- __Analysis Version__: 2.00



>A tree was found in the data file: `((((Pig:0.147969,Cow:0.213430):0.085099,Horse:0.165787,Cat:0.264806):0.058611,((RhMonkey:0.002015,Baboon:0.003108):0.022733,(Human:0.004349,Chimp:0.000799):0.011873):0.101856):0.340802,Rat:0.050958,Mouse:0.097950)`

>Would you like to use it (y/n)? Y


>Loaded a multiple sequence alignment with **10** sequences, **187** codons, and **1** partitions from `/home/sjspielman/book-chapter-2017/datasets/CD2.dat`
Yes

>Select the p-value used to for perform the test at (permissible range = [0,1], default value = 0.1): 0.1


### Branches to include in the FEL analysis
Selected 16 branches to include in FEL calculations: `Pig, Cow, Node3, Horse, Cat, Node2, RhMonkey, Baboon, Node9, Human, Chimp, Node12, Node8, Node1, Rat, Mouse`


### Obtaining branch lengths and nucleotide substitution biases under the nucleotide GTR model
* Log(L) = -3531.96, AIC-c =  7112.14 (24 estimated parameters)

### Obtaining the global omega estimate based on relative GTR branch lengths and nucleotide substitution biases
* Log(L) = -3467.07, AIC-c =  6997.22 (31 estimated parameters)
* non-synonymous/synonymous rate ratio for *test* =   1.0088

### Improving branch lengths, nucleotide substitution biases, and global dN/dS ratios under a full codon model
* Log(L) = -3466.77
* non-synonymous/synonymous rate ratio =   0.9947

### For partition 1 these sites are significant at p <=0.1

|     Codon      |   Partition    |     alpha      |      beta      |      LRT       |Selection detected?|
|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:-----------------:|
|       9        |       1        |        0.000   |        1.509   |        4.179   |  Pos. p = 0.0409  |
|       11       |       1        |        1.575   |        0.000   |        5.835   |  Neg. p = 0.0157  |
|       22       |       1        |        0.717   |        0.000   |        2.874   |  Neg. p = 0.0900  |
|       31       |       1        |       65.396   |        0.510   |        7.989   |  Neg. p = 0.0047  |
|       34       |       1        |        0.000   |        2.353   |        4.435   |  Pos. p = 0.0352  |
|       36       |       1        |      324.557   |        3.194   |        6.783   |  Neg. p = 0.0092  |
|       45       |       1        |        1.493   |        0.000   |        5.526   |  Neg. p = 0.0187  |
|       47       |       1        |       12.589   |        0.310   |        5.775   |  Neg. p = 0.0163  |
|       53       |       1        |        0.000   |        1.115   |        2.749   |  Pos. p = 0.0973  |
|       55       |       1        |        0.000   |        7.000   |        3.851   |  Pos. p = 0.0497  |
|       60       |       1        |        5.041   |        0.419   |        3.187   |  Neg. p = 0.0742  |
|       64       |       1        |        0.000   |        2.130   |        3.339   |  Pos. p = 0.0676  |
|       65       |       1        |       58.148   |        0.000   |       11.090   |  Neg. p = 0.0009  |
|       70       |       1        |        1.161   |        0.000   |        3.108   |  Neg. p = 0.0779  |
|       71       |       1        |        1.793   |        0.000   |        3.627   |  Neg. p = 0.0568  |
|       78       |       1        |        3.455   |        0.246   |        3.970   |  Neg. p = 0.0463  |
|       81       |       1        |        0.000   |        1.476   |        4.055   |  Pos. p = 0.0440  |
|       82       |       1        |        3.491   |        0.000   |        6.201   |  Neg. p = 0.0128  |
|       87       |       1        |       58.148   |        0.000   |       15.082   |  Neg. p = 0.0001  |
|       95       |       1        |        1.224   |        0.000   |        3.597   |  Neg. p = 0.0579  |
|       98       |       1        |        0.000   |        1.894   |        2.830   |  Pos. p = 0.0925  |
|      102       |       1        |        0.000   |        1.868   |        2.956   |  Pos. p = 0.0856  |
|      106       |       1        |        0.000   |        1.788   |        2.920   |  Pos. p = 0.0875  |
|      110       |       1        |        2.982   |        0.000   |        9.224   |  Neg. p = 0.0024  |
|      113       |       1        |        0.000   |        2.460   |        5.630   |  Pos. p = 0.0177  |
|      116       |       1        |        4.002   |        0.000   |        7.781   |  Neg. p = 0.0053  |
|      117       |       1        |        0.000   |        2.011   |        5.237   |  Pos. p = 0.0221  |
|      120       |       1        |        1.198   |        0.000   |        4.702   |  Neg. p = 0.0301  |
|      123       |       1        |        4.405   |        0.000   |        7.963   |  Neg. p = 0.0048  |
|      125       |       1        |        1.318   |        0.000   |        4.516   |  Neg. p = 0.0336  |
|      129       |       1        |        2.561   |        0.256   |        3.356   |  Neg. p = 0.0670  |
|      130       |       1        |        3.520   |        0.233   |        4.233   |  Neg. p = 0.0396  |
|      132       |       1        |        3.863   |        0.300   |        3.410   |  Neg. p = 0.0648  |
|      133       |       1        |        1.348   |        0.000   |        3.555   |  Neg. p = 0.0593  |
|      136       |       1        |       10.443   |        0.402   |        3.862   |  Neg. p = 0.0494  |
|      149       |       1        |        0.000   |        1.966   |        5.211   |  Pos. p = 0.0224  |
|      164       |       1        |       10.070   |        0.000   |        8.463   |  Neg. p = 0.0036  |
|      166       |       1        |        3.794   |        0.000   |       11.626   |  Neg. p = 0.0007  |
|      172       |       1        |        0.000   |        2.196   |        2.914   |  Pos. p = 0.0878  |
|      176       |       1        |      137.191   |        1.709   |        4.568   |  Neg. p = 0.0326  |

### ** Found _13_ sites under pervasive positive diversifying and _27_ sites under negative selection at p <= 0.1**

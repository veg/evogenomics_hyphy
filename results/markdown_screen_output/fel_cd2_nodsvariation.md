
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


>Loaded a multiple sequence alignment with **10** sequences, **187** codons, and **1** partitions from `/home/sjspielman/book-chapter-2017/datasets/CD2-ds1.dat`
No

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
|       11       |       1        |        1.000   |        0.000   |        3.307   |  Neg. p = 0.0690  |
|       34       |       1        |        1.000   |        2.336   |        3.331   |  Pos. p = 0.0680  |
|       45       |       1        |        1.000   |        0.000   |        5.510   |  Neg. p = 0.0189  |
|       47       |       1        |        1.000   |        0.344   |        4.006   |  Neg. p = 0.0453  |
|       65       |       1        |        1.000   |        0.000   |        6.428   |  Neg. p = 0.0112  |
|       78       |       1        |        1.000   |        0.247   |        3.969   |  Neg. p = 0.0463  |
|       82       |       1        |        1.000   |        0.000   |        4.144   |  Neg. p = 0.0418  |
|       87       |       1        |        1.000   |        0.000   |        7.144   |  Neg. p = 0.0075  |
|       95       |       1        |        1.000   |        0.000   |        3.458   |  Neg. p = 0.0629  |
|      110       |       1        |        1.000   |        0.000   |        8.783   |  Neg. p = 0.0030  |
|      113       |       1        |        1.000   |        2.471   |        4.978   |  Pos. p = 0.0257  |
|      116       |       1        |        1.000   |        0.000   |        7.673   |  Neg. p = 0.0056  |
|      117       |       1        |        1.000   |        2.034   |        3.675   |  Pos. p = 0.0552  |
|      120       |       1        |        1.000   |        0.000   |        4.700   |  Neg. p = 0.0302  |
|      123       |       1        |        1.000   |        0.000   |        4.232   |  Neg. p = 0.0397  |
|      125       |       1        |        1.000   |        0.000   |        4.357   |  Neg. p = 0.0369  |
|      133       |       1        |        1.000   |        0.000   |        3.052   |  Neg. p = 0.0807  |
|      149       |       1        |        1.000   |        1.980   |        3.458   |  Pos. p = 0.0629  |
|      166       |       1        |        1.000   |        0.000   |       10.380   |  Neg. p = 0.0013  |

### ** Found _4_ sites under pervasive positive diversifying and _15_ sites under negative selection at p <= 0.1**

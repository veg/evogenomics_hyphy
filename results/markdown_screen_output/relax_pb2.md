
Analysis Description
--------------------
RELAX (a random effects test of selection relaxation) uses a random
effects branch-site model framework to test whether a set of 'Test'
branches evolves under relaxed selection relative to a set of
'Reference' branches (R), as measured by the relaxation parameter (K).

- __Requirements__: in-frame codon alignment and a phylogenetic tree, with at least two
groups of branches defined using the {} notation (one group can be
defined as all unlabeled branches)

- __Citation__: RELAX: Detecting Relaxed Selection in a Phylogenetic Framework (2015).
Mol Biol Evol 32 (3): 820-832

- __Written by__: Sergei L Kosakovsky Pond, Ben Murrell, Steven Weaver and Temple iGEM /
UCSD viral evolution group

- __Contact Information__: spond@temple.edu

- __Analysis Version__: 2.0



>A tree was found in the data file: `(((((((Av_ABC66473:0.045949,Av_ABJ96574:0.031552):0.02814,((Av_AAY52745:0.141366,Av_AAY52761:0.048115):0.180843,((Av_AAY52751:0.112402,Av_ABB90192:0.034326):0.044822,Av_ABI94746:0.030777):0.04108):0.012085):0.016435,Av_AAT12009:0.072772):0.03242,(Av_ABD35787:0.114701,(Av_ABJ51683:0.123626,Av_AAT12010:0.056119):0.019073):0.024954):0.013721,Av_ABB88297:0.055049):0.153994,(Av_AAY52756:0.47258,(Av_ABB20293:0.040069,Av_ABB88341:0.123112):0.127339):0.01086):0.277788,(((((Av_ABB19866:0.05611,Av_ABB18090:0.101705):0.017978,Av_ABI92279:0.104957):0.053878,Av_ABI95161:0.082436):0.007775,Av_ABB21803:0.070929):0.267348,(((((((((Hu_AAY98236{test}:0.013554,Hu_AAZ83322{test}:0.008106){test}:0,Hu_ABD79166{test}:0.027317){test}:0.004193,Hu_ABD59810{test}:0.040865){test}:0.088022,Hu_AAK18016{test}:0.062666){test}:0.037501,Hu_ABB04304{test}:0.020115){test}:0,Hu_ABC40554{test}:0.011987){test}:0.132231,Hu_AAA43648{test}:0.018738){test}:0.095239,((((Hu_ABB02813{test}:0.024775,Hu_ABD63073{test}:0.004869){test}:0.119142,Hu_ABI30388{test}:0.021278){test}:0.002595,(Hu_ABM22256{test}:0.012339,Hu_ABF21232{test}:0.003797){test}:0.041478){test}:0.001479,Hu_ABI92312{test}:0.03642){test}:0.085679){test}:0.064268,Hu_CAA23855{test}:0.044636){test}:0.232812):0.160917)`

>Would you like to use it (y/n)? Y


>Loaded a multiple sequence alignment with **35** sequences, **759** codons, and **1** partitions from `/home/sjspielman/book-chapter-2017/datasets/pb2.dat`


### Branch sets for RELAX analysis
* Selected 29 branches as the _test_ set: `Hu_AAY98236, Hu_AAZ83322, Node48, Hu_ABD79166, Node47, Hu_ABD59810, Node46, Hu_AAK18016, Node45, Hu_ABB04304, Node44, Hu_ABC40554, Node43, Hu_AAA43648, Node42, Hu_ABB02813, Hu_ABD63073, Node60, Hu_ABI30388, Node59, Hu_ABM22256, Hu_ABF21232, Node64, Node58, Hu_ABI92312, Node57, Node41, Hu_CAA23855, Node40`
* Selected 38 branches as the _reference_ set: `Av_ABC66473, Av_ABJ96574, Node6, Av_AAY52745, Av_AAY52761, Node10, Av_AAY52751, Av_ABB90192, Node14, Av_ABI94746, Node13, Node9, Node5, Av_AAT12009, Node4, Av_ABD35787, Av_ABJ51683, Av_AAT12010, Node21, Node19, Node3, Av_ABB88297, Node2, Av_AAY52756, Av_ABB20293, Av_ABB88341, Node27, Node25, Av_ABB19866, Av_ABB18090, Node34, Av_ABI92279, Node33, Av_ABI95161, Node32, Av_ABB21803, Node31, Node30`


### Obtaining branch lengths and nucleotide substitution biases under the nucleotide GTR model
* Log(L) = -16755.26, AIC-c = 33660.66 (75 estimated parameters)

### Obtaining the global omega estimate based on relative GTR branch lengths and nucleotide substitution biases
* Log(L) = -14411.03, AIC-c = 28988.58 (83 estimated parameters)
* non-synonymous/synonymous rate ratio for *Reference* =   0.0401
* non-synonymous/synonymous rate ratio for *Test* =   0.0604

### Improving branch lengths, nucleotide substitution biases, and global dN/dS ratios under a full codon model
* Log(L) = -14354.67, AIC-c = 28875.86 (83 estimated parameters)
* non-synonymous/synonymous rate ratio for *Reference* =   0.0359
* non-synonymous/synonymous rate ratio for *Test* =   0.0609

### Fitting the general descriptive (separate k per branch) model

### * Log(L) = -14220.26, AIC-c = 28746.27 (152 estimated parameters)
* The following baseline rate distribution for branch-site combinations was inferred

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.013     |   99.562    |                                   |
|         Neutral evolution         |     1.000     |    0.000    |       Not supported by data       |
|      Diversifying selection       |     1.146     |    0.438    |                                   |

* Branch-level relaxation or intensification parameter distribution has mean  2.08, median  0.78, and 95% of the weight in  0.02 - 22.12

### Fitting the alternative model to test K != 1
* Log(L) = -14337.20, AIC-c = 28848.98 (87 estimated parameters)
* Relaxation/intensification parameter (K) =     0.67
* The following rate distribution was inferred for **test** branches

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.028     |   96.813    |                                   |
|        Negative selection         |     0.494     |    0.005    |       Not supported by data       |
|      Diversifying selection       |     1.174     |    3.182    |                                   |

* The following rate distribution was inferred for **reference** branches

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.005     |   96.813    |                                   |
|        Negative selection         |     0.350     |    0.005    |       Not supported by data       |
|      Diversifying selection       |     1.270     |    3.182    |                                   |


### Fitting the null (K := 1) model
* Log(L) = -14342.36, AIC-c = 28857.28 (86 estimated parameters)
* The following rate distribution for test/reference branches was inferred

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.006     |   96.378    |                                   |
|        Negative selection         |     0.020     |    0.376    |                                   |
|      Diversifying selection       |     1.426     |    3.246    |                                   |

----
## Test for relaxation (or intensification) of selection [RELAX]
Likelihood ratio test **p =   0.0013**.
>Evidence for intensification of selection among **test** branches _relative_ to the **reference** branches at P<=0.05
----


### Fitting the partitioned exploratory model (separate distributions for *test* and *reference* branches)
* Log(L) = -14336.27, AIC-c = 28853.16 (90 estimated parameters)
* The following rate distribution was inferred for *test* branches 

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.000     |    0.137    |                                   |
|        Negative selection         |     0.008     |   95.512    |                                   |
|      Diversifying selection       |     1.454     |    4.351    |                                   |

* The following rate distribution was inferred for *reference* branches 

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.008     |   96.831    |                                   |
|        Negative selection         |     0.269     |    0.830    |                                   |
|      Diversifying selection       |     1.454     |    2.338    |                                   |


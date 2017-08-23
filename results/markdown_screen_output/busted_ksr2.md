
Analysis Description
--------------------
BUSTED (branch-site unrestricted statistical test of episodic
diversification) uses a random effects branch-site model fitted jointly
to all or a subset of tree branches in order to test for alignment-wide
evidence of episodic diversifying selection. Assuming there is evidence
of positive selection (i.e. there is an omega > 1), BUSTED will also
perform a quick evidence-ratio style analysis to explore which
individual sites may have been subject to selection.

- __Requirements__: in-frame codon alignment and a phylogenetic tree (optionally annotated
with {})

- __Citation__: *Gene-wide identification of episodic selection*, Mol Biol Evol.
32(5):1365-71

- __Written by__: Sergei L Kosakovsky Pond

- __Contact Information__: spond@temple.edu

- __Analysis Version__: 1.2



>A tree was found in the data file: `(((((((HUM,PAN),GOR),PON),GIB),(MAC,BAB)),MAR),BUS)`

>Would you like to use it (y/n)? Y


>Loaded a multiple sequence alignment with **9** sequences, **949** codons, and **1** partitions from `/home/sjspielman/book-chapter-2017/datasets/ksr2.dat`


### Branches to test for selection in the BUSTED analysis
* Selected 15 branches to test in the BUSTED analysis: `HUM, PAN, Node6, GOR, Node5, PON, Node4, GIB, Node3, MAC, BAB, Node12, Node2, MAR, BUS`


### Obtaining branch lengths and nucleotide substitution biases under the nucleotide GTR model
* Log(L) = -5768.01, AIC-c = 11582.06 (23 estimated parameters)

### Obtaining the global omega estimate based on relative GTR branch lengths and nucleotide substitution biases
* Log(L) = -5342.48, AIC-c = 10745.17 (30 estimated parameters)
* non-synonymous/synonymous rate ratio for *test* =   0.0342

### Improving branch lengths, nucleotide substitution biases, and global dN/dS ratios under a full codon model
* Log(L) = -5333.46, AIC-c = 10727.13 (30 estimated parameters)
* non-synonymous/synonymous rate ratio for *test* =   0.0307

### Performing the full (dN/dS > 1 allowed) branch-site model fit
* Log(L) = -5319.67, AIC-c = 10707.62 (34 estimated parameters)
* For *test* branches, the following rate distribution for branch-site combinations was inferred

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.024     |   99.151    |                                   |
|        Negative selection         |     0.085     |    0.812    |                                   |
|      Diversifying selection       |    118.143    |    0.037    |                                   |


### Performing the constrained (dN/dS > 1 not allowed) model fit
* Log(L) = -5326.18, AIC-c = 10718.63 (33 estimated parameters)
* For *test* branches under the null (no dN/dS > 1 model), the following rate distribution for branch-site combinations was inferred

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.000     |   10.598    |                                   |
|        Negative selection         |     0.000     |   86.086    |       Collapsed rate class        |
|         Neutral evolution         |     1.000     |    3.316    |                                   |

----
## Branch-site unrestricted statistical test of episodic diversification [BUSTED]
Likelihood ratio test for episodic diversifying positive selection, **p =   0.0015**.

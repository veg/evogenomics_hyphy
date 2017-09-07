### Branches to test for selection in the BUSTED analysis
* Selected 20 branches to test in the BUSTED analysis: `0564_7, 0557_24, 0557_4, 0557_2, Node28, 0557_12, Node27, 0557_21, 0557_6, 0557_9, 0557_11, 0557_13, 0557_26, 0557_5, 0557_7, Node41, Node34, 0557_25, Node33, Node26`


### Obtaining branch lengths and nucleotide substitution biases under the nucleotide GTR model
* Log(L) = -5524.50, AIC-c = 11153.08 (52 estimated parameters)

### Obtaining the global omega estimate based on relative GTR branch lengths and nucleotide substitution biases
* Log(L) = -5436.24, AIC-c = 10992.80 (60 estimated parameters)
* non-synonymous/synonymous rate ratio for *background* =   0.8248
* non-synonymous/synonymous rate ratio for *test* =   0.8811

### Improving branch lengths, nucleotide substitution biases, and global dN/dS ratios under a full codon model
* Log(L) = -5435.93, AIC-c = 10992.18 (60 estimated parameters)
* non-synonymous/synonymous rate ratio for *background* =   0.7827
* non-synonymous/synonymous rate ratio for *test* =   0.9766

### Performing the full (dN/dS > 1 allowed) branch-site model fit
* Log(L) = -5417.81, AIC-c = 10972.03 (68 estimated parameters)
* For *test* branches, the following rate distribution for branch-site combinations was inferred

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.000     |   18.405    |                                   |
|        Negative selection         |     0.000     |   72.866    |       Collapsed rate class        |
|      Diversifying selection       |    11.820     |    8.729    |                                   |

* For *background* branches, the following rate distribution for branch-site combinations was inferred

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.000     |   86.210    |                                   |
|        Negative selection         |     0.016     |    9.561    |                                   |
|      Diversifying selection       |    20.607     |    4.229    |                                   |


### Performing the constrained (dN/dS > 1 not allowed) model fit
* Log(L) = -5420.45, AIC-c = 10975.31 (67 estimated parameters)
* For *test* branches under the null (no dN/dS > 1 model), the following rate distribution for branch-site combinations was inferred

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.000     |    9.325    |                                   |
|        Negative selection         |     0.769     |    0.000    |       Not supported by data       |
|         Neutral evolution         |     1.000     |   90.675    |                                   |

----
## Branch-site unrestricted statistical test of episodic diversification [BUSTED]
Likelihood ratio test for episodic diversifying positive selection, **p =   0.0708**.

Check messages.log details of this run.

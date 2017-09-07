
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



####Choose Genetic Code

1. [**Universal**] Universal code. (Genebank transl_table=1).
2. [**Vertebrate mtDNA**] Vertebrate mitochondrial DNA code. (Genebank transl_table=2).
3. [**Yeast mtDNA**] Yeast mitochondrial DNA code. (Genebank transl_table=3).
4. [**Mold/Protozoan mtDNA**] Mold, Protozoan and Coelenterate mitochondrial DNA and the Mycloplasma/Spiroplasma code. (Genebank transl_table=4).
5. [**Invertebrate mtDNA**] Invertebrate mitochondrial DNA code. (Genebank transl_table=5).
6. [**Ciliate Nuclear**] Ciliate, Dasycladacean and Hexamita Nuclear code. (Genebank transl_table=6).
7. [**Echinoderm mtDNA**] Echinoderm mitochondrial DNA code. (Genebank transl_table=9).
8. [**Euplotid Nuclear**] Euplotid Nuclear code. (Genebank transl_table=10).
9. [**Alt. Yeast Nuclear**] Alternative Yeast Nuclear code. (Genebank transl_table=12).
10. [**Ascidian mtDNA**] Ascidian mitochondrial DNA code. (Genebank transl_table=13).
11. [**Flatworm mtDNA**] Flatworm mitochondrial DNA code. (Genebank transl_table=14).
12. [**Blepharisma Nuclear**] Blepharisma Nuclear code. (Genebank transl_table=15).
13. [**Chlorophycean mtDNA**] Chlorophycean Mitochondrial Code (transl_table=16).
14. [**Trematode mtDNA**] Trematode Mitochondrial Code (transl_table=21).
15. [**Scenedesmus obliquus mtDNA**] Scenedesmus obliquus mitochondrial Code (transl_table=22).
16. [**Thraustochytrium mtDNA**] Thraustochytrium Mitochondrial Code (transl_table=23).
17. [**Pterobranchia mtDNA**] Pterobranchia Mitochondrial Code (transl_table=24).
18. [**SR1 and Gracilibacteria**] Candidate Division SR1 and Gracilibacteria Code (transl_table=25).
19. [**Pachysolen Nuclear**] Pachysolen tannophilus Nuclear Code (transl_table=26).

>Please choose an option (or press q to cancel selection):1


>Select a coding sequence alignment file (`/Volumes/sergei-raid/hyphy2.3/res/TemplateBatchFiles/SelectionAnalyses/`) /Volumes/sergei-raid/Dropbox/Work/Coauthored/book-chapter-2017/exercises/hiv1_transmission_exercise1.fna


>A tree was found in the data file: `(0564_7{test},(((((0564_11,0564_4),(0564_1,(0564_21,0564_5))),0564_17),((0564_13,(0564_15)),((0564_22,0564_6),0564_3))),0564_9),(((0557_24{test},0557_4{test},0557_2{test}){test},0557_12{test}){test},((0557_21{test},0557_6{test},0557_9{test},0557_11{test},0557_13{test},0557_26{test},(0557_5{test},0557_7{test}){test}){test},0557_25{test}){test}){test})`

>Would you like to use it (y/n)? y


>Loaded a multiple sequence alignment with **26** sequences, **877** codons, and **1** partitions from `/Volumes/sergei-raid/Dropbox/Work/Coauthored/book-chapter-2017/exercises/hiv1_transmission_exercise1.fna`


####Choose the set of branches to test for selection

1. [**All**] Include all branches in the analysis
2. [**Internal**] Include all internal branches in the analysis
3. [**Leaves**] Include all leaf branches in the analysis
4. [**test**] Set test with 20 branches
5. [**Unlabeled branches**] Set of 24 unlabeled branches

>Please choose an option (or press q to cancel selection):4


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
* non-synonymous/synonymous rate ratio for *background* =   0.7820
* non-synonymous/synonymous rate ratio for *test* =   0.9754

### Performing the full (dN/dS > 1 allowed) branch-site model fit
* Log(L) = -5417.81, AIC-c = 10972.03 (68 estimated parameters)
* For *test* branches, the following rate distribution for branch-site combinations was inferred

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.000     |   18.078    |                                   |
|        Negative selection         |     0.000     |   73.209    |       Collapsed rate class        |
|      Diversifying selection       |    11.836     |    8.713    |                                   |

* For *background* branches, the following rate distribution for branch-site combinations was inferred

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.000     |    6.686    |                                   |
|        Negative selection         |     0.000     |   89.064    |       Collapsed rate class        |
|      Diversifying selection       |    20.546     |    4.250    |                                   |


### Performing the constrained (dN/dS > 1 not allowed) model fit
* Log(L) = -5420.44, AIC-c = 10975.28 (67 estimated parameters)
* For *test* branches under the null (no dN/dS > 1 model), the following rate distribution for branch-site combinations was inferred

|          Selection mode           |     dN/dS     |Proportion, %|               Notes               |
|-----------------------------------|---------------|-------------|-----------------------------------|
|        Negative selection         |     0.000     |    9.315    |                                   |
|        Negative selection         |     0.832     |    0.000    |       Not supported by data       |
|         Neutral evolution         |     1.000     |   90.685    |                                   |

----
## Branch-site unrestricted statistical test of episodic diversification [BUSTED]
Likelihood ratio test for episodic diversifying positive selection, **p =   0.0719**.

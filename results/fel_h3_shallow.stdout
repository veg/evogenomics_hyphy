
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


> A tree was found in the data file: `(KF790049:0.001255,((((((((CY134956:0.000624,CY183153:0.000624):0.0,(CY186123:0.000624,CY186051:0.000624):0.0):0.0,(((CY182809:0.000624,(((CY148436:0.0,CY168583:0.000624):0.0,CY170911:0.000624):0.0,KF789547:0.00125):0.000624):0.0,(CY186019:0.000625,(CY182889:0.000624,CY135132:0.0):0.00125):0.000624):0.0,((CY170799:0.001249,CY149260:0.000624):0.0,((CY134686:0.0,(CY168887:0.000625,KF790064:0.001249):0.0):0.000625,CY169023:0.000625):0.000624):0.0):0.0):0.0,((((CY183049:0.000624,((KF789535:0.001876,CY134740:0.000624):0.0,KF790356:0.000624):0.0):0.0,(((((CY182737:0.000624,(CY168663:0.001879,KF789752:0.001253):0.000623):0.0,(CY186059:0.000624,CY183193:0.001249):0.000625):0.0,CY141264:0.000624):0.0,CY183113:0.000624):0.0,(((CY183241:0.000624,((((CY134828:0.0,KF199858:0.000625):0.0,(CY135124:0.000624,(CY134780:0.000624,CY168871:0.001249):0.0):0.0):0.0,CY135060:0.000624):0.0,KF789614:0.000624):0.0):0.000624,CY183033:0.000626):0.0,(CY168599:0.001249,(CY168063:0.0,(CY148364:0.000624,CY148596:0.000624):0.0):0.0):0.001248):0.0):0.0):0.0,CY134844:0.0):0.0,CY182865:0.000624):0.0):0.0,CY183185:0.000624):0.0,((((((CY186035:0.001249,CY183081:0.000624):0.0,CY135044:0.000624):0.0,KF789780:0.0):0.0,CY182793:0.000624):0.000624,((CY186235:0.002501,(CY134788:0.0,((((((CY170479:0.001265,KF790106:0.0):0.000624,CY141230:0.000624):0.0,(CY149084:0.0,CY169199:0.001249):0.001249):0.0,(KF789618:0.000624,CY141176:0.00125):0.0):0.0,(KF790361:0.000624,(CY141213:0.000625,(CY170647:0.000624,((((KF790316:0.000625,CY169535:0.000624):0.000624,CY170967:0.000624):0.0,(CY169527:0.000624,CY148348:0.0):0.000624):0.0,(CY168759:0.000624,CY170767:0.0):0.0):0.0):0.000624):0.0):0.0):0.0,CY141280:0.000625):0.000624):0.000625):0.0,CY182777:0.000623):0.0):0.0,((KF790448:0.000624,(CY183225:0.000625,CY134764:0.0):0.0):0.000624,(((KF790345:0.000624,(((CY182945:0.000624,CY186075:0.0):0.0,(KF790011:0.0,CY147297:0.000624):0.001249):0.0,(KF886358:0.001249,KF789871:0.003135):0.0):0.0):0.000624,((((KF790286:0.001248,(CY170991:0.0,CY171303:0.000624):0.0):0.00125,(KF886340:0.001879,CY147295:0.000627):0.001255):0.0,(CY168295:0.001256,(CY183177:0.001878,CY170543:0.000625):0.000626):0.000623):0.0,(((CY170719:0.001249,KF789613:0.001249):0.0,KF886303:0.000624):0.0,((KF886305:0.000624,(KF199854:0.001249,CY169807:0.001249):0.0):0.0,((KF790378:0.000624,(CY170823:0.001249,(CY170879:0.000624,CY170591:0.000624):0.0):0.001875):0.0,KF789701:0.000624):0.0):0.0):0.0):0.0):0.0,((CY171119:0.0,CY171199:0.00125):0.000624,(((((CY171631:0.001249,CY171407:0.000624):0.0,CY171639:0.00125):0.0,CY171055:0.000624):0.0,CY171351:0.000625):0.0,((CY141252:0.001876,(CY171583:0.000625,CY171231:0.000624):0.0):0.0,KF789998:0.0):0.0):0.0):0.001249):0.000624):0.0):0.0):0.0,(((KF790167:0.0,KF789569:0.000624):0.000624,(KF789714:0.000623,(CY134812:0.0,CY141279:0.000625):0.0):0.000624):0.0,(KF886357:0.000625,(CY171335:0.000624,CY171071:0.0):0.001877):0.001252):0.0):0.0,CY186027:0.000624):0.000626)`
>Would you like to use it? Y


>Loaded a multiple sequence alignment with **121** sequences, **566** codons, and **1** partitions from `/home/sjspielman/book-chapter-2017/datasets/shallow.dat`
Yes

>Select the p-value used to for perform the test at (permissible range = [0,1], default value = 0.1): 0.1


### Branches to include in the FEL analysis
Selected 239 branches to include in FEL calculations: `KF790049, CY134956, CY183153, Node9, CY186123, CY186051, Node12, Node8, CY182809, CY148436, CY168583, Node21, CY170911, Node20, KF789547, Node19, Node17, CY186019, CY182889, CY135132, Node28, Node26, Node16, CY170799, CY149260, Node32, CY134686, CY168887, KF790064, Node38, Node36, CY169023, Node35, Node31, Node15, Node7, CY183049, KF789535, CY134740, Node48, KF790356, Node47, Node45, CY182737, CY168663, KF789752, Node58, Node56, CY186059, CY183193, Node61, Node55, CY141264, Node54, CY183113, Node53, CY183241, CY134828, KF199858, Node73, CY135124, CY134780, CY168871, Node78, Node76, Node72, CY135060, Node71, KF789614, Node70, Node68, CY183033, Node67, CY168599, CY168063, CY148364, CY148596, Node88, Node86, Node84, Node66, Node52, Node44, CY134844, Node43, CY182865, Node42, Node6, CY183185, Node5, CY186035, CY183081, Node99, CY135044, Node98, KF789780, Node97, CY182793, Node96, CY186235, CY134788, CY170479, KF790106, Node115, CY141230, Node114, CY149084, CY169199, Node119, Node113, KF789618, CY141176, Node122, Node112, KF790361, CY141213, CY170647, KF790316, CY169535, Node134, CY170967, Node133, CY169527, CY148348, Node138, Node132, CY168759, CY170767, Node141, Node131, Node129, Node127, Node125, Node111, CY141280, Node110, Node108, Node106, CY182777, Node105, Node95, KF790448, CY183225, CY134764, Node149, Node147, KF790345, CY182945, CY186075, Node158, KF790011, CY147297, Node161, Node157, KF886358, KF789871, Node164, Node156, Node154, KF790286, CY170991, CY171303, Node172, Node170, KF886340, CY147295, Node175, Node169, CY168295, CY183177, CY170543, Node180, Node178, Node168, CY170719, KF789613, Node185, KF886303, Node184, KF886305, KF199854, CY169807, Node192, Node190, KF790378, CY170823, CY170879, CY170591, Node200, Node198, Node196, KF789701, Node195, Node189, Node183, Node167, Node153, CY171119, CY171199, Node205, CY171631, CY171407, Node212, CY171639, Node211, CY171055, Node210, CY171351, Node209, CY141252, CY171583, CY171231, Node221, Node219, KF789998, Node218, Node208, Node204, Node152, Node146, Node94, Node4, KF790167, KF789569, Node227, KF789714, CY134812, CY141279, Node232, Node230, Node226, KF886357, CY171335, CY171071, Node237, Node235, Node225, Node3, CY186027`


### Obtaining branch lengths and nucleotide rates under the  GTR model
* Log(L) = -3884.95

### Obtaining the global omega estimate based on relative GTR branch lengths and nucleotide substitution biases
* Log(L) = -3784.11
* non-synonymous/synonymous rate ratio for *test* =   0.2432

### Improving branch lengths, nucleotide substitution biases, and global dN/dS ratios under a full codon model
* Log(L) = -3779.98
* non-synonymous/synonymous rate ratio =   0.2138

### For partition 1 these sites are significant at p <=0.1

|     Codon      |   Partition    |     alpha      |      beta      |      LRT       |Selection detected?|
|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:-----------------:|
|       12       |       1        |        6.848   |        0.000   |        3.265   |  Neg. p = 0.0708  |
|       16       |       1        |        5.016   |        0.000   |        2.836   |  Neg. p = 0.0922  |
|       21       |       1        |        4.367   |        0.000   |        2.862   |  Neg. p = 0.0907  |
|       88       |       1        |        4.367   |        0.000   |        2.862   |  Neg. p = 0.0907  |
|       32       |       1        |        5.435   |        0.000   |        4.546   |  Neg. p = 0.0330  |
|       46       |       1        |        5.529   |        0.000   |        3.561   |  Neg. p = 0.0592  |
|       48       |       1        |        5.875   |        0.000   |        3.250   |  Neg. p = 0.0714  |
|       49       |       1        |        0.000   |        7.617   |        3.321   |  Pos. p = 0.0684  |
|       54       |       1        |        6.839   |        0.000   |        3.187   |  Neg. p = 0.0742  |
|       61       |       1        |        6.864   |        0.000   |        3.192   |  Neg. p = 0.0740  |
|       70       |       1        |       13.952   |        0.000   |        7.193   |  Neg. p = 0.0073  |
|       77       |       1        |        4.468   |        0.000   |        2.896   |  Neg. p = 0.0888  |
|       80       |       1        |        6.853   |        0.000   |        3.266   |  Neg. p = 0.0707  |
|       84       |       1        |        6.949   |        0.000   |        3.482   |  Neg. p = 0.0620  |
|       94       |       1        |        4.177   |        0.000   |        2.897   |  Neg. p = 0.0887  |
|       99       |       1        |        5.744   |        0.000   |        2.886   |  Neg. p = 0.0894  |
|      101       |       1        |        5.883   |        0.000   |        3.252   |  Neg. p = 0.0713  |
|      106       |       1        |        6.709   |        0.000   |        3.442   |  Neg. p = 0.0636  |
|      107       |       1        |        5.947   |        0.000   |        3.381   |  Neg. p = 0.0660  |
|      152       |       1        |        6.912   |        0.000   |        3.591   |  Neg. p = 0.0581  |
|      165       |       1        |        6.861   |        0.000   |        3.578   |  Neg. p = 0.0585  |
|      181       |       1        |        5.874   |        0.000   |        2.994   |  Neg. p = 0.0836  |
|      182       |       1        |        5.445   |        0.000   |        3.696   |  Neg. p = 0.0546  |
|      187       |       1        |        6.787   |        0.000   |        3.177   |  Neg. p = 0.0747  |
|      198       |       1        |       10.109   |        0.000   |        5.353   |  Neg. p = 0.0207  |
|      199       |       1        |        5.874   |        0.000   |        2.875   |  Neg. p = 0.0900  |
|      202       |       1        |        5.001   |        0.000   |        3.178   |  Neg. p = 0.0747  |
|      212       |       1        |        4.993   |        0.000   |        2.829   |  Neg. p = 0.0926  |
|      232       |       1        |        7.126   |        0.000   |        3.253   |  Neg. p = 0.0713  |
|      234       |       1        |        4.310   |        0.000   |        2.844   |  Neg. p = 0.0917  |
|      236       |       1        |        4.903   |        0.000   |        2.951   |  Neg. p = 0.0858  |
|      241       |       1        |        0.000   |       10.631   |        2.760   |  Pos. p = 0.0967  |
|      272       |       1        |        5.016   |        0.000   |        3.182   |  Neg. p = 0.0744  |
|      304       |       1        |        6.255   |        0.000   |        2.813   |  Neg. p = 0.0935  |
|      331       |       1        |        5.610   |        0.000   |        2.850   |  Neg. p = 0.0913  |
|      338       |       1        |       19.791   |        0.000   |        9.384   |  Neg. p = 0.0022  |
|      349       |       1        |        8.385   |        0.000   |        5.798   |  Neg. p = 0.0160  |
|      353       |       1        |        5.026   |        0.000   |        3.185   |  Neg. p = 0.0743  |
|      396       |       1        |        6.508   |        0.000   |        4.193   |  Neg. p = 0.0406  |
|      431       |       1        |        6.046   |        0.000   |        3.296   |  Neg. p = 0.0695  |
|      440       |       1        |        5.887   |        0.000   |        2.997   |  Neg. p = 0.0834  |
|      446       |       1        |        8.479   |        0.000   |        5.168   |  Neg. p = 0.0230  |
|      454       |       1        |        6.857   |        0.000   |        3.461   |  Neg. p = 0.0628  |
|      489       |       1        |        6.857   |        0.000   |        3.268   |  Neg. p = 0.0707  |
|      493       |       1        |        5.876   |        0.000   |        2.935   |  Neg. p = 0.0867  |
|      509       |       1        |        6.905   |        0.000   |        3.472   |  Neg. p = 0.0624  |
|      514       |       1        |        5.879   |        0.000   |        2.995   |  Neg. p = 0.0835  |
|      515       |       1        |        4.613   |        0.000   |        3.314   |  Neg. p = 0.0687  |
|      540       |       1        |        6.861   |        0.000   |        3.269   |  Neg. p = 0.0706  |

### ** Found _2_ sites under pervasive positive diversifying and _47_ sites under negative selection at p <= 0.1**


Analysis Description
--------------------
MEME (Mixed Effects Model of Evolution) estimates a site-wise synonymous
(&alpha;) and a two-category mixture of non-synonymous (&beta;-, with
proportion p-, and &beta;+ with proportion [1-p-]) rates, and uses a
likelihood ratio test to determine if &beta;+ > &alpha; at a site. The
estimates aggregate information over a proportion of branches at a site,
so the signal is derived from episodic diversification, which is a
combination of strength of selection [effect size] and the proportion of
the tree affected. A subset of branches can be selected for testing as
well, in which case an additional (nuisance) parameter will be inferred
-- the non-synonymous rate on branches NOT selected for testing.
Multiple partitions within a NEXUS file are also supported for
recombination - aware analysis. 

- __Requirements__: in-frame codon alignment and a phylogenetic tree

- __Citation__: Detecting Individual Sites Subject to Episodic Diversifying Selection.
_PLoS Genet_ 8(7): e1002764.

- __Written by__: Sergei L. Kosakovsky Pond, Steven Weaver

- __Contact Information__: spond@temple.edu

- __Analysis Version__: 2.00


> A tree was found in the data file: `(KF790049:0.001255,((((((((CY134956:0.000624,CY183153:0.000624):0.0,(CY186123:0.000624,CY186051:0.000624):0.0):0.0,(((CY182809:0.000624,(((CY148436:0.0,CY168583:0.000624):0.0,CY170911:0.000624):0.0,KF789547:0.00125):0.000624):0.0,(CY186019:0.000625,(CY182889:0.000624,CY135132:0.0):0.00125):0.000624):0.0,((CY170799:0.001249,CY149260:0.000624):0.0,((CY134686:0.0,(CY168887:0.000625,KF790064:0.001249):0.0):0.000625,CY169023:0.000625):0.000624):0.0):0.0):0.0,((((CY183049:0.000624,((KF789535:0.001876,CY134740:0.000624):0.0,KF790356:0.000624):0.0):0.0,(((((CY182737:0.000624,(CY168663:0.001879,KF789752:0.001253):0.000623):0.0,(CY186059:0.000624,CY183193:0.001249):0.000625):0.0,CY141264:0.000624):0.0,CY183113:0.000624):0.0,(((CY183241:0.000624,((((CY134828:0.0,KF199858:0.000625):0.0,(CY135124:0.000624,(CY134780:0.000624,CY168871:0.001249):0.0):0.0):0.0,CY135060:0.000624):0.0,KF789614:0.000624):0.0):0.000624,CY183033:0.000626):0.0,(CY168599:0.001249,(CY168063:0.0,(CY148364:0.000624,CY148596:0.000624):0.0):0.0):0.001248):0.0):0.0):0.0,CY134844:0.0):0.0,CY182865:0.000624):0.0):0.0,CY183185:0.000624):0.0,((((((CY186035:0.001249,CY183081:0.000624):0.0,CY135044:0.000624):0.0,KF789780:0.0):0.0,CY182793:0.000624):0.000624,((CY186235:0.002501,(CY134788:0.0,((((((CY170479:0.001265,KF790106:0.0):0.000624,CY141230:0.000624):0.0,(CY149084:0.0,CY169199:0.001249):0.001249):0.0,(KF789618:0.000624,CY141176:0.00125):0.0):0.0,(KF790361:0.000624,(CY141213:0.000625,(CY170647:0.000624,((((KF790316:0.000625,CY169535:0.000624):0.000624,CY170967:0.000624):0.0,(CY169527:0.000624,CY148348:0.0):0.000624):0.0,(CY168759:0.000624,CY170767:0.0):0.0):0.0):0.000624):0.0):0.0):0.0,CY141280:0.000625):0.000624):0.000625):0.0,CY182777:0.000623):0.0):0.0,((KF790448:0.000624,(CY183225:0.000625,CY134764:0.0):0.0):0.000624,(((KF790345:0.000624,(((CY182945:0.000624,CY186075:0.0):0.0,(KF790011:0.0,CY147297:0.000624):0.001249):0.0,(KF886358:0.001249,KF789871:0.003135):0.0):0.0):0.000624,((((KF790286:0.001248,(CY170991:0.0,CY171303:0.000624):0.0):0.00125,(KF886340:0.001879,CY147295:0.000627):0.001255):0.0,(CY168295:0.001256,(CY183177:0.001878,CY170543:0.000625):0.000626):0.000623):0.0,(((CY170719:0.001249,KF789613:0.001249):0.0,KF886303:0.000624):0.0,((KF886305:0.000624,(KF199854:0.001249,CY169807:0.001249):0.0):0.0,((KF790378:0.000624,(CY170823:0.001249,(CY170879:0.000624,CY170591:0.000624):0.0):0.001875):0.0,KF789701:0.000624):0.0):0.0):0.0):0.0):0.0,((CY171119:0.0,CY171199:0.00125):0.000624,(((((CY171631:0.001249,CY171407:0.000624):0.0,CY171639:0.00125):0.0,CY171055:0.000624):0.0,CY171351:0.000625):0.0,((CY141252:0.001876,(CY171583:0.000625,CY171231:0.000624):0.0):0.0,KF789998:0.0):0.0):0.0):0.001249):0.000624):0.0):0.0):0.0,(((KF790167:0.0,KF789569:0.000624):0.000624,(KF789714:0.000623,(CY134812:0.0,CY141279:0.000625):0.0):0.000624):0.0,(KF886357:0.000625,(CY171335:0.000624,CY171071:0.0):0.001877):0.001252):0.0):0.0,CY186027:0.000624):0.000626)`
>Would you like to use it? Y


>Loaded a multiple sequence alignment with **121** sequences, **566** codons, and **1** partitions from `/home/sjspielman/book-chapter-2017/datasets/shallow.dat`

>Select the p-value used to for perform the test at (permissible range = [0,1], default value = 0.1): 0.1


### Branches to include in the MEME analysis
Selected 239 branches to include in the MEME analysis: `KF790049, CY134956, CY183153, Node9, CY186123, CY186051, Node12, Node8, CY182809, CY148436, CY168583, Node21, CY170911, Node20, KF789547, Node19, Node17, CY186019, CY182889, CY135132, Node28, Node26, Node16, CY170799, CY149260, Node32, CY134686, CY168887, KF790064, Node38, Node36, CY169023, Node35, Node31, Node15, Node7, CY183049, KF789535, CY134740, Node48, KF790356, Node47, Node45, CY182737, CY168663, KF789752, Node58, Node56, CY186059, CY183193, Node61, Node55, CY141264, Node54, CY183113, Node53, CY183241, CY134828, KF199858, Node73, CY135124, CY134780, CY168871, Node78, Node76, Node72, CY135060, Node71, KF789614, Node70, Node68, CY183033, Node67, CY168599, CY168063, CY148364, CY148596, Node88, Node86, Node84, Node66, Node52, Node44, CY134844, Node43, CY182865, Node42, Node6, CY183185, Node5, CY186035, CY183081, Node99, CY135044, Node98, KF789780, Node97, CY182793, Node96, CY186235, CY134788, CY170479, KF790106, Node115, CY141230, Node114, CY149084, CY169199, Node119, Node113, KF789618, CY141176, Node122, Node112, KF790361, CY141213, CY170647, KF790316, CY169535, Node134, CY170967, Node133, CY169527, CY148348, Node138, Node132, CY168759, CY170767, Node141, Node131, Node129, Node127, Node125, Node111, CY141280, Node110, Node108, Node106, CY182777, Node105, Node95, KF790448, CY183225, CY134764, Node149, Node147, KF790345, CY182945, CY186075, Node158, KF790011, CY147297, Node161, Node157, KF886358, KF789871, Node164, Node156, Node154, KF790286, CY170991, CY171303, Node172, Node170, KF886340, CY147295, Node175, Node169, CY168295, CY183177, CY170543, Node180, Node178, Node168, CY170719, KF789613, Node185, KF886303, Node184, KF886305, KF199854, CY169807, Node192, Node190, KF790378, CY170823, CY170879, CY170591, Node200, Node198, Node196, KF789701, Node195, Node189, Node183, Node167, Node153, CY171119, CY171199, Node205, CY171631, CY171407, Node212, CY171639, Node211, CY171055, Node210, CY171351, Node209, CY141252, CY171583, CY171231, Node221, Node219, KF789998, Node218, Node208, Node204, Node152, Node146, Node94, Node4, KF790167, KF789569, Node227, KF789714, CY134812, CY141279, Node232, Node230, Node226, KF886357, CY171335, CY171071, Node237, Node235, Node225, Node3, CY186027`


### Obtaining branch lengths and nucleotide rates under the  GTR model
* Log(L) = -3884.95

### Obtaining the global omega estimate based on relative GTR branch lengths and nucleotide substitution biases
* Log(L) = -3784.11
* non-synonymous/synonymous rate ratio for *test* =   0.2432

### Improving branch lengths, nucleotide substitution biases, and global dN/dS ratios under a full codon model
* Log(L) = -3779.98
* non-synonymous/synonymous rate ratio =   0.2136

### For partition 1 these sites are significant at p <=0.1

|   Codon    | Partition  |   alpha    |   beta+    |     p+     |    LRT     |Episodic selection detected?| # branches |
|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:--------------------------:|:----------:|
|     49     |     1      |    0.000   |  167.379   |    0.065   |    3.580   |      Yes, p =  0.0787      |     0      |
|    320     |     1      |    0.000   |  437.674   |    0.010   |    3.230   |      Yes, p =  0.0946      |     0      |

### ** Found _2_ sites under episodic diversifying positive selection at p <= 0.1**

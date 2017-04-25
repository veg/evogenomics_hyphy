# Inference Results

## BUSTED

We have several suitable datasets for demonstrating how BUSTED can pick up (whole-tree) signal of selection when *no sites* (as analyzed with FEL, aBSREL, MEME) are under selection. Datasets are primate-only alignment subsets (9 taxa) from Enard and Petrov's eLife paper. The following table shows results for genes with the most biological information:


ensembl | gene | BUSTED Pvalue | notes
--- | --- | --- | ---
ENSG00000088682|COQ9|0.000606636|apparently mitochondrial?????
ENSG00000075426|FOSL2|0.000954833|fos-related antigen2| regulates cell proliferation/differentiation/transformation
ENSG00000120129|DUSP1|0.00125078|dual-specificity phospatase. inactivates MAP. cellular response to environmental stress.
ENSG00000171435|KSR2|0.001480504|kinase suppressor of ras2. reduces glucose and fatty acid oxidation| involved in type2 diabetes
ENSG00000145354|CISD2|0.001764008|zinc finger protein in ER. defects cause Wolfram syndrome2| possible Ca homeostasis involvement
ENSG00000171132|PRKCE|0.002772339|protein kinase C epsilon-type| does a whole bunch of things in cardiac muscle 
ENSG00000123388|HOXC11|0.003743968|hox gene possibly in early intestinal development
ENSG00000070831|CDC42|0.004019145|cell division controlling protein 42 homolog; GTPase in the Rho family  
ENSG00000164463|CREBRF|0.006074875|missense variant makes Samoans overweight says a GWAS: [http://www.nature.com/ng/journal/v48/n9/full/ng.3620.html](http://www.nature.com/ng/journal/v48/n9/full/ng.3620.html)
ENSG00000104164|BLOC1S6|0.007925127|biogenesis of lysosomal organelles complex 1 subunit 6; intracellular vesicle trafficking. mutations cause disease.
ENSG00000166689|PLEKHA7|0.008631871|adherins junction protein and even has a full wikipedia page


## aBSREL

Still cannot find a dataset with a reasonable distinction between exploratory and a priori hypothesis. My best option so far has been rcbL, but only 3-5 random branches with no clear pattern (certainly not C4) emerged as selected, and BUSTED showed no strong evidence of selection on C4 foreground (P=0.09).

## RELAX

Identified a dataset of influenza pb2 sequences (very commonly used in mutsel papers, so there are results to compare with although a bit apples-to-oranges) with sequences from human and avian hosts. Human host sequences form a single clade. The original dataset contains 401 sequences (80 human and 321 avian) which I subsetted to 60 sequences (20 humans and 40 avian) for runtime. When human sequences specified as test branches, k=0.702 with P=
http://test.datamonkey.org/relax/58ff5df00928c6440e403952

## FUBAR/FEL/SLAC/MEME

Used the H3N2 HA dataset from [https://doi.org/10.1371/journal.ppat.1004940](https://doi.org/10.1371/journal.ppat.1004940). The original dataset size was 3854 sequences. To subset, a few visually-identified outliers were removed as well as any sequence with a gap or ambiguities, resulting in a subsetted dataset of 2555 sequences ("full"). This was further subset into trunk and shallow lineage datasets:

dataset | N | tree length
--- | --- | ---
full | 2555 | 3.68
trunk | 163 | 0.43
shallow | 121 | 0.116

Selection results (at P<0.1) for these datasets are as follows.

### Full H3N2

**Bold sites shared with trunk**, and *emph sites shared with shallow*

+ **FUBAR**: *19*, 47, **61**, **69**, **154**, 156, 173, *241*, 277, 278, 292


Italicized sites appear in more than 1 method:

### Trunk H3N2

+ **FUBAR**: *61*, *69*, 154, *208*, *242*
+ **FEL**: *61*, 64, *69*, 137, *208*
+ **SLAC**: 154, 208
+ **MEME**: *61*, 64, 154, 171, *208*, 209, *242*, 372, 402 

### Shallow H3N2

+ **FUBAR**: *19*, *49*, *241*
+ **FEL**: (*19* has P=0.11), *49*, *241*
+ **SLAC**: None
+ **MEME**: *49*, *241* 320 




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

Error:
Could not find source dataset file "PROMPT_FOR_FILE" (resolved to '/home/sjspielman/hyphy/res/TemplateBatchFiles/SelectionAnalyses/All')
Path stack:
	/home/sjspielman/hyphy/res/
	/home/sjspielman/hyphy/res/TemplateBatchFiles/SelectionAnalyses/

Function call stack
1 : Read Data Set ^dataset_name from file PROMPT_FOR_FILE
	Standard input redirect:
		000000000004 : Yes
		000000000005 : 0.1
		-------
2 : code_info=alignments.LoadGeneticCode(None)
	Standard input redirect:
		000000000004 : Yes
		000000000005 : 0.1
		-------
3 : A return statement with:1
	Standard input redirect:
		000000000004 : Yes
		000000000005 : 0.1
		-------
4 : A return statement with:1
	Standard input redirect:
		000000000004 : Yes
		000000000005 : 0.1
		-------
5 : codon_data_info=alignments.PromptForGeneticCodeAndAlignment(prefix+".codon_data",prefix+".codon_filter")
	Standard input redirect:
		000000000004 : Yes
		000000000005 : 0.1
		-------
6 : load_file("fel")
	Standard input redirect:
		000000000004 : Yes
		000000000005 : 0.1
		-------
7 : Call a nested list (via namespace):
 

Step 0.LoadFunctionLibrary from file"modules/shared-load-file.bf" using basepath /home/sjspielman/hyphy/res/TemplateBatchFiles/SelectionAnalyses/.

Step 1.load_file("fel")
	Standard input redirect:
		000000000004 : Yes
		000000000005 : 0.1
		-------

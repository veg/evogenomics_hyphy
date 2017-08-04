## Tips for HyPhy usage
> To be placed at end of book chapter, per editors' request.



1. There are generally three ways to provide HyPhy with data.
	+ A nexus file. HyPhy will issue a single prompt for data.
	+ An FASTA-formatted alignment file with a newick tree string at the bottom of the file. HyPhy will issue a prompt asking to accept the tree found in the provided alignment file.
	+ Separate alignment and newick tree files. HyPhy will issue a prompt asking for the path to file w/ tree.

2. JSONs can be parsed easily in Python (`json` package) and R (`jsonlite` package). This [webpage](link-tbd) defines all fields in the output.

3. Please use [Issues](github.com/veg/hyphy/issues) with questions on HyPhy usage.

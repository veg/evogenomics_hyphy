"""
   Subset the H3 alignment from https://doi.org/10.1371/journal.ppat.1004940 and construct a new phylogeny using FastTree.
   Alignment is subsetted by:
    1) Removing certain IDs which were visually identified as strong outliers (excessively long branches)
    2) Removing any partial sequences (i.e. any with gaps)    
"""
from Bio import AlignIO
import subprocess

original_aln = "original_h3n2_ha.aln" ## Alignment from https://doi.org/10.1371/journal.ppat.1004940

prefix = "h3n2_ha_subset"
outaln = prefix + ".aln"
outtree = prefix + ".tre"

## Visually identified outlying sequences.
outliers = ["KF805696", "GU937743", "JN866186", "JX905414", "JQ070776", "JX905419", "JN992750", "JQ070792", "JQ290164"]

aln = AlignIO.read(original_aln, 'fasta')

have = []
with open(outaln, "w") as f:
    for entry in aln:
        s = str(entry.seq)
        if s.count("-") == 0 and entry.id not in outliers:
            if s in have:
                continue
            else:
                have.append(s)
                f.write(">" + entry.id + "\n" + s + "\n")
#print "KEEPING", len(have)
cmd = "FastTree -nt -gtr -nosupport " + outaln + " > " + outtree
build_tree = subprocess.call(cmd, shell=True)
assert(build_tree == 0), "FastTree failed to run"
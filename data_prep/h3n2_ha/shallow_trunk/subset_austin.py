from Bio import AlignIO
import subprocess

original_aln = "austin_h3n2_ha.aln"

prefix = "h3n2_ha_subset"
outaln = prefix + ".aln"
outtree = prefix + ".tre"

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
print "KEEPING", len(have)
cmd = "FastTree -nt -gtr -nosupport " + outaln + " > " + outtree
subprocess.call(cmd, shell=True)

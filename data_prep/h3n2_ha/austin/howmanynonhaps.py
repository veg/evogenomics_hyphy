from Bio import AlignIO
aln = AlignIO.read('austin_h3n2_ha.aln', 'fasta')

g = 0
x = 0
for entry in aln:
    s = str(entry.seq)
    if s.count("-") <= g:
        x+=1
print x 
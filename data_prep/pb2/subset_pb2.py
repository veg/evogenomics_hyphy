from Bio import AlignIO
import numpy as np

a = AlignIO.read("pb2.fasta", "fasta") ## 80 human and 320 avian. somehow we lost an avian..?

nAv = 40
nHu = 20

human = {}
avian = {}
for record in a:
    if record.id.startswith("Hu_"):
        human[record.id] = str(record.seq) 
    elif record.id.startswith("Av_"):
        avian[record.id] = str(record.seq) 

final = {}
human_random = np.random.choice(range(0, len(human)), size=nHu, replace=False)
avian_random = np.random.choice(range(0, len(avian)), size=nAv, replace=False)

with open("pb2_subset.fasta", "w") as f:
    x = 0
    for entry in human:
        if x in human_random:
            f.write(">" + entry + "\n" + human[entry] + "\n")
        x+=1
        
    x = 0
    for entry in avian:
        if x in avian_random:
            print "Av"
            f.write(">" + entry + "\n" + avian[entry] + "\n")
        x+=1
        
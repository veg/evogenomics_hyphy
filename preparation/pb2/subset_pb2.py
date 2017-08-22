from Bio import AlignIO
import numpy as np
#import dendropy ## Dendropy is being exceedingly difficult so pruning will be done in R w/ ape library

nav = 20
nhu = 15


aln = AlignIO.read("tamuriPB2.phy", "phylip-relaxed")


avian = []
human = []
for i in range(len(aln)):
    isavian = str(aln[i].id).startswith("Av_")
    if isavian:
        avian.append(i)
    else:
        human.append(i)

keepav = list(np.random.choice(avian, size=nav, replace=False))
keephu = list(np.random.choice(human, size=nhu, replace=False))


keep = keepav + keephu
chucked_ids = []

with open("pb2_small.dat", "w") as f:
    for i in range(len(aln)):
        if i in keep:
            f.write(">" + str(aln[i].id) + "\n" + str(aln[i].seq) + "\n")
        else:
            chucked_ids.append(str(aln[i].id))


print chucked_ids

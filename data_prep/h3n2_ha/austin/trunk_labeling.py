'''
basic idea:
    1. given a certain tree topology in Newick format, find the innermost parenthesis or parentheses
    2. if parenthesis:
        random choose one leave as trunk
        going out one level, label the parenthesis containing the trunk as trunk 
        repeat last step util reach the outmost parenthesis
      if parentheses:
        random choose one parenthesis and follow the steps for "if parenthesis"
'''  
import random
import sys

filename = sys.argv[1]
outfile  = sysa.argv[2]

t = open(filename, 'r')
tstring = t.read()
t.close()
length = len(tstring)
deepest = 0 
deepth = 0
count = 0
comma_position = 0
deepth_index ={}        #storre the index of right parenthesis (and comma on its left) with deepest level so far
for i in xrange(length):
    if tstring[i]==",":
        comma_position = i
    if tstring[i]=="(":
        count +=1                  #count the level of trees 
    if tstring[i]==")":
        deepth = count 
        count -= 1
        if deepth == deepest:
            deepth_index[deepest].append((comma_position,i))
        if deepth > deepest:
            deepest = deepth 
            deepth_index.clear()
            deepth_index[deepest]=[(comma_position,i)]

trunk_node = random.choice(deepth_index.values()[0])    #random choose a deepest NODE and return its index
labeled_tree = tstring[:trunk_node[0]] + "_trunk_" + tstring[trunk_node[0]:trunk_node[1]] + "_trunk_" + tstring[trunk_node[1]:]

new_len= len(labeled_tree)
j = trunk_node[1]+16 # the fuck is this magic horseshit
deepth = deepest
while j<new_len:
    if labeled_tree[j] == "(":
        deepth +=1            
    elif labeled_tree[j] == ")":
        deepth -=1
        if deepth < deepest:
            deepest -=1
            labeled_tree = labeled_tree[:j] + "_trunk_" + labeled_tree[j:]
            new_len= len(labeled_tree)
            j+=7
    j += 1

output = open(outfile, "w")
output.write(labeled_tree)
output.close()
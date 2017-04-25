import dendropy
from Bio import AlignIO

def parse():
        
        
        
        
        
(tree, flags, internalNode_count, index) = _parse_tree(tstring, flags, internalNode_count, scale_tree, 0) 





tree = dendropy.Tree.get(
    path='labeled_trunk.tre',
    schema='newick',
    preserve_underscores=True)

retain = []
for node in tree.preorder_node_iter():
    if node.label == "TRUNK":
        for child in node._child_nodes:
            if child.taxon is not None:
                retain.append(child.taxon) #### This is always going to be 80. If we need more taxa, can randomly select other ones to add in.

tree.retain_taxa(retain)
tree.write(
     path="austin_h3n2_ha_TRUNK.tre",
    schema="newick")

with open("austin_h3n2_ha.aln", "r") as f:
    aln = AlignIO.read(f, "fasta")
    
retainstr = [str(x).replace("'","") for x in retain]
with open("austin_h3n2_ha_TRUNK.aln", "w") as f:
    for rec in aln:
        if rec.id in retainstr:
            f.write(">" + rec.id  + "\n" + str(rec.seq) + "\n")

    

 

# trunk_namespace = [str(x) for x in tree.taxon_namespace if "TRUNK" in str(x)]
# print trunk_namespace
#tree.retain_taxa_with_labels(trunk_namespace)
#tree.write(
#    path="trunk.tre",
#    schema="newick",
#    )

#print tree.taxon_namespace
#print type(tree.taxon_namespace)
#print trunk_namespace

# retain = []
# for node in tree.postorder_node_iter():
#     if "TRUNK" in node.taxon:
#         retain.append(, node.taxon
# 


#         for child in nd._child_nodes:
#             if node_desc_counts[child] > maxChildren:
#                 whichChild = child
#                 maxChildren = node_desc_counts[child]
#         trunks.append(whichChild)
# print len(trunks)



# 
# tree = dendropy.Tree.get(
#     path='raw.tre',
#     schema='newick',
#     preserve_underscores=True)
#     
# target_node = "trunk_end"
# 
# for node in tree.postorder_node_iter():
#     if:
#         node.label == target_node:
#             node.trunk = True
#     else:
#         for child in node._child_nodes:
#             

# 
#     // **********************************************************
#     // now do the branch/trunk analysis.
#     // Hyphy doesn't allow us to factor this into a function,
#     // so here it comes in all its messiness.
#     
#     treeAVL = site_tree^0;
#     
#     n = Abs(treeAVL); // # total number of nodes in the tree
#     for (i=1; i<n; i=i+1)
#     {
#         node_name = (treeAVL[i])["Name"];
#         // are we at the target node?
#         if (node_name == target_node)
#         {
#             (treeAVL[i])["Trunk"] = 1;
#         }
#         else // no, but maybe we're ancestral to the target node?
#         {
#             children = Abs((treeAVL[i])["Children"]);
#             for (j=0; j<children; j=j+1)
#             {
#                 child_index = ((treeAVL[i])["Children"])[j];
#                 if ((treeAVL[child_index])["Trunk"])
#                 {
#                       (treeAVL[i])["Trunk"] = 1;
#                       break; // if we find one appropriate child we're done
#                 }
#             }
#         }
#         // if i is a trunk node, set appropriate constraint
#         if ((treeAVL[i])["Trunk"])
#         {
#             execString = "ClearConstraints(site_tree."+node_name+".w)";
#             ExecuteCommands(execString);
#             ReplicateConstraint("this1."+node_name+".w:=w_trunk", site_tree);
#         }
#     }
#     
#     // end placing constraints on trunk
#     // **********************************************************

# dt=1
# 
# # Find most recent tip
# most_recent_date = -1e10
# for node in tree.leaf_iter():
# 	if node.num_date>most_recent_date:
# 		most_recent_date=node.num_date
# for node in tree.postorder_node_iter():
# 	node.trunk_count=0		
# 
# # Mark ancestry of recent tips
# number_recent = 0
# for node in tree.leaf_iter():
# 	if most_recent_date -  node.num_date<dt:
# 		number_recent += 1
# 		parent = node.parent_node
# 		while (parent != None):
# 			parent.trunk_count += 1
# 			parent = parent.parent_node
# 
# # Mark trunk nodes
# for node in tree.postorder_node_iter():
# 	if node.trunk_count == number_recent:
# 		node.trunk = True
# 	else:
# 		node.trunk = False
# 
# 
# for node in tree.postorder_node_iter():
# 	print node.name, node.trunk
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 










##### Ladderize source code
#        Sorts child nodes in ascending (if ``ascending`` is |False|) or
#        descending (if ``ascending`` is |False|) order in terms of the number of
#        children each child node has.node_desc_counts = {}
# node_desc_counts = {}
# ascending = False
# for nd in tree.postorder_node_iter():
#     if len(nd._child_nodes) == 0:
#         node_desc_counts[nd] = 0
#     else:
#         total = 0
#         for child in nd._child_nodes:
#             total += node_desc_counts[child]
#         total += len(nd._child_nodes)
#         node_desc_counts[nd] = total
#         nd._child_nodes.sort(key=lambda n: node_desc_counts[n], reverse=not ascending)
# 

# tree.ladderize(ascending=False)
# 
# trunks = []
# for nd in tree.postorder_node_iter():
#     if len(nd._child_nodes) > 0:
#         maxChildren = 0
#         whichChild = None
#         for child in nd._child_nodes:
#             if node_desc_counts[child] > maxChildren:
#                 whichChild = child
#                 maxChildren = node_desc_counts[child]
#         trunks.append(whichChild)
# print len(trunks)
# 
# trunks = []
# for nd in tree.postorder_node_iter():
#     if len(nd._child_nodes) > 0:
#         maxChildren = 0
#         whichChild = None
#         for child in nd._child_nodes:
#             if node_desc_counts[child] > maxChildren:
#                 whichChild = child
#                 maxChildren = node_desc_counts[child]
#         trunks.append(whichChild)
# print len(trunks)
# 
# 






#for nd in tree.postorder_node_iter():
#    if len(nd._child_nodes) == 0:
#        nd.label = "trunk"
#    else:
#        for child in nd._child_nodes:
#            if child in trunks: 
#                child.label = "trunk"
#            else:
#                child.label = "nontrunk"


#tree.write(
#     path="updated_austin.tre",
#    schema="newick")

#print len(trunks)
#print x
#print(tree.as_string(schema='newick'))

#tree.ladderize(ascending = False)
#print(tree)
# 
# for node in tree.preorder_node_iter():
#     if node.taxon is None:
#         node.label = "internal"
#     else:
#         node.label = "tip"
# 
# for node in tree.preorder_node_iter():
#     
#     for child in node.child_nodes():
#         if child.label
#         
#     print node.taxon, node.label
# 
# 
# 

########################
## SJS. Plot tips colored by analysis classification. Output in "treeplot.R".
########################


require(tidyverse)
require(ape)
require(ggtree)

full.tree <- ape::read.tree("h3n2_ha_subset.tre")
trunk.tree <- ape::read.tree("trunk.tre")
shallow.tree <- ape::read.tree("shallow.tre")

tip.frame <- tibble("tip" = character(), "value" = integer())
for (tip in full.tree$tip.label){
    value <- -1
    ## 3 is shallow and trunk
    if (tip %in% trunk.tree$tip.label & tip %in% shallow.tree$tip.label){
        value <- 3
    }
    ### 2 is trunk only
    if (tip %in% trunk.tree$tip.label & !(tip %in% shallow.tree$tip.label)){
        value <- 2
    }
    ### 1 is shallow only
    if (!(tip %in% trunk.tree$tip.label) & tip %in% shallow.tree$tip.label){
        value <- 1
    }
    ### 0 is full only
    if (!(tip %in% trunk.tree$tip.label) & !(tip %in% shallow.tree$tip.label)){
        value <- 0
    }
    if (value == -1){
        stop("can't place the tip")
    }
    temp <- tibble("tip" = tip, "value" = value)
    tip.frame <- rbind(tip.frame, temp)
}
tip.frame$value <- as.factor(tip.frame$value)

### 0,1,2,3 --> full,shallow,trunk,shallow+trunk
all.colors <- c(rgb(0, 0, 0, 0.2), "deepskyblue", "firebrick1", "darkorchid1")


tree.plot <- ggtree(full.tree, size = 0.3) %<+% tip.frame + geom_tippoint(aes(color = value), size=1) + scale_color_manual(values=all.colors, name = "",labels=c("Full", "Shallow", "Trunk", "Shallow and trunk")) + geom_treescale(x=0.01, y=-1, fontsize=3, offset=-50) + theme(legend.position = "right", legend.text = element_text(size=9)) + guides(color = guide_legend(override.aes = list(size=1.75))) 
ggsave("treeplot.pdf", tree.plot, height=4, width=7)




#+ scale_shape_manual(values=c(1,16,16,16,16),name = "",labels=c("Full", "Shallow", "Trunk", "Shallow and trunk"))



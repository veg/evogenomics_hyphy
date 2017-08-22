import json
import re


def makeoutline(type, site, col, threshold):
    a = float(col[0])
    b = float(col[1])
    p = float(col[4])
    outline = type + "," + site 
    if p <= threshold:
        if b > a:
            outline += ",P," + str(p) + "\n"
        else:
            outline += ",N," + str(p) + "\n"
    else:
        outline += ",none," + str(p) + "\n"
    
    return outline
        
        
threshold =0.1

nods_json = "../results/CD2-ds1.dat.FEL.json"
ds_json   = "../results/CD2-dsvar.dat.FEL.json"

with open(nods_json, "r") as f:
    nods = json.load(f)
    
with open(ds_json, "r") as f:
    dsvar = json.load(f)
    
nods_columns = nods["MLE"]["content"]["0"]
dsvar_columns = dsvar["MLE"]["content"]["0"]
assert(len(nods_columns) == len(dsvar_columns)), "diff numbers of sites in jsons"

output = "type,site,selection,p\n" ## site, selection, p
## 0: alpha, 1: beta, 4: p
for i in range(len(nods_columns)):
    outline = ""
    
    c1 = nods_columns[i]
    c2 = dsvar_columns[i]
    
    outline1 = makeoutline("ds1", str(i+1), c1, threshold)
    outline2 = makeoutline("dsvar", str(i+1), c2, threshold)
    
    if "none" in outline1 and "none" in outline2:
        outline1 = "ds1," +str(i+1) + ",none,0\n"
        outline2 = "dsvar," +str(i+1) + ",none,0\n"
    output += outline1 + outline2
    
with open("cd2_compare.csv", "w") as f:
    f.write(output)


""" R code:

library(tidyverse)
require(grid)

dat.raw <- read_csv("cd2_compare.csv")
dat.raw %>% 
    mutate(yend = ifelse(type == "ds1", -0.06, 0.06)) %>%
    mutate(y = ifelse(type == "ds1", -0.01, 0.01)) %>%
    filter(selection != "none")  -> dat
dat$selection <- factor(dat$selection, levels=c("P", "N")) #, "none"))

dat %>% 
    select(-p, -y, -yend) %>% 
    spread(type, selection) %>% 
    filter(is.na(ds1), dsvar == "P") %>%
    select(site) -> dsvarpos.sites
dat %>% 
    select(-p, -y, -yend) %>% 
    spread(type, selection) %>% 
    filter(is.na(ds1), dsvar == "N") %>%
    select(site) -> dsvarneg.sites
    

############# below unusued. ###############
# 
# 
# 
# 
# ggplot(dat, aes(x = site, xend=site, y =y , yend=yend, color = selection)) + 
#     geom_segment() + 
#     scale_color_manual(values=c("red", "dodgerblue2"), name = "Selection", labels=c("Positive", "Negative")) +
#     scale_y_continuous(limits=c(-0.1, 0.1)) + 
#     theme(legend.position="none", axis.title=element_blank(), axis.text=element_blank(),axis.ticks=element_blank()) + 
#         geom_hline(yintercept=0)   ->pline
#     
# ggsave("cd2_siteline_compare_RAW.pdf", pline, width=7, height=2)
# 
# 
#     
# 
# 
# 
# 
# 
# 
# dat.raw %>% mutate(shrunkp = ifelse(p>=0.2, 0.2, p)) -> dat
# 
# ## Sites which are positively selected in ds variation inference but NOT significant in ds=1 inference
# dat %>% filter(type == "ds1") -> ds1.dat
# 
# dat %>% 
#     select(-p, -shrunkp) %>% 
#     spread(type, selection) %>% 
#     filter(ds1 == "none", dsvar == "P") %>% 
#     left_join(ds1.dat) %>%
#     select(site, shrunkp) %>%
#     mutate(shrunkp_y = shrunkp+0.01) -> dsvarpos.sites
# dat %>% 
#     select(-p, -shrunkp) %>% 
#     spread(type, selection) %>% 
#     filter(ds1 == "none", dsvar == "N") %>% 
#     left_join(ds1.dat) %>%
#     select(site, shrunkp) %>%
#     mutate(shrunkp_y = shrunkp+0.01) -> dsvarneg.sites
#     
# dat$selection <- factor(dat$selection, levels=c("P", "N", "none"))
# ggplot(NULL) + 
#     geom_bar(data=dat, aes(x = site, y = shrunkp, fill=selection, group=type), stat="identity", position="dodge") + 
#     scale_fill_manual(name = "Selection", labels = c("Positive", "Negative", "No evidence"), values=c("red", "dodgerblue", "grey80")) + 
#     geom_hline(yintercept=0.1, size=0.2) + 
#     xlab("Site") + ylab("P-value") + 
#     theme_classic() +  
#     theme(legend.key.size = unit(0.3, "cm"), legend.title = element_text(size=9), legend.text = element_text(size=8)) +
#     scale_x_continuous(expand = c(0,0)) + scale_y_continuous(expand=c(0,0)) + coord_cartesian(ylim=c(0, 0.22)) + 
#     geom_point(data = dsvarpos.sites, aes(x = site, y=shrunkp_y), shape = "*", size=3, color="red") +
#     geom_point(data = dsvarneg.sites, aes(x = site, y=shrunkp_y), shape = "*", size=3, color="dodgerblue")
# 
#     
#     -> pbar
# ggsave("cd2_pvalue_compare_RAW.pdf", pbar, width=7, height=2)

"""









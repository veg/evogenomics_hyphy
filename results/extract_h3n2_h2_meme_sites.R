library(tidyverse)
dat <- read_csv("h3n2_ha_subset.dat.meme.csv")
dat %>% 
    mutate(site = 1:n()) %>% 
    filter(p<=0.05,beta_plus>1) %>% 
    select(site)
# 
# 
# # A tibble: 14 × 1
#     site
#    <int>
# 1     19
# 2     47
# 3     69
# 4    110
# 5    151
# 6    154
# 7    156
# 8    173
# 9    208
# 10   236
# 11   241
# 12   278
# 13   292
# 14   538
# 

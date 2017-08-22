
============================= FUBAR v1.0 ============================

This file will perform a Fast Unbiased AppRoximate Bayesian (FUBAR)
analysis of a coding sequence alignment to determine whether some
sites have been subject to pervasive purifying or diversifying
selection. For details of the method and explanations of various
settings, please see http://www.hyphy.org/wiki/FUBAR

Please note that a FUBAR analysis generates many files in the same
directory as the original alignment. HyPhy needs to have write
privileges to this directory. For example if the original file is in
/home/sergei/FUBAR/data/pol.nex then at the end of a FUBAR run, there
will also exist files such as /home/sergei/FUBAR/data/pol.nex.samples,
/home/sergei/FUBAR/data/pol.nex.gridInfo etc. Many of these files can
be further examined for diagnostic and other purposes. They also
provide checkpointing so that a partially completed analysis can be
restarted.

=====================================================================

How many datafiles are to be analyzed (>=1):?1

Reading input file 1/1

163 species:{KF789585, CY025485, KC535396, CY039880, CY112957, CY017283, CY010628, KC882883, CY010716, CY001792, CY172847, CY001504, CY134876, CY039879, KC892266, CY011560, KF789591, KC882867, CY012728, CY013669, CY002048, CY010516, CY026019, CY002304, CY173095, CY173255, CY171039, CY012456, CY090885, KC892156, CY012200, CY011824, CY172823, GQ385889, CY007979, KJ667974, CY006163, KF790037, CY112605, CY020069, KF790414, CY172903, CY183065, CY172839, GQ385891, CY168407, FJ179356, FJ179354, KF551075, EU779522, CY173191, CY141224, KC892174, CY001920, KF790408, CY168471, CY011328, CY002080, CY036847, CY010036, KF790438, CY147305, CY147300, CY092217, CY012896, CY134996, KF685747, CY006060, CY141202, KC882488, CY001600, CY010028, CY013200, CY009732, AB434109, CY006899, KC535387, KC535363, KF790049, JX978746, CY010012, CY112556, KF886352, CY003632, CY001744, KC535378, KC892685, KC535375, KC892519, CY006579, CY114309, KF598733, CY006283, CY002456, KC893110, KC892407, CY000721, CY011848, CY168239, CY010004, CY172191, KC892889, CY025341, CY088198, CY169303, CY012512, CY026251, CY012184, EU516019, CY002368, CY009484, CY035062, KC893018, KF790384, KF790389, EU199255, CY134956, KC535402, KF790010, CY114493, CY037727, KC892641, CY114509, CY011888, CY092241, CY172223, CY027075, CY010020, KF761507, CY006859, CY002136, CY012760, CY011416, KC892498, JX913043, CY172431, CY011896, CY112669, KJ938675, CY114221, CY088475, CY183153, CY112901, CY000257, CY013701, KC892480, CY037703, CY172775, FJ686933, GQ385846, CY006635, CY001912, CY044748, KF790403, CY013693, CY002064, CY006499, CY012224, CY006491, CY025643, KC526205, CY012232, EU199367};
Total Sites:1698;
Distinct Sites:399

A tree was found in the data file:
((KF790010:0.001247,CY147300:0.000623):0.0,((CY168239:0.001872,(CY171039:0.001874,KF790389:0.000623):0.000624):0.0,((CY141224:0.001247,(CY147305:0.0,KF790037:0.000623):0.000623):0.0,(((KF790403:0.000623,KF761507:0.001876):0.0,KC526205:0.000623):0.0,((CY169303:0.0,(KF789585:0.000623,CY141202:0.000623):0.000623):0.000623,(((KJ667974:0.002501,KJ938675:0.001873):0.000623,CY134876:0.0):0.000623,((KF790414:0.001248,(KF790384:0.001245,KF790408:0.00125):0.0):0.0,((KF886352:0.001882,(KF790438:0.000623,CY134996:0.001873):0.000623):0.001875,(KF789591:0.001879,((KF790049:0.001255,(CY134956:0.000624,CY183153:0.000624):0.000626):0.001249,((CY168407:0.004394,CY183065:0.003128):0.0,(KF598733:0.002501,((KC892174:0.0,(KF685747:0.000624,CY168471:0.000625):0.00375):0.000624,(((KC892685:0.000624,KC892641:0.0):0.001874,KC893110:0.001249):0.0,(KC892480:0.0,(JX913043:0.001249,(KF551075:0.00125,((CY114509:0.0,(KC892889:0.0,KC893018:0.002498):0.005006):0.001877,(((KC892519:0.0,KC892498:0.000624):0.002497,KC892266:0.000623):0.001026,((KC892156:0.003756,(JX978746:0.001256,KC892407:0.001883):0.001875):0.00355,((KC535402:0.000623,(KC882488:0.002498,KC535387:0.001247):0.001872):0.0,(KC535363:0.000623,((KC535396:0.000623,(KC882883:0.0,KC882867:0.000623):0.003124):0.0,((KC535378:0.001872,KC535375:0.002498):0.0,(GQ385891:0.001248,((EU779522:0.001251,(CY037727:0.0,FJ179354:0.003124):0.0):0.000623,((GQ385889:0.005007,(FJ686933:0.001243,FJ179356:0.003117):0.0):0.000622,(CY173095:0.001245,(((CY173191:0.0,CY037703:0.001247):0.000622,CY035062:0.00249):0.0,((CY173255:0.001871,(CY044748:0.0,GQ385846:0.001247):0.000623):0.0,((CY027075:0.000623,(EU199367:0.0,CY172823:0.000623):0.0):0.000623,(((CY172847:0.000623,CY025643:0.0):0.000623,CY172839:0.000623):0.001247,(((CY026251:0.002497,CY092241:0.00125):0.000624,CY026019:0.000623):0.0,((CY025341:0.002502,(CY172775:0.001247,CY172903:0.000623):0.001248):0.000622,(EU199255:0.003134,(CY172431:0.000621,((CY172223:0.003127,(CY172191:0.001254,CY020069:0.000628):0.000621):0.0,((CY092217:0.003119,(CY025485:0.001283,EU516019:0.00059):0.008843):0.001868,(CY002080:0.000622,((CY002064:0.001873,(CY002456:0.000626,CY002048:0.002491):0.001243):0.003763,(AB434109:0.006307,(((CY088198:0.001245,CY088475:0.000621):0.0,CY000257:0.000621):0.002494,((CY112957:0.003135,CY006859:0.001253):0.000616,((CY000721:0.001243,(CY114493:0.0,CY090885:0.002483):0.002488):0.0,((CY001792:0.000621,(CY001600:0.00062,CY002368:0.001865):0.0):0.0,((CY002304:0.002489,(CY006163:0.001242,CY003632:0.00062):0.0):0.00062,(CY001920:0.003739,(CY001912:0.002498,((CY001504:0.0,CY006060:0.001241):0.00062,((CY001744:0.0,CY002136:0.00124):0.00062,((CY114309:0.003746,(CY006899:0.001874,CY112901:0.001863):0.002496):0.000618,(((CY006579:0.001245,CY006283:0.000621):0.001244,CY007979:0.001864):0.0,((CY006499:0.001241,(CY006491:0.001863,CY006635:0.00124):0.0):0.00062,(((CY036847:0.002495,CY010004:0.001867):0.000621,CY012200:0.000621):0.0,(((CY010028:0.001242,CY009732:0.001242):0.0,CY010012:0.002484):0.001875,(((CY010020:0.002497,CY011416:0.001237):0.001252,CY009484:0.00062):0.005658,((CY010036:0.0,(CY039879:0.002489,CY039880:0.000621):0.002487):0.003109,((CY010628:0.000619,(CY010716:0.002485,CY010516:0.001239):0.0):0.000619,((CY012728:0.0,CY013701:0.000621):0.001243,(((CY012760:0.001239,CY013200:0.001239):0.0,CY011888:0.005614):0.0,((CY013693:0.000619,(CY012184:0.002484,CY013669:0.00124):0.00124):0.0,((CY112669:0.004353,(CY112556:0.001861,CY011896:0.000619):0.00186):0.0,(CY112605:0.001243,(CY012224:0.006953,((CY012512:0.000619,(CY012896:0.00062,CY012232:0.00062):0.000621):0.0,(CY011848:0.0,(((CY011328:0.0,CY114221:0.000619):0.001241,CY011560:0.00124):0.0,((CY012456:0.000619,CY011824:0.00124):0.0,CY017283:0.000619):0.0):0.0):0.0):0.002439):0.008263):0.000618):0.0):0.0):0.000617):0.012609):0.000619):0.001215):0.003782):0.000613):0.006878):0.0):0.001862):0.0):0.0):0.001863):0.001862):0.001245):0.0):0.001241):0.021084):0.000623):0.00065):0.003713):0.002495):0.0):0.005637):0.00313):0.002515):0.001876):0.0):0.000623):0.0):0.003749):0.0):0.0):0.000623):0.000623):0.001872):0.002503):0.0):0.0):0.000623):0.001468):0.00189):0.002721):0.002524):0.0):0.000624):0.0):0.0):0.0):0.000623):0.001248):0.001255):0.000619):0.0):0.0):0.0):0.000623):0.0):0.0):0.0)

Would you like to use it:(Y/N)?Y




FUBAR will write intermediate and result files to
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.extension

[FUBAR PHASE 1] Optimizing relative branch lengths under the nucleotide REV model
[FUBAR PHASE 1 FINISHED] log(L) = -7505.961582661496
	Length of tree 1 (substitutions/site) = 0.4040753831941774
[DIAGNOSTIC] FUBAR wrote the self-contained nucleotide fit file to /Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.gtr_fit


<<Number of grid points per dimension (total number is D^2) (permissible range = [5,50], default value = 20, integer)>>20
[DIAGNOSTIC] FUBAR will use a 20X20 grid
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.gtr_fit
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.codon_fit
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.grid_info
20
[FUBAR PHASE 2] Determining appropriate branch scaling using the 20X20 grid points.
	Best scaling achieved for dN/dS =  0.29.
	Computing site-by-site likelihoods at 20X20 grid points
	Finished with likelihood calculations. Achieved throughput of  10.53 calculations/second
[DIAGNOSTIC] FUBAR wrote the self-contained codon fit file to /Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.codon_fit
[DIAGNOSTIC] FUBAR wrote the the site likelihoods file to /Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.grid_info


<<Number of MCMC chains to run (permissible range = [2,20], default value = 5, integer)>>5
[DIAGNOSTIC] FUBAR will use run 5 independent chains
<<The length of each chain (permissible range = [500000,100000000], default value = 2000000, integer)>>2000000
[DIAGNOSTIC] FUBAR will run the chains for 2000000 steps
<<Discard this many samples as burn-in (permissible range = [100000,1900000], default value = 1000000, integer)>>1000000
[DIAGNOSTIC] FUBAR will run discard 1000000 steps as burn-in
<<How many samples should be drawn from each chain (permissible range = [10,1000000], default value = 100, integer)>>100
[DIAGNOSTIC] FUBAR will run thin each chain down to 100 samples
<<The concentration parameter of the Dirichlet prior (permissible range = [0.001,1], default value = 0.5)>>0.5
[DIAGNOSTIC] FUBAR will use the Dirichlet prior concentration parameter of 0.5
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.samples
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.grid_info
5
2000000
1000000
100
0.5

[FUBAR PHASE 3] Running an MCMC chain (ID 0) to obtain a posterior sample of grid point weights: 2000000 total steps, of which 1000000 will be discarded as burn-in, and sampling every 10000 steps. Dirichlet prior concentration parameter = 0.5.

[FUBAR PHASE 3] Running an MCMC chain (ID 1) to obtain a posterior sample of grid point weights: 2000000 total steps, of which 1000000 will be discarded as burn-in, and sampling every 10000 steps. Dirichlet prior concentration parameter = 0.5.

[FUBAR PHASE 3] Running an MCMC chain (ID 2) to obtain a posterior sample of grid point weights: 2000000 total steps, of which 1000000 will be discarded as burn-in, and sampling every 10000 steps. Dirichlet prior concentration parameter = 0.5.

[FUBAR PHASE 3] Running an MCMC chain (ID 3) to obtain a posterior sample of grid point weights: 2000000 total steps, of which 1000000 will be discarded as burn-in, and sampling every 10000 steps. Dirichlet prior concentration parameter = 0.5.

[FUBAR PHASE 3] Running an MCMC chain (ID 4) to obtain a posterior sample of grid point weights: 2000000 total steps, of which 1000000 will be discarded as burn-in, and sampling every 10000 steps. Dirichlet prior concentration parameter = 0.5.

[FUBAR PHASE 3 DONE] Finished running the MCMC chains; drew 5x100 samples from chains of length 2000000 after discarding 1000000 burn-in steps. Achieved throughput of  58824 moves/sec.

[DIAGNOSTIC] FUBAR wrote samples from 5 independent chains to /Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.samples[0-4]


/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.gtr_fit
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.grid_info
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.samples
5
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.fubar.csv
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.sim_codon_fit
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.sim_grid_info
/Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.codon_fit

[DIAGNOSTIC] FUBAR wrote the results of its analysis to /Users/sjspielman/Research/book-chapter-2017/datasets/trunk.dat.fubar.csv

[RESULTS] At posterior probability >= 0.9 there were 5 sites under diversifying positive selection, of which  0.25 [0 - 1] are expected to be false positives.

Codon	Prob[dN/dS>1]	EBF[dN/dS]>1	PSRF	N_eff
154	0.9792455873998263	135.5085825291314	1.002669516420821	327.5562792964825
208	0.9679391716892779	86.70795685131961	1.004667820364042	260.7157734980822
242	0.9527006089029333	57.84775622024963	1.009389000745099	176.4811006168593
69	0.9293967842677076	37.80613744196437	1.004189811183296	274.0630215232991
61	0.9239715247472688	34.90341587102175	1.004012996713934	279.3583433500093


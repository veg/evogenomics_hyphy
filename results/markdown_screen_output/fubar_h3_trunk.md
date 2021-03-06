
Analysis Description
--------------------
Perform a Fast Unbiased AppRoximate Bayesian (FUBAR) analysis of a
coding sequence alignment to determine whether some sites have been
subject to pervasive purifying or diversifying selection. Please note
that a FUBAR analysis generates a cache and a results JSON file in the
same directory as directory as the original alignment. HyPhy needs to
have write privileges to this directory. For example if the original
file is in /home/sergei/FUBAR/data/pol.nex then at the end of a FUBAR
run, there will also exist FUBAR-generated files
/home/sergei/FUBAR/data/pol.nex.fubar.json,
/home/sergei/FUBAR/data/pol.nex.fubrarcache. They also provide
checkpointing so that a partially completed analysis can be restarted.

- __Requirements__: in-frame codon alignment (possibly partitioned) and a phylogenetic tree
(one per partition)

- __Citation__: FUBAR: a fast, unconstrained bayesian approximation for inferring
selection (2013), Mol Biol Evol. 30(5):1196-205

- __Written by__: Sergei L Kosakovsky Pond

- __Contact Information__: spond@temple.edu

- __Analysis Version__: 2.0



>A tree was found in the data file: `((KF790010:0.001247,CY147300:0.000623):0.0,((CY168239:0.001872,(CY171039:0.001874,KF790389:0.000623):0.000624):0.0,((CY141224:0.001247,(CY147305:0.0,KF790037:0.000623):0.000623):0.0,(((KF790403:0.000623,KF761507:0.001876):0.0,KC526205:0.000623):0.0,((CY169303:0.0,(KF789585:0.000623,CY141202:0.000623):0.000623):0.000623,(((KJ667974:0.002501,KJ938675:0.001873):0.000623,CY134876:0.0):0.000623,((KF790414:0.001248,(KF790384:0.001245,KF790408:0.00125):0.0):0.0,((KF886352:0.001882,(KF790438:0.000623,CY134996:0.001873):0.000623):0.001875,(KF789591:0.001879,((KF790049:0.001255,(CY134956:0.000624,CY183153:0.000624):0.000626):0.001249,((CY168407:0.004394,CY183065:0.003128):0.0,(KF598733:0.002501,((KC892174:0.0,(KF685747:0.000624,CY168471:0.000625):0.00375):0.000624,(((KC892685:0.000624,KC892641:0.0):0.001874,KC893110:0.001249):0.0,(KC892480:0.0,(JX913043:0.001249,(KF551075:0.00125,((CY114509:0.0,(KC892889:0.0,KC893018:0.002498):0.005006):0.001877,(((KC892519:0.0,KC892498:0.000624):0.002497,KC892266:0.000623):0.001026,((KC892156:0.003756,(JX978746:0.001256,KC892407:0.001883):0.001875):0.00355,((KC535402:0.000623,(KC882488:0.002498,KC535387:0.001247):0.001872):0.0,(KC535363:0.000623,((KC535396:0.000623,(KC882883:0.0,KC882867:0.000623):0.003124):0.0,((KC535378:0.001872,KC535375:0.002498):0.0,(GQ385891:0.001248,((EU779522:0.001251,(CY037727:0.0,FJ179354:0.003124):0.0):0.000623,((GQ385889:0.005007,(FJ686933:0.001243,FJ179356:0.003117):0.0):0.000622,(CY173095:0.001245,(((CY173191:0.0,CY037703:0.001247):0.000622,CY035062:0.00249):0.0,((CY173255:0.001871,(CY044748:0.0,GQ385846:0.001247):0.000623):0.0,((CY027075:0.000623,(EU199367:0.0,CY172823:0.000623):0.0):0.000623,(((CY172847:0.000623,CY025643:0.0):0.000623,CY172839:0.000623):0.001247,(((CY026251:0.002497,CY092241:0.00125):0.000624,CY026019:0.000623):0.0,((CY025341:0.002502,(CY172775:0.001247,CY172903:0.000623):0.001248):0.000622,(EU199255:0.003134,(CY172431:0.000621,((CY172223:0.003127,(CY172191:0.001254,CY020069:0.000628):0.000621):0.0,((CY092217:0.003119,(CY025485:0.001283,EU516019:0.00059):0.008843):0.001868,(CY002080:0.000622,((CY002064:0.001873,(CY002456:0.000626,CY002048:0.002491):0.001243):0.003763,(AB434109:0.006307,(((CY088198:0.001245,CY088475:0.000621):0.0,CY000257:0.000621):0.002494,((CY112957:0.003135,CY006859:0.001253):0.000616,((CY000721:0.001243,(CY114493:0.0,CY090885:0.002483):0.002488):0.0,((CY001792:0.000621,(CY001600:0.00062,CY002368:0.001865):0.0):0.0,((CY002304:0.002489,(CY006163:0.001242,CY003632:0.00062):0.0):0.00062,(CY001920:0.003739,(CY001912:0.002498,((CY001504:0.0,CY006060:0.001241):0.00062,((CY001744:0.0,CY002136:0.00124):0.00062,((CY114309:0.003746,(CY006899:0.001874,CY112901:0.001863):0.002496):0.000618,(((CY006579:0.001245,CY006283:0.000621):0.001244,CY007979:0.001864):0.0,((CY006499:0.001241,(CY006491:0.001863,CY006635:0.00124):0.0):0.00062,(((CY036847:0.002495,CY010004:0.001867):0.000621,CY012200:0.000621):0.0,(((CY010028:0.001242,CY009732:0.001242):0.0,CY010012:0.002484):0.001875,(((CY010020:0.002497,CY011416:0.001237):0.001252,CY009484:0.00062):0.005658,((CY010036:0.0,(CY039879:0.002489,CY039880:0.000621):0.002487):0.003109,((CY010628:0.000619,(CY010716:0.002485,CY010516:0.001239):0.0):0.000619,((CY012728:0.0,CY013701:0.000621):0.001243,(((CY012760:0.001239,CY013200:0.001239):0.0,CY011888:0.005614):0.0,((CY013693:0.000619,(CY012184:0.002484,CY013669:0.00124):0.00124):0.0,((CY112669:0.004353,(CY112556:0.001861,CY011896:0.000619):0.00186):0.0,(CY112605:0.001243,(CY012224:0.006953,((CY012512:0.000619,(CY012896:0.00062,CY012232:0.00062):0.000621):0.0,(CY011848:0.0,(((CY011328:0.0,CY114221:0.000619):0.001241,CY011560:0.00124):0.0,((CY012456:0.000619,CY011824:0.00124):0.0,CY017283:0.000619):0.0):0.0):0.0):0.002439):0.008263):0.000618):0.0):0.0):0.000617):0.012609):0.000619):0.001215):0.003782):0.000613):0.006878):0.0):0.001862):0.0):0.0):0.001863):0.001862):0.001245):0.0):0.001241):0.021084):0.000623):0.00065):0.003713):0.002495):0.0):0.005637):0.00313):0.002515):0.001876):0.0):0.000623):0.0):0.003749):0.0):0.0):0.000623):0.000623):0.001872):0.002503):0.0):0.0):0.000623):0.001468):0.00189):0.002721):0.002524):0.0):0.000624):0.0):0.0):0.0):0.000623):0.001248):0.001255):0.000619):0.0):0.0):0.0):0.000623):0.0):0.0):0.0)`

>Would you like to use it (y/n)? Y


>Loaded a multiple sequence alignment with **163** sequences, **566** codons, and **1** partitions from `/home/sjspielman/evogenomics_hyphy/datasets/h3_trunk.fna`
> FUBAR will write cache and result files to _/home/sjspielman/evogenomics_hyphy/datasets/h3_trunk.fna.cache_ and _/home/sjspielman/evogenomics_hyphy/datasets/h3_trunk.fna.json_, respectively 


> Number of grid points per dimension (total number is D^2) (permissible range = [5,50], default value = 20, integer): 20
> Number of MCMC chains to run (permissible range = [2,20], default value = 5, integer): 5
> The length of each chain (permissible range = [500000,50000000], default value = 2000000, integer): 2000000
> Use this many samples as burn-in (permissible range = [100000,1900000], default value = 1000000, integer): 1000000
> How many samples should be drawn from each chain (permissible range = [50,1000000], default value = 100, integer): 100
> The concentration parameter of the Dirichlet prior (permissible range = [0.001,1], default value = 0.5): 0.5


### Obtaining branch lengths and nucleotide substitution biases under the nucleotide GTR model
* Log(L) = -7506.06, AIC-c = 15674.92 (331 estimated parameters)
* Tree length (expected substitutions/site) for partition 1 :    0.404

### Computing the phylogenetic likelihood function on the grid 
* Determining appropriate tree scaling based on the best score from a  20 x 20 rate grid
* Best scaling achieved for 
	* synonymous rate =  2.815
	* non-synonymous rate =  0.571
* Computing conditional site likelihoods on a 20 x 20 rate grid

### Running MCMC chains to obtain a posterior sample of (synonymous,non-synonymous) rate weights
* Using the following settings
	* Number of chains : 5
	* Steps/chain      : 2000000
	* Burn-in steps    : 1000000
	* Samples/chain    : 100
	* Dirichlet alpha  : 0.5
* Running MCMC chain 1
* Running MCMC chain 2
* Running MCMC chain 3
* Running MCMC chain 4
* Running MCMC chain 5

### Tabulating site-level results
|     Codon      |   Partition    |     alpha      |      beta      |     N.eff      |Posterior prob for positive selection|
|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:-----------------------------------:|
|       61       |       1        |        0.755   |        4.403   |       72.964   |       Pos. posterior = 0.9243       |
|       64       |       1        |        0.757   |        3.958   |       75.118   |       Pos. posterior = 0.9073       |
|       69       |       1        |        0.733   |        4.484   |       73.188   |       Pos. posterior = 0.9306       |
|      154       |       1        |        0.628   |        6.607   |       90.265   |       Pos. posterior = 0.9827       |
|      208       |       1        |        0.618   |        5.940   |       77.098   |       Pos. posterior = 0.9727       |
|      242       |       1        |        2.198   |       12.000   |     1077.748   |       Pos. posterior = 0.9154       |
----
## FUBAR inferred 6 sites subject to diversifying positive selection at posterior probability >= 0.9
Of these,  0.37 are expected to be false positives (95% confidence interval of 0-2 )

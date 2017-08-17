
Analysis Description
--------------------
aBSREL (Adaptive branch-site random effects likelihood) uses an adaptive
random effects branch-site model framework to test whether each branch
has evolved under positive selection, using a procedure which infers an
optimal number of rate categories per branch.

- __Requirements__: in-frame codon alignment and a phylogenetic tree

- __Citation__: Less Is More: An Adaptive Branch-Site Random Effects Model for Efficient
Detection of Episodic Diversifying Selection (2015). Mol Biol Evol 32
(5): 1342-1353

- __Written by__: Sergei L Kosakovsky Pond, Ben Murrell, Steven Weaver and Temple iGEM /
UCSD viral evolution group

- __Contact Information__: spond@temple.edu

- __Analysis Version__: 1.0



>A tree was found in the data file: `((((Halimione_pedunculata_C3:0.00864425,Halimione_verrucifera_C3:0.00092984)99:0.00537145,(((((Axyris_prostrata_C3:0.01534606,(Ceratocarpus_arenarius_C3:0.02990907,Krascheninnikovia_ceratoides_C3:0.01600814)99:0.01061137)97:0.01138461,((((Suckleya_suckleyana_C3:0.02012189,(Cycloloma_atriplicifolium_C3:0.00640215,(((Chenopodium_cristatum_C3:0.00634437,Dysphania_glomulifera_C3:0.00288888)82:0.00460287,Chenopodium_ambrosioides_C3:0.00969603)22:0.00000102,Chenopodium_botrys_C3:0.00526699)53:0.00107999)78:0.00625852)94:0.00776160,Teloxys_aristata_C3:0.01280784)60:0.00226243,((((Hablitzia_tamnoides_C3:0.01134794,(Aphanisma_blitoides_C3:0.00619394,Patellifolia_patellaris_C3:0.00764319)86:0.00433032)81:0.00373440,(Beta_vulgaris_C3:0.00636735,Beta_nana_C3:0.00208042)100:0.00762631)56:0.00483380,(((((Ptilotus_manglesii_C3:0.01107055,(((Iresine_palmeri_C3:0.00424920,((Gomphrena_elegans_C3:0.00663687,(Pseudoplantago_friesii_C3:0.00419924,Hebanthe_occidentalis_C3:0.00000102)100:0.00949326)96:0.00646777,(((Guilleminea_densa_C4:0.01097833,(Gomphrena_serrata_C4:0.00106511,Gomphrena_haageana_C4:0.00317777)95:0.00215240)73:0.00100613,Blutaparon_vermiculare_C4:0.00106592)93:0.00746116,((Alternanthera_pungens_C4:0.00211324,(Alternanthera_caracasana_C4:0.00105849,Alternanthera_repens_C4:0.00000102)70:0.00000102)100:0.01201192,Tidestromia_lanuginosa_C4:0.02218561)74:0.00114104)66:0.00511913)79:0.00349103)36:0.00101479,Aerva_javanica_C4:0.01510976)17:0.00000102,(Pupalia_lappacea_C3:0.00526750,(((Sericostachys_scandens_C3:0.00745715,(Achyranthes_aspera_C3:0.00105486,Nototrichium_humile_C3:0.00419384)94:0.00318201)42:0.00101179,Pandiaka_angustifolia_C3:0.00633305)14:0.00000102,Calicorema_capitata_C3:0.00209471)10:0.00000102)63:0.00209457)59:0.00062618)100:0.01733079,(((Chamissoa_altissima_C3:0.02775692,((Amaranthus_greggii_C4:0.00000102,Amaranthus_tricolor_C4:0.00105299)83:0.00000102,(Amaranthus_blitum_C4:0.00000102,Amaranthus_hypochondriacus_C4:0.00643206)96:0.00318172)100:0.01451714)100:0.01188603,(Deeringia_amaranthoides_C3:0.01401420,(Hermbstaedtia_glauca_C3:0.01188740,(Celosia_trigyna_C3:0.00334626,Celosia_argentea_C3:0.00847134)100:0.01103714)89:0.00739590)78:0.00290398)96:0.01207656,(Charpentiera_ovata_C3:0.00000102,Charpentiera_obovata_C3:0.00209837)100:0.02101136)51:0.00404498)90:0.00873580,Bosea_yervamora_C3:0.01246853)55:0.00123834,((Nitrophila_occidentalis_C3:0.00423941,Hemichroa_diandra_C3:0.00313045)100:0.00491046,Polycnemum_perenne_C3:0.01602915)100:0.01564853)62:0.00340750,Oreobliton_thesioides_C3:0.02566195)25:0.00231295)6:0.00112808,((((((Halocharis_hispida_C4:0.00853137,(Salsola_vermiculata_C4:0.01173181,(Salsola_implicata_C4:0.00524366,((Salsola_orientalis_C4:0.00000102,Salsola_dshungarica_C4:0.00000102)96:0.00210063,Salsola_micranthera_C4:0.00105274)89:0.00209641)51:0.00000102)96:0.00426190)96:0.00395543,((((Petrosimonia_glaucescens_C4:0.00000102,Petrosimonia_squarrosa_C4:0.00000102)100:0.00322210,Petrosimonia_nigdeensis_C4:0.01301656)94:0.00193353,Petrosimonia_sibirica_C4:0.00758872)91:0.00287087,(((Halimocnemis_villosa_C4:0.00000102,Halimocnemis_karelinii_C4:0.00000102)100:0.01067822,((Salsola_sukaczevii_C4:0.00000102,(Salsola_ferganica_C4:0.00000102,Salsola_heptapotamica_C4:0.00000102)17:0.00000102)30:0.00000102,Climacoptera_lanata_C4:0.00000102)99:0.00316698)85:0.00115767,(Salsola_affinis_C4:0.00480242,Climacoptera_brachiata_C4:0.00210931)82:0.00143556)94:0.00353572)93:0.00540349)77:0.00242058,(Nanophyton_erinaceum_C4:0.01724365,(((((Kochia_americana_C3:0.00536817,Bassia_diffusa_C3:0.00421106)99:0.00431594,((Bassia_dasyphylla_C3:0.00531623,(Maireana_brevifolia_C3:0.00104529,(Sclerolaena_obliquicuspis_C3:0.00315592,(Roycea_divaricata_C3:0.00104718,Dissocarpus_paradoxus_C3:0.00105135)41:0.00000102)64:0.00105266)74:0.00102656)83:0.00214954,((Kochia_densiflora_C4:0.00848085,(Chenoleoides_tomentosa_C4:0.00313108,(Bassia_prostrata_C4:0.01079383,Panderia_pilosa_C4:0.00868129)68:0.00199012)31:0.00000102)96:0.00634913,(Bassia_sedoides_C4:0.00519018,Camphorosma_monspeliaca_C4:0.01051475)97:0.00478526)83:0.00325729)60:0.00095378)100:0.01175947,((Sympegma_regelii_C3:0.00955615,Halothamnus_bottae_C4:0.00439455)53:0.00217134,((((((Salsola_rosacea_C4:0.00167187,Noaea_mucronata_C4:0.00464541)80:0.00215133,Ofaiston_monandrum_C4:0.01030439)94:0.00355407,Rhaphidophyton_regelii_C3:0.00208826)16:0.00000102,Salsola_arbusculiformis_C3:0.00000102)14:0.00000102,Salsola_laricifolia_C3:0.00209005)54:0.00104353,(((Anabasis_brevifolia_C4:0.00000102,Anabasis_truncata_C4:0.00314889)84:0.00104267,(Anabasis_eriopoda_C4:0.00104311,(Anabasis_aphylla_C4:0.00210649,(Anabasis_salsa_C4:0.00000102,Anabasis_elatior_C4:0.00104471)97:0.00209836)94:0.00210361)92:0.00211717)85:0.00209977,(((Girgensohnia_oppositiflora_C4:0.00635314,(Halogeton_glomeratus_C4:0.00638604,(Haloxylon_ammodendron_C4:0.00000102,Haloxylon_persicum_C4:0.00000102)100:0.00421249)47:0.00105843)19:0.00000102,((Haloxylon_tamariscifolium_C4:0.00209455,(Horaninovia_ulicina_C4:0.01192778,Halogeton_arachnoideus_C4:0.00426781)66:0.00206553)12:0.00000102,Iljinia_regelii_C4:0.00000102)8:0.00000102)64:0.00105483,Salsola_foliosa_C4:0.00634975)69:0.00209463)20:0.00000102)94:0.00506880)62:0.00115837)56:0.00324816,(Salsola_arbuscula_C4:0.00211160,(Salsola_kali_C4:0.00104118,((Salsola_chinghaiensis_C4:0.00104318,(Salsola_zaidamica_C4:0.00104394,((Salsola_komarovii_C4:0.00000102,Salsola_ruthenica_C4:0.00000102)15:0.00000102,Salsola_collina_C4:0.00000102)21:0.00000102)28:0.00000102)61:0.00104205,(Salsola_praecox_C4:0.00000102,(Salsola_pellucida_C4:0.00000102,Salsola_paulsenii_C4:0.00000102)17:0.00000102)26:0.00000102)24:0.00000102)87:0.00207039)100:0.00528234)27:0.00105494,Salsola_genistoides_C3:0.00314018)20:0.00104526)6:0.00000102)93:0.01140271,((((((Arthrocnemum_macrostachyum_C3:0.00208856,(Sarcocornia_utahensis_C3:0.00430842,Salicornia_europaea_C3:0.01084361)45:0.00208472)28:0.00214026,((Tecticornia_disarticulata_C3:0.00213150,Sclerostegia_moniliformis_C3:0.00212837)94:0.00426304,(Tecticornia_australasica_C3:0.00105460,((Salicornia_dolichostachya_C3:0.01671719,Halosarcia_indica_C4:0.00632785)54:0.00650166,Pachycornia_triandra_C3:0.00319160)8:0.00000102)4:0.00000102)18:0.00107232)41:0.00217706,((Halostachys_belangeriana_C3:0.00142728,Halopeplis_amplexicaulis_C3:0.00498422)54:0.00319933,(Kalidium_cuspidatum_C3:0.00536000,(Kalidium_caspicum_C3:0.00424783,Kalidium_foliatum_C3:0.00000102)29:0.00000102)84:0.00285700)76:0.00467946)38:0.00134451,Allenrolfea_occidentalis_C3:0.00724180)62:0.00692387,Bienertia_cycloptera_C4:0.01313946)79:0.00702054,((Suaeda_maritima_C3:0.00490738,Suaeda_crassifolia_C3:0.00388120)100:0.01891477,((Suaeda_physophora_C3:0.00588870,Suaeda_microphylla_C4:0.00486985)82:0.00972204,Suaeda_altissima_C4:0.01306847)65:0.00725815)56:0.00443597)80:0.00709752)100:0.01330392,(Agriophyllum_squarrosum_C3:0.01187852,(Corispermum_filifolium_C3:0.00957955,Anthochlamys_multinervis_C3:0.00119607)94:0.00642820)92:0.00603656)35:0.00283291,Acroglochin_chenopodioides_C3:0.01944356)15:0.00152637)14:0.00377071)12:0.00227794,(((Monolepis_nuttalliana_C3:0.00314556,Spinacia_oleracea_C3:0.02411154)100:0.01335566,Chenopodium_foliosum_C3:0.00648643)34:0.00205671,Chenopodium_bonushenricus_C3:0.00310884)39:0.00219374)19:0.00092256)97:0.00745230,Chenopodium_coronopus_C3:0.00690985)99:0.00615396,(Microgynoecium_tibeticum_C3:0.01320943,((((Chenopodium_acuminatum_C3:0.00209272,((Chenopodium_album_C3:0.00000102,Chenopodium_murale_C3:0.00104331)96:0.00314773,Chenopodium_sanctaeclarae_C3:0.00423868)18:0.00000102)5:0.00000102,Chenopodium_frutescens_C3:0.00000102)25:0.00000102,Micromonolepis_pusilla_C3:0.00526085)69:0.00099815,((Einadia_nutans_C3:0.00104063,Rhagodia_drummondi_C3:0.00000102)88:0.00208881,(Chenopodium_desertorum_C3:0.00104282,Chenopodium_auricomum_C3:0.00104393)38:0.00000102)64:0.00321817)100:0.01116813)80:0.00067388)99:0.00433628,(Manochlamys_albicans_C3:0.00519597,Archiatriplex_nanpinensis_C3:0.00861502)61:0.00212072)63:0.00206883)100:0.00649188,(((((Atriplex_parryi_C4:0.00104219,((Atriplex_phyllostegia_C4:0.00104244,Atriplex_serenana_C4:0.00000102)43:0.00000102,Atriplex_powellii_C4:0.00104263)87:0.00209024)11:0.00000102,((Atriplex_lampa_C4:0.00209727,Atriplex_undulata_C4:0.00104916)67:0.00103801,Atriplex_lentiformis_C4:0.00104296)12:0.00000102)38:0.00000102,(((Atriplex_spongiosa_C4:0.00104854,Atriplex_rosea_C4:0.00313774)73:0.00000102,Atriplex_centralasiatica_C4:0.00419604)53:0.00105750,Atriplex_glauca_C4:0.00419623)72:0.00209055)42:0.00104288,Atriplex_coriacea_C4:0.00419172)61:0.00104689,(Atriplex_halimus_C4:0.00208849,Cremnophyton_lanfrancoi_C3:0.00000102)16:0.00000102)28:0.00000102)58:0.00104026,(Atriplex_australasica_C3:0.00000102,Atriplex_patula_C3:0.00000102)62:0.00000102,Atriplex_aucherii_C3:0.00208586)`

>Would you like to use it (y/n)? Y


Selected the following branches for testing
	Halimione_pedunculata_C3
	Halimione_verrucifera_C3
	Chenopodium_cristatum_C3
	Node41
	Node31
	Halocharis_hispida_C4
	Salsola_vermiculata_C4
	Salsola_implicata_C4
	Salsola_orientalis_C4
	Salsola_dshungarica_C4
	Node124
	Salsola_micranthera_C4
	Node123
	Dysphania_glomulifera_C3
	Node121
	Node119
	Node117
	Petrosimonia_glaucescens_C4
	Petrosimonia_squarrosa_C4
	Node131
	Petrosimonia_nigdeensis_C4
	Node130
	Petrosimonia_sibirica_C4
	Node129
	Node24
	Halimocnemis_villosa_C4
	Halimocnemis_karelinii_C4
	Node138
	Salsola_sukaczevii_C4
	Salsola_ferganica_C4
	Salsola_heptapotamica_C4
	Node144
	Node142
	Climacoptera_lanata_C4
	Node141
	Chenopodium_ambrosioides_C3
	Node137
	Salsola_affinis_C4
	Climacoptera_brachiata_C4
	Node148
	Node136
	Node128
	Node116
	Nanophyton_erinaceum_C4
	Kochia_americana_C3
	Bassia_diffusa_C3
	Node23
	Node157
	Bassia_dasyphylla_C3
	Maireana_brevifolia_C3
	Sclerolaena_obliquicuspis_C3
	Roycea_divaricata_C3
	Dissocarpus_paradoxus_C3
	Node167
	Node165
	Node163
	Node161
	Chenopodium_botrys_C3
	Kochia_densiflora_C4
	Chenoleoides_tomentosa_C4
	Bassia_prostrata_C4
	Panderia_pilosa_C4
	Node175
	Node173
	Node171
	Bassia_sedoides_C4
	Camphorosma_monspeliaca_C4
	Node178
	Node22
	Node170
	Node160
	Node156
	Sympegma_regelii_C3
	Halothamnus_bottae_C4
	Node182
	Salsola_rosacea_C4
	Noaea_mucronata_C4
	Node190
	Ofaiston_monandrum_C4
	Node20
	Node189
	Rhaphidophyton_regelii_C3
	Node188
	Salsola_arbusculiformis_C3
	Node187
	Salsola_laricifolia_C3
	Node186
	Anabasis_brevifolia_C4
	Anabasis_truncata_C4
	Node199
	Node18
	Anabasis_eriopoda_C4
	Anabasis_aphylla_C4
	Anabasis_salsa_C4
	Anabasis_elatior_C4
	Node206
	Node204
	Node202
	Node198
	Girgensohnia_oppositiflora_C4
	Halogeton_glomeratus_C4
	Teloxys_aristata_C3
	Haloxylon_ammodendron_C4
	Haloxylon_persicum_C4
	Node215
	Node213
	Node211
	Haloxylon_tamariscifolium_C4
	Horaninovia_ulicina_C4
	Halogeton_arachnoideus_C4
	Node221
	Node219
	Node3
	Node17
	Iljinia_regelii_C4
	Node218
	Node210
	Salsola_foliosa_C4
	Node209
	Node197
	Node185
	Node181
	Node155
	Salsola_arbuscula_C4
	Hablitzia_tamnoides_C3
	Salsola_kali_C4
	Salsola_chinghaiensis_C4
	Salsola_zaidamica_C4
	Salsola_komarovii_C4
	Salsola_ruthenica_C4
	Node236
	Salsola_collina_C4
	Node235
	Node233
	Node231
	Aphanisma_blitoides_C3
	Salsola_praecox_C4
	Salsola_pellucida_C4
	Salsola_paulsenii_C4
	Node242
	Node240
	Node230
	Node228
	Node226
	Node154
	Salsola_genistoides_C3
	Patellifolia_patellaris_C3
	Node153
	Node151
	Node115
	Arthrocnemum_macrostachyum_C3
	Sarcocornia_utahensis_C3
	Salicornia_europaea_C3
	Node253
	Node251
	Tecticornia_disarticulata_C3
	Sclerostegia_moniliformis_C3
	Node35
	Node257
	Tecticornia_australasica_C3
	Salicornia_dolichostachya_C3
	Halosarcia_indica_C4
	Node263
	Pachycornia_triandra_C3
	Node262
	Node260
	Node256
	Node250
	Node33
	Halostachys_belangeriana_C3
	Halopeplis_amplexicaulis_C3
	Node268
	Kalidium_cuspidatum_C3
	Kalidium_caspicum_C3
	Kalidium_foliatum_C3
	Node273
	Node271
	Node267
	Node249
	Beta_vulgaris_C3
	Allenrolfea_occidentalis_C3
	Node248
	Bienertia_cycloptera_C4
	Node247
	Suaeda_maritima_C3
	Suaeda_crassifolia_C3
	Node279
	Suaeda_physophora_C3
	Suaeda_microphylla_C4
	Node283
	Beta_nana_C3
	Suaeda_altissima_C4
	Node282
	Node278
	Node246
	Node114
	Agriophyllum_squarrosum_C3
	Corispermum_filifolium_C3
	Anthochlamys_multinervis_C3
	Node289
	Node287
	Node38
	Node113
	Acroglochin_chenopodioides_C3
	Node112
	Node30
	Node16
	Monolepis_nuttalliana_C3
	Spinacia_oleracea_C3
	Node295
	Chenopodium_foliosum_C3
	Node294
	Node32
	Chenopodium_bonushenricus_C3
	Node293
	Node15
	Node9
	Chenopodium_coronopus_C3
	Node8
	Microgynoecium_tibeticum_C3
	Chenopodium_acuminatum_C3
	Chenopodium_album_C3
	Chenopodium_murale_C3
	Axyris_prostrata_C3
	Ptilotus_manglesii_C3
	Node309
	Chenopodium_sanctaeclarae_C3
	Node308
	Node306
	Chenopodium_frutescens_C3
	Node305
	Micromonolepis_pusilla_C3
	Node304
	Einadia_nutans_C3
	Rhagodia_drummondi_C3
	Iresine_palmeri_C3
	Node316
	Chenopodium_desertorum_C3
	Chenopodium_auricomum_C3
	Node319
	Node315
	Node303
	Node301
	Node7
	Manochlamys_albicans_C3
	Archiatriplex_nanpinensis_C3
	Gomphrena_elegans_C3
	Node322
	Node6
	Node2
	Atriplex_parryi_C4
	Atriplex_phyllostegia_C4
	Atriplex_serenana_C4
	Node332
	Atriplex_powellii_C4
	Node331
	Node329
	Pseudoplantago_friesii_C3
	Atriplex_lampa_C4
	Atriplex_undulata_C4
	Node337
	Atriplex_lentiformis_C4
	Node336
	Node328
	Atriplex_spongiosa_C4
	Atriplex_rosea_C4
	Node343
	Atriplex_centralasiatica_C4
	Hebanthe_occidentalis_C3
	Node342
	Atriplex_glauca_C4
	Node341
	Node327
	Atriplex_coriacea_C4
	Node326
	Atriplex_halimus_C4
	Cremnophyton_lanfrancoi_C3
	Node349
	Node325
	Node54
	Node1
	Atriplex_australasica_C3
	Atriplex_patula_C3
	Node352
	Atriplex_aucherii_C3
	Node52
	Guilleminea_densa_C4
	Gomphrena_serrata_C4
	Gomphrena_haageana_C4
	Ceratocarpus_arenarius_C3
	Node61
	Node59
	Blutaparon_vermiculare_C4
	Node58
	Alternanthera_pungens_C4
	Alternanthera_caracasana_C4
	Alternanthera_repens_C4
	Node68
	Node66
	Tidestromia_lanuginosa_C4
	Krascheninnikovia_ceratoides_C3
	Node65
	Node57
	Node51
	Node49
	Aerva_javanica_C4
	Node48
	Pupalia_lappacea_C3
	Sericostachys_scandens_C3
	Achyranthes_aspera_C3
	Nototrichium_humile_C3
	Node12
	Node79
	Node77
	Pandiaka_angustifolia_C3
	Node76
	Calicorema_capitata_C3
	Node75
	Node73
	Node47
	Node45
	Chamissoa_altissima_C3
	Node10
	Amaranthus_greggii_C4
	Amaranthus_tricolor_C4
	Node89
	Amaranthus_blitum_C4
	Amaranthus_hypochondriacus_C4
	Node92
	Node88
	Node86
	Deeringia_amaranthoides_C3
	Hermbstaedtia_glauca_C3
	Suckleya_suckleyana_C3
	Celosia_trigyna_C3
	Celosia_argentea_C3
	Node99
	Node97
	Node95
	Node85
	Charpentiera_ovata_C3
	Charpentiera_obovata_C3
	Node102
	Node84
	Cycloloma_atriplicifolium_C3
	Node44
	Bosea_yervamora_C3
	Node43
	Nitrophila_occidentalis_C3
	Hemichroa_diandra_C3
	Node107
	Polycnemum_perenne_C3
	Node106
	Node42
	Oreobliton_thesioides_C3
[PHASE 0] Fitting the local MG94 (no site-to-site variation) to obtain initial parameter estimates

Log L = -10687.69483402032 with 724 degrees of freedom. IC = 22836.6300070579

Branch omega values

	Count    = 355
	Mean     = 2.87561817813965
	Median   = 0.1358042567482686
	Variance = 19.7141785429052
	Std.Dev  = 4.440065150750065
	COV      = 1.544038490402963
	Sum      = 1020.844453239576
	Sq. sum  = 9914.378070977196
	Skewness = 4.375367796213713
	Kurtosis = 8.50403645367658
	Min      = 0
	2.5%     = 0
	97.5%    = 10
	Max      = 10

[PHASE 1] Fitting Branch Site REL models to one branch at a time

[PHASE 1] Branch Ceratocarpus_arenarius_C3 log(L) = -10684.198, IC = 22833.709
	2 rate classes
	Node: mixtureTree.Ceratocarpus_arenarius_C3
	Length parameter = 0.1864917412140149
	Class 1
		omega = 0.000
		weight = 0.979
	Class 2
		omega = 6.446
		weight = 0.021

[PHASE 1] Branch Ceratocarpus_arenarius_C3 log(L) = -10684.19780643258, IC = 22837.78323205692
	3 rate classes
	Node: mixtureTree.Ceratocarpus_arenarius_C3
	Length parameter = 0.1864842062455933
	Class 1
		omega = 0.000
		weight = 0.978
	Class 2
		omega = 0.000
		weight = 0.000
	Class 3
		omega = 6.492
		weight = 0.021

[PHASE 1] Branch Chamissoa_altissima_C3 log(L) = -10684.201, IC = 22837.789
	2 rate classes
	Node: mixtureTree.Chamissoa_altissima_C3
	Length parameter = 0.1840242180053837
	Class 1
		omega = 0.059
		weight = 0.862
	Class 2
		omega = 0.146
		weight = 0.138

[PHASE 1] Branch Oreobliton_thesioides_C3 log(L) = -10684.198, IC = 22837.784
	2 rate classes
	Node: mixtureTree.Oreobliton_thesioides_C3
	Length parameter = 0.1900063366917283
	Class 1
		omega = 0.039
		weight = 0.980
	Class 2
		omega = 0.109
		weight = 0.020

[PHASE 1] Branch Spinacia_oleracea_C3 log(L) = -10684.202, IC = 22837.791
	2 rate classes
	Node: mixtureTree.Spinacia_oleracea_C3
	Length parameter = 0.1888659501611533
	Class 1
		omega = 0.016
		weight = 0.855
	Class 2
		omega = 0.095
		weight = 0.145

[PHASE 1] Branch Tidestromia_lanuginosa_C4 log(L) = -10684.201, IC = 22837.790
	2 rate classes
	Node: mixtureTree.Tidestromia_lanuginosa_C4
	Length parameter = 0.1835788471167193
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.741
		weight = 0.020

[PHASE 1] Branch Node102 log(L) = -10680.027, IC = 22829.441
	2 rate classes
	Node: mixtureTree.Node102
	Length parameter = 0.1206064612104016
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 13.858
		weight = 0.019

[PHASE 1] Branch Node102 log(L) = -10680.02636008183, IC = 22833.51428773259
	3 rate classes
	Node: mixtureTree.Node102
	Length parameter = 0.120747393271121
	Class 1
		omega = 0.000
		weight = 0.974
	Class 2
		omega = 0.000
		weight = 0.007
	Class 3
		omega = 13.934
		weight = 0.019

[PHASE 1] Branch Suckleya_suckleyana_C3 log(L) = -10680.037, IC = 22833.535
	2 rate classes
	Node: mixtureTree.Suckleya_suckleyana_C3
	Length parameter = 0.1440289058789781
	Class 1
		omega = 0.002
		weight = 0.746
	Class 2
		omega = 0.210
		weight = 0.254

[PHASE 1] Branch Node279 log(L) = -10680.032, IC = 22833.525
	2 rate classes
	Node: mixtureTree.Node279
	Length parameter = 0.1493462627662678
	Class 1
		omega = 0.020
		weight = 0.917
	Class 2
		omega = 0.198
		weight = 0.083

[PHASE 1] Branch Acroglochin_chenopodioides_C3 log(L) = -10672.711, IC = 22818.884
	2 rate classes
	Node: mixtureTree.Acroglochin_chenopodioides_C3
	Length parameter = 0.105163121445937
	Class 1
		omega = 0.000
		weight = 0.984
	Class 2
		omega = 15.197
		weight = 0.016

[PHASE 1] Branch Acroglochin_chenopodioides_C3 log(L) = -10672.71127870632, IC = 22822.95827890608
	3 rate classes
	Node: mixtureTree.Acroglochin_chenopodioides_C3
	Length parameter = 0.1050875148883769
	Class 1
		omega = 0.000
		weight = 0.984
	Class 2
		omega = 0.000
		weight = 0.000
	Class 3
		omega = 15.329
		weight = 0.016

[PHASE 1] Branch Nanophyton_erinaceum_C4 log(L) = -10672.712, IC = 22822.959
	2 rate classes
	Node: mixtureTree.Nanophyton_erinaceum_C4
	Length parameter = 0.1401346576701291
	Class 1
		omega = 0.018
		weight = 0.999
	Class 2
		omega = 0.205
		weight = 0.001

[PHASE 1] Branch Salicornia_dolichostachya_C3 log(L) = -10659.996, IC = 22797.528
	2 rate classes
	Node: mixtureTree.Salicornia_dolichostachya_C3
	Length parameter = 0.08512228278240165
	Class 1
		omega = 0.040
		weight = 0.993
	Class 2
		omega = 89.219
		weight = 0.007

[PHASE 1] Branch Salicornia_dolichostachya_C3 log(L) = -10659.99597410096, IC = 22801.60202918277
	3 rate classes
	Node: mixtureTree.Salicornia_dolichostachya_C3
	Length parameter = 0.08496209259064523
	Class 1
		omega = 0.040
		weight = 0.993
	Class 2
		omega = 0.042
		weight = 0.000
	Class 3
		omega = 89.482
		weight = 0.007

[PHASE 1] Branch Node45 log(L) = -10653.589, IC = 22788.788
	2 rate classes
	Node: mixtureTree.Node45
	Length parameter = 0.08106457601351341
	Class 1
		omega = 0.000
		weight = 0.988
	Class 2
		omega = 26.168
		weight = 0.012

[PHASE 1] Branch Node45 log(L) = -10653.58756783018, IC = 22792.85978170708
	3 rate classes
	Node: mixtureTree.Node45
	Length parameter = 0.08101098092267676
	Class 1
		omega = 0.000
		weight = 0.988
	Class 2
		omega = 0.000
		weight = 0.001
	Class 3
		omega = 26.796
		weight = 0.012

[PHASE 1] Branch Polycnemum_perenne_C3 log(L) = -10653.589, IC = 22792.863
	2 rate classes
	Node: mixtureTree.Polycnemum_perenne_C3
	Length parameter = 0.136166275420845
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Krascheninnikovia_ceratoides_C3 log(L) = -10653.589, IC = 22792.863
	2 rate classes
	Node: mixtureTree.Krascheninnikovia_ceratoides_C3
	Length parameter = 0.06389076086621381
	Class 1
		omega = 0.399
		weight = 0.317
	Class 2
		omega = 0.254
		weight = 0.683

[PHASE 1] Branch Aerva_javanica_C4 log(L) = -10653.597, IC = 22792.879
	2 rate classes
	Node: mixtureTree.Aerva_javanica_C4
	Length parameter = 0.08332761028685387
	Class 1
		omega = 0.062
		weight = 0.645
	Class 2
		omega = 0.329
		weight = 0.355

[PHASE 1] Branch Node106 log(L) = -10653.132, IC = 22791.948
	2 rate classes
	Node: mixtureTree.Node106
	Length parameter = 0.08216337550216574
	Class 1
		omega = 0.000
		weight = 0.976
	Class 2
		omega = 9.466
		weight = 0.024

[PHASE 1] Branch Axyris_prostrata_C3 log(L) = -10653.588, IC = 22792.861
	2 rate classes
	Node: mixtureTree.Axyris_prostrata_C3
	Length parameter = 0.09505920141932296
	Class 1
		omega = 0.006
		weight = 0.900
	Class 2
		omega = 0.996
		weight = 0.100

[PHASE 1] Branch Suaeda_altissima_C4 log(L) = -10653.592, IC = 22792.868
	2 rate classes
	Node: mixtureTree.Suaeda_altissima_C4
	Length parameter = 0.1076833182225429
	Class 1
		omega = 0.038
		weight = 0.962
	Class 2
		omega = 0.291
		weight = 0.038

[PHASE 1] Branch Node88 log(L) = -10653.599, IC = 22792.883
	2 rate classes
	Node: mixtureTree.Node88
	Length parameter = 0.07688149675419567
	Class 1
		omega = 0.072
		weight = 0.793
	Class 2
		omega = 0.556
		weight = 0.207

[PHASE 1] Branch Deeringia_amaranthoides_C3 log(L) = -10653.595, IC = 22792.874
	2 rate classes
	Node: mixtureTree.Deeringia_amaranthoides_C3
	Length parameter = 0.08413290876697473
	Class 1
		omega = 0.003
		weight = 0.490
	Class 2
		omega = 0.239
		weight = 0.510

[PHASE 1] Branch Microgynoecium_tibeticum_C3 log(L) = -10653.589, IC = 22792.863
	2 rate classes
	Node: mixtureTree.Microgynoecium_tibeticum_C3
	Length parameter = 0.113962944839979
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Petrosimonia_nigdeensis_C4 log(L) = -10653.534, IC = 22792.752
	2 rate classes
	Node: mixtureTree.Petrosimonia_nigdeensis_C4
	Length parameter = 0.08482118327997068
	Class 1
		omega = 0.000
		weight = 0.956
	Class 2
		omega = 2.344
		weight = 0.044

[PHASE 1] Branch Node114 log(L) = -10653.596, IC = 22792.877
	2 rate classes
	Node: mixtureTree.Node114
	Length parameter = 0.07549290639309665
	Class 1
		omega = 0.050
		weight = 0.553
	Class 2
		omega = 0.245
		weight = 0.447

[PHASE 1] Branch Node295 log(L) = -10653.590, IC = 22792.865
	2 rate classes
	Node: mixtureTree.Node295
	Length parameter = 0.05538187118530825
	Class 1
		omega = 0.213
		weight = 0.746
	Class 2
		omega = 0.492
		weight = 0.254

[PHASE 1] Branch Node66 log(L) = -10653.589, IC = 22792.863
	2 rate classes
	Node: mixtureTree.Node66
	Length parameter = 0.1066822786542418
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Teloxys_aristata_C3 log(L) = -10650.495, IC = 22786.675
	2 rate classes
	Node: mixtureTree.Teloxys_aristata_C3
	Length parameter = 0.06568390968408486
	Class 1
		omega = 0.000
		weight = 0.983
	Class 2
		omega = 15.439
		weight = 0.017

[PHASE 1] Branch Teloxys_aristata_C3 log(L) = -10650.49692028409, IC = 22790.75325727478
	3 rate classes
	Node: mixtureTree.Teloxys_aristata_C3
	Length parameter = 0.06555511446558546
	Class 1
		omega = 0.000
		weight = 0.984
	Class 2
		omega = 0.800
		weight = 0.000
	Class 3
		omega = 16.524
		weight = 0.016

[PHASE 1] Branch Node86 log(L) = -10650.048, IC = 22789.856
	2 rate classes
	Node: mixtureTree.Node86
	Length parameter = 0.08676706930577577
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 19.396
		weight = 0.005

[PHASE 1] Branch Node156 log(L) = -10650.500, IC = 22790.760
	2 rate classes
	Node: mixtureTree.Node156
	Length parameter = 0.09418075946492181
	Class 1
		omega = 0.001
		weight = 0.899
	Class 2
		omega = 0.269
		weight = 0.101

[PHASE 1] Branch Horaninovia_ulicina_C4 log(L) = -10650.501, IC = 22790.762
	2 rate classes
	Node: mixtureTree.Horaninovia_ulicina_C4
	Length parameter = 0.08519514419601128
	Class 1
		omega = 0.001
		weight = 0.746
	Class 2
		omega = 0.238
		weight = 0.254

[PHASE 1] Branch Bosea_yervamora_C3 log(L) = -10650.495, IC = 22790.749
	2 rate classes
	Node: mixtureTree.Bosea_yervamora_C3
	Length parameter = 0.07597576716575687
	Class 1
		omega = 0.103
		weight = 0.986
	Class 2
		omega = 0.092
		weight = 0.014

[PHASE 1] Branch Hermbstaedtia_glauca_C3 log(L) = -10640.127, IC = 22770.013
	2 rate classes
	Node: mixtureTree.Hermbstaedtia_glauca_C3
	Length parameter = 0.06438504187794998
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 10000.000
		weight = 0.005

[PHASE 1] Branch Hermbstaedtia_glauca_C3 log(L) = -10640.12683999346, IC = 22774.088072963
	3 rate classes
	Node: mixtureTree.Hermbstaedtia_glauca_C3
	Length parameter = 0.06438512189532161
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 0.500
		weight = 0.000
	Class 3
		omega = 10000.000
		weight = 0.005

[PHASE 1] Branch Node115 log(L) = -10640.127, IC = 22774.089
	2 rate classes
	Node: mixtureTree.Node115
	Length parameter = 0.09080374016309394
	Class 1
		omega = 0.004
		weight = 0.899
	Class 2
		omega = 0.251
		weight = 0.101

[PHASE 1] Branch Salsola_vermiculata_C4 log(L) = -10640.129, IC = 22774.092
	2 rate classes
	Node: mixtureTree.Salsola_vermiculata_C4
	Length parameter = 0.03689255719647191
	Class 1
		omega = 0.412
		weight = 0.733
	Class 2
		omega = 0.712
		weight = 0.267

[PHASE 1] Branch Node85 log(L) = -10638.039, IC = 22769.912
	2 rate classes
	Node: mixtureTree.Node85
	Length parameter = 0.08608047759081239
	Class 1
		omega = 0.002
		weight = 0.994
	Class 2
		omega = 22.066
		weight = 0.006

[PHASE 1] Branch Node85 log(L) = -10638.04008767814, IC = 22773.98975022698
	3 rate classes
	Node: mixtureTree.Node85
	Length parameter = 0.08617245992910269
	Class 1
		omega = 0.008
		weight = 0.994
	Class 2
		omega = 1.000
		weight = 0.001
	Class 3
		omega = 28.000
		weight = 0.005

[PHASE 1] Branch Node99 log(L) = -10638.044, IC = 22773.997
	2 rate classes
	Node: mixtureTree.Node99
	Length parameter = 0.08868420985408937
	Class 1
		omega = 0.002
		weight = 0.898
	Class 2
		omega = 0.271
		weight = 0.102

[PHASE 1] Branch Node10 log(L) = -10631.277, IC = 22760.464
	2 rate classes
	Node: mixtureTree.Node10
	Length parameter = 0.07458615096301725
	Class 1
		omega = 0.000
		weight = 0.996
	Class 2
		omega = 72.224
		weight = 0.004

[PHASE 1] Branch Node10 log(L) = -10631.27686394208, IC = 22764.53869029017
	3 rate classes
	Node: mixtureTree.Node10
	Length parameter = 0.0744751638464205
	Class 1
		omega = 0.000
		weight = 0.996
	Class 2
		omega = 0.501
		weight = 0.000
	Class 3
		omega = 73.462
		weight = 0.004

[PHASE 1] Branch Salicornia_europaea_C3 log(L) = -10631.277, IC = 22764.539
	2 rate classes
	Node: mixtureTree.Salicornia_europaea_C3
	Length parameter = 0.09476983983375747
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node12 log(L) = -10631.277, IC = 22764.540
	2 rate classes
	Node: mixtureTree.Node12
	Length parameter = 0.08586154864610525
	Class 1
		omega = 0.007
		weight = 0.901
	Class 2
		omega = 0.247
		weight = 0.099

[PHASE 1] Branch Ptilotus_manglesii_C3 log(L) = -10631.284, IC = 22764.553
	2 rate classes
	Node: mixtureTree.Ptilotus_manglesii_C3
	Length parameter = 0.08561128896542176
	Class 1
		omega = 0.004
		weight = 0.898
	Class 2
		omega = 0.267
		weight = 0.102

[PHASE 1] Branch Agriophyllum_squarrosum_C3 log(L) = -10631.282, IC = 22764.548
	2 rate classes
	Node: mixtureTree.Agriophyllum_squarrosum_C3
	Length parameter = 0.08495348197626632
	Class 1
		omega = 0.007
		weight = 0.898
	Class 2
		omega = 0.242
		weight = 0.102

[PHASE 1] Branch Bienertia_cycloptera_C4 log(L) = -10627.687, IC = 22757.359
	2 rate classes
	Node: mixtureTree.Bienertia_cycloptera_C4
	Length parameter = 0.03178159401496635
	Class 1
		omega = 0.000
		weight = 0.978
	Class 2
		omega = 38.409
		weight = 0.022

[PHASE 1] Branch Bienertia_cycloptera_C4 log(L) = -10627.68737744343, IC = 22761.43531048447
	3 rate classes
	Node: mixtureTree.Bienertia_cycloptera_C4
	Length parameter = 0.0315731796810961
	Class 1
		omega = 0.000
		weight = 0.973
	Class 2
		omega = 0.000
		weight = 0.005
	Class 3
		omega = 39.065
		weight = 0.022

[PHASE 1] Branch Bassia_prostrata_C4 log(L) = -10627.692, IC = 22761.444
	2 rate classes
	Node: mixtureTree.Bassia_prostrata_C4
	Length parameter = 0.08395952772878779
	Class 1
		omega = 0.004
		weight = 0.898
	Class 2
		omega = 0.273
		weight = 0.102

[PHASE 1] Branch Node138 log(L) = -10627.691, IC = 22761.443
	2 rate classes
	Node: mixtureTree.Node138
	Length parameter = 0.08387608825635692
	Class 1
		omega = 0.003
		weight = 0.898
	Class 2
		omega = 0.274
		weight = 0.102

[PHASE 1] Branch Node303 log(L) = -10623.342, IC = 22752.745
	2 rate classes
	Node: mixtureTree.Node303
	Length parameter = 0.05738076427785803
	Class 1
		omega = 0.000
		weight = 0.991
	Class 2
		omega = 40.083
		weight = 0.009

[PHASE 1] Branch Node303 log(L) = -10623.33934987319, IC = 22756.81505420743
	3 rate classes
	Node: mixtureTree.Node303
	Length parameter = 0.05750218552540356
	Class 1
		omega = 0.017
		weight = 0.991
	Class 2
		omega = 0.000
		weight = 0.002
	Class 3
		omega = 52.144
		weight = 0.007

[PHASE 1] Branch Guilleminea_densa_C4 log(L) = -10623.343, IC = 22756.821
	2 rate classes
	Node: mixtureTree.Guilleminea_densa_C4
	Length parameter = 0.05732936772390411
	Class 1
		omega = 0.181
		weight = 0.978
	Class 2
		omega = 0.253
		weight = 0.022

[PHASE 1] Branch Camphorosma_monspeliaca_C4 log(L) = -10623.347, IC = 22756.831
	2 rate classes
	Node: mixtureTree.Camphorosma_monspeliaca_C4
	Length parameter = 0.07360216302260103
	Class 1
		omega = 0.045
		weight = 0.939
	Class 2
		omega = 0.469
		weight = 0.061

[PHASE 1] Branch Hablitzia_tamnoides_C3 log(L) = -10623.198, IC = 22756.531
	2 rate classes
	Node: mixtureTree.Hablitzia_tamnoides_C3
	Length parameter = 0.05639569358168615
	Class 1
		omega = 0.000
		weight = 0.978
	Class 2
		omega = 10.635
		weight = 0.022

[PHASE 1] Branch Ofaiston_monandrum_C4 log(L) = -10623.343, IC = 22756.821
	2 rate classes
	Node: mixtureTree.Ofaiston_monandrum_C4
	Length parameter = 0.05376992376109603
	Class 1
		omega = 0.195
		weight = 0.984
	Class 2
		omega = 0.068
		weight = 0.016

[PHASE 1] Branch Sympegma_regelii_C3 log(L) = -10616.515, IC = 22743.167
	2 rate classes
	Node: mixtureTree.Sympegma_regelii_C3
	Length parameter = 0.05531687106386807
	Class 1
		omega = 0.038
		weight = 0.997
	Class 2
		omega = 164.630
		weight = 0.003

[PHASE 1] Branch Sympegma_regelii_C3 log(L) = -10616.51524765567, IC = 22747.24285432322
	3 rate classes
	Node: mixtureTree.Sympegma_regelii_C3
	Length parameter = 0.05555589913140844
	Class 1
		omega = 0.038
		weight = 0.997
	Class 2
		omega = 0.500
		weight = 0.000
	Class 3
		omega = 159.441
		weight = 0.003

[PHASE 1] Branch Chenopodium_ambrosioides_C3 log(L) = -10616.516, IC = 22747.243
	2 rate classes
	Node: mixtureTree.Chenopodium_ambrosioides_C3
	Length parameter = 0.03638203992980513
	Class 1
		omega = 0.397
		weight = 0.746
	Class 2
		omega = 0.250
		weight = 0.254

[PHASE 1] Branch Node54 log(L) = -10616.520, IC = 22747.252
	2 rate classes
	Node: mixtureTree.Node54
	Length parameter = 0.06151117253240612
	Class 1
		omega = 0.057
		weight = 0.936
	Class 2
		omega = 0.497
		weight = 0.064

[PHASE 1] Branch Node44 log(L) = -10607.028, IC = 22728.267
	2 rate classes
	Node: mixtureTree.Node44
	Length parameter = 0.02553156035459619
	Class 1
		omega = 0.044
		weight = 0.995
	Class 2
		omega = 1356.108
		weight = 0.005

[PHASE 1] Branch Node44 log(L) = -10607.02752829877, IC = 22732.34362586324
	3 rate classes
	Node: mixtureTree.Node44
	Length parameter = 0.02552226722580405
	Class 1
		omega = 0.044
		weight = 0.995
	Class 2
		omega = 0.500
		weight = 0.000
	Class 3
		omega = 1366.648
		weight = 0.005

[PHASE 1] Branch Node283 log(L) = -10607.028, IC = 22732.344
	2 rate classes
	Node: mixtureTree.Node283
	Length parameter = 0.07705322116566087
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Corispermum_filifolium_C3 log(L) = -10607.028, IC = 22732.344
	2 rate classes
	Node: mixtureTree.Corispermum_filifolium_C3
	Length parameter = 0.0757594211178446
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Halocharis_hispida_C4 log(L) = -10607.028, IC = 22732.344
	2 rate classes
	Node: mixtureTree.Halocharis_hispida_C4
	Length parameter = 0.07475198522229713
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Halimione_pedunculata_C3 log(L) = -10607.028, IC = 22732.344
	2 rate classes
	Node: mixtureTree.Halimione_pedunculata_C3
	Length parameter = 0.07444820075928908
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Panderia_pilosa_C4 log(L) = -10607.032, IC = 22732.353
	2 rate classes
	Node: mixtureTree.Panderia_pilosa_C4
	Length parameter = 0.04658301081654666
	Class 1
		omega = 0.109
		weight = 0.819
	Class 2
		omega = 0.426
		weight = 0.181

[PHASE 1] Branch Archiatriplex_nanpinensis_C3 log(L) = -10607.031, IC = 22732.351
	2 rate classes
	Node: mixtureTree.Archiatriplex_nanpinensis_C3
	Length parameter = 0.05515341640495258
	Class 1
		omega = 0.068
		weight = 0.949
	Class 2
		omega = 0.579
		weight = 0.051

[PHASE 1] Branch Celosia_argentea_C3 log(L) = -10607.030, IC = 22732.348
	2 rate classes
	Node: mixtureTree.Celosia_argentea_C3
	Length parameter = 0.03713868634939674
	Class 1
		omega = 0.212
		weight = 0.744
	Class 2
		omega = 0.488
		weight = 0.256

[PHASE 1] Branch Kochia_densiflora_C4 log(L) = -10607.036, IC = 22732.361
	2 rate classes
	Node: mixtureTree.Kochia_densiflora_C4
	Length parameter = 0.04530544620041997
	Class 1
		omega = 0.066
		weight = 0.801
	Class 2
		omega = 0.607
		weight = 0.199

[PHASE 1] Branch Node246 log(L) = -10607.028, IC = 22732.344
	2 rate classes
	Node: mixtureTree.Node246
	Length parameter = 0.07125307161275839
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node248 log(L) = -10607.028, IC = 22732.344
	2 rate classes
	Node: mixtureTree.Node248
	Length parameter = 0.07107456409190238
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Petrosimonia_sibirica_C4 log(L) = -10607.028, IC = 22732.344
	2 rate classes
	Node: mixtureTree.Petrosimonia_sibirica_C4
	Length parameter = 0.06772424252401081
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Patellifolia_patellaris_C3 log(L) = -10607.037, IC = 22732.364
	2 rate classes
	Node: mixtureTree.Patellifolia_patellaris_C3
	Length parameter = 0.04343819209974539
	Class 1
		omega = 0.013
		weight = 0.756
	Class 2
		omega = 0.637
		weight = 0.244

[PHASE 1] Branch Node58 log(L) = -10607.028, IC = 22732.344
	2 rate classes
	Node: mixtureTree.Node58
	Length parameter = 0.0659649720247454
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node38 log(L) = -10602.918, IC = 22724.125
	2 rate classes
	Node: mixtureTree.Node38
	Length parameter = 0.02877719727411415
	Class 1
		omega = 0.002
		weight = 0.989
	Class 2
		omega = 48.015
		weight = 0.011

[PHASE 1] Branch Node38 log(L) = -10602.81090768625, IC = 22727.98680061059
	3 rate classes
	Node: mixtureTree.Node38
	Length parameter = 0.02867321617602095
	Class 1
		omega = 0.133
		weight = 0.990
	Class 2
		omega = 0.129
		weight = 0.006
	Class 3
		omega = 135.463
		weight = 0.004

[PHASE 1] Branch Node282 log(L) = -10601.962, IC = 22726.289
	2 rate classes
	Node: mixtureTree.Node282
	Length parameter = 0.05502832073775229
	Class 1
		omega = 0.000
		weight = 0.997
	Class 2
		omega = 72.614
		weight = 0.003

[PHASE 1] Branch Node9 log(L) = -10602.924, IC = 22728.214
	2 rate classes
	Node: mixtureTree.Node9
	Length parameter = 0.0546658346484175
	Class 1
		omega = 0.003
		weight = 0.905
	Class 2
		omega = 0.478
		weight = 0.095

[PHASE 1] Branch Node18 log(L) = -10602.681, IC = 22727.727
	2 rate classes
	Node: mixtureTree.Node18
	Length parameter = 0.04645884404965894
	Class 1
		omega = 0.000
		weight = 0.990
	Class 2
		omega = 16.242
		weight = 0.010

[PHASE 1] Branch Sericostachys_scandens_C3 log(L) = -10602.918, IC = 22728.202
	2 rate classes
	Node: mixtureTree.Sericostachys_scandens_C3
	Length parameter = 0.03704424551800218
	Class 1
		omega = 0.198
		weight = 0.751
	Class 2
		omega = 0.249
		weight = 0.249

[PHASE 1] Branch Gomphrena_elegans_C3 log(L) = -10602.918, IC = 22728.202
	2 rate classes
	Node: mixtureTree.Gomphrena_elegans_C3
	Length parameter = 0.06299741754282037
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Allenrolfea_occidentalis_C3 log(L) = -10590.596, IC = 22703.557
	2 rate classes
	Node: mixtureTree.Allenrolfea_occidentalis_C3
	Length parameter = 0.0179234042671354
	Class 1
		omega = 0.000
		weight = 0.993
	Class 2
		omega = 376.452
		weight = 0.007

[PHASE 1] Branch Allenrolfea_occidentalis_C3 log(L) = -10590.59388365408, IC = 22707.62937425274
	3 rate classes
	Node: mixtureTree.Allenrolfea_occidentalis_C3
	Length parameter = 0.01747931622456654
	Class 1
		omega = 0.000
		weight = 0.993
	Class 2
		omega = 0.000
		weight = 0.000
	Class 3
		omega = 394.756
		weight = 0.007

[PHASE 1] Branch Node97 log(L) = -10590.596, IC = 22707.633
	2 rate classes
	Node: mixtureTree.Node97
	Length parameter = 0.03659041464393612
	Class 1
		omega = 0.199
		weight = 0.951
	Class 2
		omega = 0.249
		weight = 0.049

[PHASE 1] Branch Node263 log(L) = -10590.596, IC = 22707.633
	2 rate classes
	Node: mixtureTree.Node263
	Length parameter = 0.05737716400435247
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node289 log(L) = -10590.596, IC = 22707.633
	2 rate classes
	Node: mixtureTree.Node289
	Length parameter = 0.05732308280666365
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node287 log(L) = -10583.562, IC = 22693.566
	2 rate classes
	Node: mixtureTree.Node287
	Length parameter = 0.01993353926377734
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 1466.224
		weight = 0.005

[PHASE 1] Branch Node287 log(L) = -10583.5874700493, IC = 22697.69337449938
	3 rate classes
	Node: mixtureTree.Node287
	Length parameter = 0.01825994321461437
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 0.000
		weight = 0.000
	Class 3
		omega = 2091.576
		weight = 0.005

[PHASE 1] Branch Girgensohnia_oppositiflora_C4 log(L) = -10583.562, IC = 22697.642
	2 rate classes
	Node: mixtureTree.Girgensohnia_oppositiflora_C4
	Length parameter = 0.05646218923045186
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Salsola_foliosa_C4 log(L) = -10583.562, IC = 22697.642
	2 rate classes
	Node: mixtureTree.Salsola_foliosa_C4
	Length parameter = 0.05638669663032261
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Chenopodium_coronopus_C3 log(L) = -10581.495, IC = 22693.509
	2 rate classes
	Node: mixtureTree.Chenopodium_coronopus_C3
	Length parameter = 0.03799824100721418
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 114.159
		weight = 0.005

[PHASE 1] Branch Chenopodium_coronopus_C3 log(L) = -10581.4952808539, IC = 22697.58602933008
	3 rate classes
	Node: mixtureTree.Chenopodium_coronopus_C3
	Length parameter = 0.03785784351492109
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 0.500
		weight = 0.000
	Class 3
		omega = 116.158
		weight = 0.005

[PHASE 1] Branch Suaeda_microphylla_C4 log(L) = -10581.362, IC = 22697.319
	2 rate classes
	Node: mixtureTree.Suaeda_microphylla_C4
	Length parameter = 0.02908734346741552
	Class 1
		omega = 0.033
		weight = 0.987
	Class 2
		omega = 25.753
		weight = 0.013

[PHASE 1] Branch Pandiaka_angustifolia_C3 log(L) = -10581.495, IC = 22697.586
	2 rate classes
	Node: mixtureTree.Pandiaka_angustifolia_C3
	Length parameter = 0.0556076370725864
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node20 log(L) = -10581.495, IC = 22697.586
	2 rate classes
	Node: mixtureTree.Node20
	Length parameter = 0.0555446937244331
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node171 log(L) = -10581.495, IC = 22697.586
	2 rate classes
	Node: mixtureTree.Node171
	Length parameter = 0.05534047016752533
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node8 log(L) = -10581.495, IC = 22697.586
	2 rate classes
	Node: mixtureTree.Node8
	Length parameter = 0.05493638645785068
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Halogeton_glomeratus_C4 log(L) = -10581.497, IC = 22697.590
	2 rate classes
	Node: mixtureTree.Halogeton_glomeratus_C4
	Length parameter = 0.03723544173669632
	Class 1
		omega = 0.010
		weight = 0.451
	Class 2
		omega = 0.247
		weight = 0.549

[PHASE 1] Branch Node247 log(L) = -10581.496, IC = 22697.587
	2 rate classes
	Node: mixtureTree.Node247
	Length parameter = 0.03684858812244218
	Class 1
		omega = 0.008
		weight = 0.450
	Class 2
		omega = 0.249
		weight = 0.550

[PHASE 1] Branch Halosarcia_indica_C4 log(L) = -10581.497, IC = 22697.589
	2 rate classes
	Node: mixtureTree.Halosarcia_indica_C4
	Length parameter = 0.03695928719381101
	Class 1
		omega = 0.032
		weight = 0.497
	Class 2
		omega = 0.248
		weight = 0.503

[PHASE 1] Branch Beta_vulgaris_C3 log(L) = -10581.498, IC = 22697.591
	2 rate classes
	Node: mixtureTree.Beta_vulgaris_C3
	Length parameter = 0.04568934191769954
	Class 1
		omega = 0.001
		weight = 0.749
	Class 2
		omega = 0.225
		weight = 0.251

[PHASE 1] Branch Cycloloma_atriplicifolium_C3 log(L) = -10581.497, IC = 22697.589
	2 rate classes
	Node: mixtureTree.Cycloloma_atriplicifolium_C3
	Length parameter = 0.03672541397853844
	Class 1
		omega = 0.036
		weight = 0.500
	Class 2
		omega = 0.249
		weight = 0.500

[PHASE 1] Branch Amaranthus_hypochondriacus_C4 log(L) = -10570.814, IC = 22676.223
	2 rate classes
	Node: mixtureTree.Amaranthus_hypochondriacus_C4
	Length parameter = 0.005697991478246647
	Class 1
		omega = 0.000
		weight = 0.992
	Class 2
		omega = 7484.057
		weight = 0.008

[PHASE 1] Branch Amaranthus_hypochondriacus_C4 log(L) = -10570.81397622116, IC = 22680.30065906694
	3 rate classes
	Node: mixtureTree.Amaranthus_hypochondriacus_C4
	Length parameter = 0.005676151073464238
	Class 1
		omega = 0.000
		weight = 0.992
	Class 2
		omega = 0.025
		weight = 0.000
	Class 3
		omega = 7535.468
		weight = 0.008

[PHASE 1] Branch Chenopodium_cristatum_C3 log(L) = -10570.812, IC = 22680.296
	2 rate classes
	Node: mixtureTree.Chenopodium_cristatum_C3
	Length parameter = 0.02734222310107593
	Class 1
		omega = 0.198
		weight = 0.951
	Class 2
		omega = 2.015
		weight = 0.049

[PHASE 1] Branch Node52 log(L) = -10570.814, IC = 22680.301
	2 rate classes
	Node: mixtureTree.Node52
	Length parameter = 0.05360347099934533
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Chenopodium_foliosum_C3 log(L) = -10566.844, IC = 22672.361
	2 rate classes
	Node: mixtureTree.Chenopodium_foliosum_C3
	Length parameter = 0.01811901946854946
	Class 1
		omega = 0.030
		weight = 0.990
	Class 2
		omega = 81.396
		weight = 0.010

[PHASE 1] Branch Chenopodium_foliosum_C3 log(L) = -10566.84356210569, IC = 22676.43727563475
	3 rate classes
	Node: mixtureTree.Chenopodium_foliosum_C3
	Length parameter = 0.01842033636044004
	Class 1
		omega = 0.037
		weight = 0.990
	Class 2
		omega = 1.000
		weight = 0.000
	Class 3
		omega = 81.007
		weight = 0.009

[PHASE 1] Branch Node2 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node2
	Length parameter = 0.0182660159543502
	Class 1
		omega = 0.600
		weight = 0.712
	Class 2
		omega = 0.500
		weight = 0.288

[PHASE 1] Branch Aphanisma_blitoides_C3 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Aphanisma_blitoides_C3
	Length parameter = 0.02093085672157754
	Class 1
		omega = 0.401
		weight = 0.951
	Class 2
		omega = 0.494
		weight = 0.049

[PHASE 1] Branch Node128 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node128
	Length parameter = 0.04847578971557484
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Halopeplis_amplexicaulis_C3 log(L) = -10566.846, IC = 22676.442
	2 rate classes
	Node: mixtureTree.Halopeplis_amplexicaulis_C3
	Length parameter = 0.03809822838749717
	Class 1
		omega = 0.002
		weight = 0.748
	Class 2
		omega = 0.266
		weight = 0.252

[PHASE 1] Branch Bassia_dasyphylla_C3 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Bassia_dasyphylla_C3
	Length parameter = 0.04657312790041754
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node226 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node226
	Length parameter = 0.04604718509314331
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Salsola_implicata_C4 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Salsola_implicata_C4
	Length parameter = 0.04585128814806844
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Kalidium_cuspidatum_C3 log(L) = -10566.851, IC = 22676.453
	2 rate classes
	Node: mixtureTree.Kalidium_cuspidatum_C3
	Length parameter = 0.02824921741485958
	Class 1
		omega = 0.010
		weight = 0.755
	Class 2
		omega = 0.731
		weight = 0.245

[PHASE 1] Branch Node185 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node185
	Length parameter = 0.04561380603023524
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Pupalia_lappacea_C3 log(L) = -10566.851, IC = 22676.452
	2 rate classes
	Node: mixtureTree.Pupalia_lappacea_C3
	Length parameter = 0.03670328787656972
	Class 1
		omega = 0.004
		weight = 0.907
	Class 2
		omega = 0.728
		weight = 0.093

[PHASE 1] Branch Node3 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node3
	Length parameter = 0.02798563921375173
	Class 1
		omega = 0.185
		weight = 1.000
	Class 2
		omega = 0.010
		weight = 0.000

[PHASE 1] Branch Micromonolepis_pusilla_C3 log(L) = -10566.850, IC = 22676.451
	2 rate classes
	Node: mixtureTree.Micromonolepis_pusilla_C3
	Length parameter = 0.0364678120674316
	Class 1
		omega = 0.002
		weight = 0.898
	Class 2
		omega = 0.687
		weight = 0.102

[PHASE 1] Branch Chenopodium_botrys_C3 log(L) = -10566.850, IC = 22676.450
	2 rate classes
	Node: mixtureTree.Chenopodium_botrys_C3
	Length parameter = 0.03631767955438011
	Class 1
		omega = 0.002
		weight = 0.901
	Class 2
		omega = 0.721
		weight = 0.099

[PHASE 1] Branch Manochlamys_albicans_C3 log(L) = -10566.845, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Manochlamys_albicans_C3
	Length parameter = 0.02719147506311788
	Class 1
		omega = 0.181
		weight = 0.980
	Class 2
		omega = 0.642
		weight = 0.020

[PHASE 1] Branch Kochia_americana_C3 log(L) = -10566.846, IC = 22676.443
	2 rate classes
	Node: mixtureTree.Kochia_americana_C3
	Length parameter = 0.009212050754063669
	Class 1
		omega = 0.866
		weight = 0.760
	Class 2
		omega = 1.947
		weight = 0.240

[PHASE 1] Branch Bassia_sedoides_C4 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Bassia_sedoides_C4
	Length parameter = 0.04416443990380005
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node107 log(L) = -10566.850, IC = 22676.449
	2 rate classes
	Node: mixtureTree.Node107
	Length parameter = 0.03472410185405509
	Class 1
		omega = 0.002
		weight = 0.899
	Class 2
		omega = 0.741
		weight = 0.101

[PHASE 1] Branch Node178 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node178
	Length parameter = 0.04258001408733701
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Salsola_affinis_C4 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Salsola_affinis_C4
	Length parameter = 0.04235956048575402
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node32 log(L) = -10566.462, IC = 22675.674
	2 rate classes
	Node: mixtureTree.Node32
	Length parameter = 0.02483749909814845
	Class 1
		omega = 0.000
		weight = 0.992
	Class 2
		omega = 43.454
		weight = 0.008

[PHASE 1] Branch Node24 log(L) = -10566.849, IC = 22676.449
	2 rate classes
	Node: mixtureTree.Node24
	Length parameter = 0.0322020703650869
	Class 1
		omega = 0.009
		weight = 0.899
	Class 2
		omega = 0.735
		weight = 0.101

[PHASE 1] Branch Node57 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node57
	Length parameter = 0.01418865021131449
	Class 1
		omega = 0.600
		weight = 0.500
	Class 2
		omega = 0.501
		weight = 0.500

[PHASE 1] Branch Noaea_mucronata_C4 log(L) = -10565.708, IC = 22674.165
	2 rate classes
	Node: mixtureTree.Noaea_mucronata_C4
	Length parameter = 0.03012183044971056
	Class 1
		omega = 0.000
		weight = 0.998
	Class 2
		omega = 271.661
		weight = 0.002

[PHASE 1] Branch Halothamnus_bottae_C4 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Halothamnus_bottae_C4
	Length parameter = 0.03809915436663018
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Suaeda_crassifolia_C3 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Suaeda_crassifolia_C3
	Length parameter = 0.03789812139400579
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node267 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node267
	Length parameter = 0.03777951932982124
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node35 log(L) = -10565.901, IC = 22674.552
	2 rate classes
	Node: mixtureTree.Node35
	Length parameter = 0.02917015894792748
	Class 1
		omega = 0.000
		weight = 0.997
	Class 2
		omega = 118.740
		weight = 0.003

[PHASE 1] Branch Kalidium_caspicum_C3 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Kalidium_caspicum_C3
	Length parameter = 0.03762353940363406
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node157 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node157
	Length parameter = 0.03751920501057279
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node215 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node215
	Length parameter = 0.03728989909585852
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Halogeton_arachnoideus_C4 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Halogeton_arachnoideus_C4
	Length parameter = 0.03713636162675662
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Sarcocornia_utahensis_C3 log(L) = -10566.849, IC = 22676.449
	2 rate classes
	Node: mixtureTree.Sarcocornia_utahensis_C3
	Length parameter = 0.02811739174542047
	Class 1
		omega = 0.005
		weight = 0.907
	Class 2
		omega = 0.968
		weight = 0.093

[PHASE 1] Branch Nototrichium_humile_C3 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Nototrichium_humile_C3
	Length parameter = 0.03658463363495303
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Atriplex_glauca_C4 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Atriplex_glauca_C4
	Length parameter = 0.03655634849854596
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Nitrophila_occidentalis_C3 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Nitrophila_occidentalis_C3
	Length parameter = 0.03637715656467602
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Bassia_diffusa_C3 log(L) = -10566.850, IC = 22676.451
	2 rate classes
	Node: mixtureTree.Bassia_diffusa_C3
	Length parameter = 0.02746648414052186
	Class 1
		omega = 0.003
		weight = 0.898
	Class 2
		omega = 0.916
		weight = 0.102

[PHASE 1] Branch Suaeda_physophora_C3 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Suaeda_physophora_C3
	Length parameter = 0.03634188470032299
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Suaeda_maritima_C3 log(L) = -10566.759, IC = 22676.268
	2 rate classes
	Node: mixtureTree.Suaeda_maritima_C3
	Length parameter = 0.009928071362814308
	Class 1
		omega = 0.000
		weight = 0.978
	Class 2
		omega = 43.331
		weight = 0.022

[PHASE 1] Branch Atriplex_centralasiatica_C4 log(L) = -10566.849, IC = 22676.449
	2 rate classes
	Node: mixtureTree.Atriplex_centralasiatica_C4
	Length parameter = 0.02710983470829505
	Class 1
		omega = 0.002
		weight = 0.901
	Class 2
		omega = 0.966
		weight = 0.099

[PHASE 1] Branch Node117 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node117
	Length parameter = 0.02710181310481399
	Class 1
		omega = 0.000
		weight = 0.951
	Class 2
		omega = 1.999
		weight = 0.049

[PHASE 1] Branch Node33 log(L) = -10566.845, IC = 22676.440
	2 rate classes
	Node: mixtureTree.Node33
	Length parameter = 0.02476363957612442
	Class 1
		omega = 0.014
		weight = 0.498
	Class 2
		omega = 0.248
		weight = 0.502

[PHASE 1] Branch Node257 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Node257
	Length parameter = 0.009351124036696317
	Class 1
		omega = 0.801
		weight = 0.842
	Class 2
		omega = 0.998
		weight = 0.158

[PHASE 1] Branch Iresine_palmeri_C3 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Iresine_palmeri_C3
	Length parameter = 0.009169616549783962
	Class 1
		omega = 0.800
		weight = 0.748
	Class 2
		omega = 0.998
		weight = 0.252

[PHASE 1] Branch Chenopodium_sanctaeclarae_C3 log(L) = -10566.844, IC = 22676.439
	2 rate classes
	Node: mixtureTree.Chenopodium_sanctaeclarae_C3
	Length parameter = 0.009148187978680151
	Class 1
		omega = 0.802
		weight = 0.751
	Class 2
		omega = 1.006
		weight = 0.249

[PHASE 1] Branch Node84 log(L) = -10566.842, IC = 22676.434
	2 rate classes
	Node: mixtureTree.Node84
	Length parameter = 0.02573785288330722
	Class 1
		omega = 0.009
		weight = 0.501
	Class 2
		omega = 0.243
		weight = 0.499

[PHASE 1] Branch Node7 log(L) = -10556.549, IC = 22655.847
	2 rate classes
	Node: mixtureTree.Node7
	Length parameter = 0.00383295959816971
	Class 1
		omega = 0.353
		weight = 0.996
	Class 2
		omega = 10000.000
		weight = 0.004

[PHASE 1] Branch Node7 log(L) = -10556.54161533127, IC = 22659.9110326967
	3 rate classes
	Node: mixtureTree.Node7
	Length parameter = 0.003914085779737916
	Class 1
		omega = 0.383
		weight = 0.996
	Class 2
		omega = 0.000
		weight = 0.000
	Class 3
		omega = 10000.000
		weight = 0.003

[PHASE 1] Branch Node119 log(L) = -10551.542, IC = 22649.913
	2 rate classes
	Node: mixtureTree.Node119
	Length parameter = 0.008795759495479201
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 332.129
		weight = 0.005

[PHASE 1] Branch Node119 log(L) = -10551.58801573573, IC = 22654.08168994402
	3 rate classes
	Node: mixtureTree.Node119
	Length parameter = 0.008099015742706059
	Class 1
		omega = 0.116
		weight = 0.994
	Class 2
		omega = 0.849
		weight = 0.002
	Class 3
		omega = 716.940
		weight = 0.004

[PHASE 1] Branch Node278 log(L) = -10551.549, IC = 22654.004
	2 rate classes
	Node: mixtureTree.Node278
	Length parameter = 0.02565542320036576
	Class 1
		omega = 0.003
		weight = 0.901
	Class 2
		omega = 0.994
		weight = 0.099

[PHASE 1] Branch Pseudoplantago_friesii_C3 log(L) = -10551.543, IC = 22653.992
	2 rate classes
	Node: mixtureTree.Pseudoplantago_friesii_C3
	Length parameter = 0.0152944351552927
	Class 1
		omega = 0.207
		weight = 0.539
	Class 2
		omega = 0.494
		weight = 0.461

[PHASE 1] Branch Node51 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node51
	Length parameter = 0.03198304825263524
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node42 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node42
	Length parameter = 0.03117567427108368
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node189 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node189
	Length parameter = 0.03050478730775424
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node30 log(L) = -10551.542, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Node30
	Length parameter = 0.02159877113527032
	Class 1
		omega = 0.000
		weight = 0.511
	Class 2
		omega = 0.246
		weight = 0.489

[PHASE 1] Branch Node131 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node131
	Length parameter = 0.02799752241303818
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Monolepis_nuttalliana_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Monolepis_nuttalliana_C3
	Length parameter = 0.02782920642135606
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Anabasis_truncata_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Anabasis_truncata_C4
	Length parameter = 0.02773554443934785
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node271 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Node271
	Length parameter = 0.01900925593374243
	Class 1
		omega = 0.023
		weight = 0.499
	Class 2
		omega = 0.249
		weight = 0.501

[PHASE 1] Branch Node136 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Node136
	Length parameter = 0.01030516660499374
	Class 1
		omega = 0.598
		weight = 0.751
	Class 2
		omega = 0.214
		weight = 0.249

[PHASE 1] Branch Node141 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node141
	Length parameter = 0.02765255367603319
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Salsola_genistoides_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_genistoides_C3
	Length parameter = 0.02760053054132446
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Gomphrena_haageana_C4 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Gomphrena_haageana_C4
	Length parameter = 0.01858500530605428
	Class 1
		omega = 0.007
		weight = 0.450
	Class 2
		omega = 0.249
		weight = 0.550

[PHASE 1] Branch Node309 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node309
	Length parameter = 0.02736610831423659
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Atriplex_coriacea_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Atriplex_coriacea_C4
	Length parameter = 0.02720288115782833
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Chenoleoides_tomentosa_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Chenoleoides_tomentosa_C4
	Length parameter = 0.02716114952414917
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Hemichroa_diandra_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Hemichroa_diandra_C3
	Length parameter = 0.02704914841608552
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node315 log(L) = -10550.602, IC = 22652.110
	2 rate classes
	Node: mixtureTree.Node315
	Length parameter = 0.01830036227964576
	Class 1
		omega = 0.000
		weight = 0.997
	Class 2
		omega = 184.131
		weight = 0.003

[PHASE 1] Branch Chenopodium_bonushenricus_C3 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Chenopodium_bonushenricus_C3
	Length parameter = 0.01815199460990723
	Class 1
		omega = 0.014
		weight = 0.450
	Class 2
		omega = 0.249
		weight = 0.550

[PHASE 1] Branch Atriplex_rosea_C4 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Atriplex_rosea_C4
	Length parameter = 0.0180938355109875
	Class 1
		omega = 0.038
		weight = 0.499
	Class 2
		omega = 0.249
		weight = 0.501

[PHASE 1] Branch Node268 log(L) = -10551.542, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Node268
	Length parameter = 0.009275504364167443
	Class 1
		omega = 0.599
		weight = 0.901
	Class 2
		omega = 0.196
		weight = 0.099

[PHASE 1] Branch Node92 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Node92
	Length parameter = 0.009210043121311681
	Class 1
		omega = 0.599
		weight = 0.899
	Class 2
		omega = 0.262
		weight = 0.101

[PHASE 1] Branch Sclerolaena_obliquicuspis_C3 log(L) = -10551.542, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Sclerolaena_obliquicuspis_C3
	Length parameter = 0.009196557758269271
	Class 1
		omega = 0.600
		weight = 0.898
	Class 2
		omega = 0.250
		weight = 0.102

[PHASE 1] Branch Node79 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node79
	Length parameter = 0.009120219962165952
	Class 1
		omega = 0.600
		weight = 0.696
	Class 2
		omega = 0.501
		weight = 0.304

[PHASE 1] Branch Node155 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node155
	Length parameter = 0.009008465344491838
	Class 1
		omega = 0.600
		weight = 0.749
	Class 2
		omega = 0.501
		weight = 0.251

[PHASE 1] Branch Celosia_trigyna_C3 log(L) = -10551.577, IC = 22654.060
	2 rate classes
	Node: mixtureTree.Celosia_trigyna_C3
	Length parameter = 0.0003520362712119332
	Class 1
		omega = 0.999
		weight = 0.000
	Class 2
		omega = 21.989
		weight = 1.000

[PHASE 1] Branch Node170 log(L) = -10552.268, IC = 22655.442
	2 rate classes
	Node: mixtureTree.Node170
	Length parameter = 0.006116607539582485
	Class 1
		omega = 1.000
		weight = 1.000
	Class 2
		omega = 0.322
		weight = 0.000

[PHASE 1] Branch Node129 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Node129
	Length parameter = 0.01745032548547231
	Class 1
		omega = 0.025
		weight = 0.450
	Class 2
		omega = 0.249
		weight = 0.550

[PHASE 1] Branch Node17 log(L) = -10551.254, IC = 22653.413
	2 rate classes
	Node: mixtureTree.Node17
	Length parameter = 0.02003650613914087
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Dysphania_glomulifera_C3 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Dysphania_glomulifera_C3
	Length parameter = 0.004774644558341238
	Class 1
		omega = 0.801
		weight = 0.752
	Class 2
		omega = 1.987
		weight = 0.248

[PHASE 1] Branch Node113 log(L) = -10551.538, IC = 22653.982
	2 rate classes
	Node: mixtureTree.Node113
	Length parameter = 0.01412177432772065
	Class 1
		omega = 0.183
		weight = 0.981
	Class 2
		omega = 0.240
		weight = 0.019

[PHASE 1] Branch Node95 log(L) = -10551.791, IC = 22654.488
	2 rate classes
	Node: mixtureTree.Node95
	Length parameter = 0.005540857767334477
	Class 1
		omega = 1.000
		weight = 1.000
	Class 2
		omega = 0.000
		weight = 0.000

[PHASE 1] Branch Node41 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node41
	Length parameter = 0.02042998408816982
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node116 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node116
	Length parameter = 0.01955270529494645
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node250 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node250
	Length parameter = 0.01904222613816323
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node61 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node61
	Length parameter = 0.01884024378010066
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Sclerostegia_moniliformis_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Sclerostegia_moniliformis_C3
	Length parameter = 0.01876505058454522
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node190 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node190
	Length parameter = 0.01873306340510092
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Alternanthera_pungens_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Alternanthera_pungens_C4
	Length parameter = 0.01865987601448919
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node202 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node202
	Length parameter = 0.01861012972591717
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Arthrocnemum_macrostachyum_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Arthrocnemum_macrostachyum_C3
	Length parameter = 0.01855014282324864
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node124 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node124
	Length parameter = 0.01853396365262698
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node206 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node206
	Length parameter = 0.01851644001440312
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Climacoptera_brachiata_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Climacoptera_brachiata_C4
	Length parameter = 0.01849221024237934
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node253 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node253
	Length parameter = 0.01848817268650534
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node161 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node161
	Length parameter = 0.01848203448985271
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node209 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node209
	Length parameter = 0.01846697666560802
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node198 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node198
	Length parameter = 0.01846780899162425
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Salsola_laricifolia_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_laricifolia_C3
	Length parameter = 0.01843057893031086
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Anabasis_aphylla_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Anabasis_aphylla_C4
	Length parameter = 0.01840760576266593
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node322 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node322
	Length parameter = 0.01832862538815805
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node123 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node123
	Length parameter = 0.01837204774072892
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Rhaphidophyton_regelii_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Rhaphidophyton_regelii_C3
	Length parameter = 0.01837439792074241
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node73 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node73
	Length parameter = 0.01829114608679703
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node294 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node294
	Length parameter = 0.01826080978581268
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node331 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node331
	Length parameter = 0.01823178317794987
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node6 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node6
	Length parameter = 0.01810799158069246
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Atriplex_aucherii_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Atriplex_aucherii_C3
	Length parameter = 0.01809770508676745
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node293 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Node293
	Length parameter = 0.009327920330934349
	Class 1
		omega = 0.203
		weight = 0.751
	Class 2
		omega = 0.499
		weight = 0.249

[PHASE 1] Branch Node204 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Node204
	Length parameter = 0.009320473065826897
	Class 1
		omega = 0.202
		weight = 0.751
	Class 2
		omega = 0.508
		weight = 0.249

[PHASE 1] Branch Haloxylon_tamariscifolium_C4 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Haloxylon_tamariscifolium_C4
	Length parameter = 0.009285521987575464
	Class 1
		omega = 0.204
		weight = 0.751
	Class 2
		omega = 0.504
		weight = 0.249

[PHASE 1] Branch Anthochlamys_multinervis_C3 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Anthochlamys_multinervis_C3
	Length parameter = 0.009299928484899722
	Class 1
		omega = 0.200
		weight = 0.736
	Class 2
		omega = 0.498
		weight = 0.264

[PHASE 1] Branch Calicorema_capitata_C3 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Calicorema_capitata_C3
	Length parameter = 0.009219479809494649
	Class 1
		omega = 0.201
		weight = 0.900
	Class 2
		omega = 1.013
		weight = 0.100

[PHASE 1] Branch Salsola_arbuscula_C4 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Salsola_arbuscula_C4
	Length parameter = 0.00917927863509424
	Class 1
		omega = 0.201
		weight = 0.898
	Class 2
		omega = 0.996
		weight = 0.102

[PHASE 1] Branch Chenopodium_acuminatum_C3 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Chenopodium_acuminatum_C3
	Length parameter = 0.009101498601511517
	Class 1
		omega = 0.214
		weight = 0.752
	Class 2
		omega = 0.500
		weight = 0.248

[PHASE 1] Branch Node175 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node175
	Length parameter = 0.01782866167081703
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Atriplex_lampa_C4 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Atriplex_lampa_C4
	Length parameter = 0.00918212609116398
	Class 1
		omega = 0.203
		weight = 0.900
	Class 2
		omega = 0.996
		weight = 0.100

[PHASE 1] Branch Node228 log(L) = -10551.543, IC = 22653.991
	2 rate classes
	Node: mixtureTree.Node228
	Length parameter = 0.009078647867234191
	Class 1
		omega = 0.213
		weight = 0.747
	Class 2
		omega = 0.497
		weight = 0.253

[PHASE 1] Branch Atriplex_halimus_C4 log(L) = -10550.398, IC = 22651.701
	2 rate classes
	Node: mixtureTree.Atriplex_halimus_C4
	Length parameter = 0.008703616195651099
	Class 1
		omega = 0.000
		weight = 0.998
	Class 2
		omega = 945.638
		weight = 0.002

[PHASE 1] Branch Beta_nana_C3 log(L) = -10551.564, IC = 22654.035
	2 rate classes
	Node: mixtureTree.Beta_nana_C3
	Length parameter = 8.405825991459837e-06
	Class 1
		omega = 1.000
		weight = 0.925
	Class 2
		omega = 8464.157
		weight = 0.075

[PHASE 1] Branch Pachycornia_triandra_C3 log(L) = -10551.563, IC = 22654.031
	2 rate classes
	Node: mixtureTree.Pachycornia_triandra_C3
	Length parameter = 0.0009721071213501511
	Class 1
		omega = 0.210
		weight = 0.000
	Class 2
		omega = 5.283
		weight = 1.000

[PHASE 1] Branch Node316 log(L) = -10551.548, IC = 22654.001
	2 rate classes
	Node: mixtureTree.Node316
	Length parameter = 8.446867482953243e-06
	Class 1
		omega = 0.000
		weight = 0.727
	Class 2
		omega = 2268.860
		weight = 0.273

[PHASE 1] Branch Charpentiera_obovata_C3 log(L) = -10551.544, IC = 22653.994
	2 rate classes
	Node: mixtureTree.Charpentiera_obovata_C3
	Length parameter = 1.499520134049619e-05
	Class 1
		omega = 0.001
		weight = 0.000
	Class 2
		omega = 345.859
		weight = 1.000

[PHASE 1] Branch Node251 log(L) = -10551.543, IC = 22653.993
	2 rate classes
	Node: mixtureTree.Node251
	Length parameter = 1.035066761752277e-05
	Class 1
		omega = 0.999
		weight = 0.000
	Class 2
		omega = 501.036
		weight = 1.000

[PHASE 1] Branch Node221 log(L) = -10551.566, IC = 22654.038
	2 rate classes
	Node: mixtureTree.Node221
	Length parameter = 0.0002242301587081058
	Class 1
		omega = 0.959
		weight = 0.000
	Class 2
		omega = 22.867
		weight = 1.000

[PHASE 1] Branch Tecticornia_disarticulata_C3 log(L) = -10551.565, IC = 22654.036
	2 rate classes
	Node: mixtureTree.Tecticornia_disarticulata_C3
	Length parameter = 0.0001784611784279703
	Class 1
		omega = 1.000
		weight = 0.630
	Class 2
		omega = 77.275
		weight = 0.370

[PHASE 1] Branch Node326 log(L) = -10551.566, IC = 22654.037
	2 rate classes
	Node: mixtureTree.Node326
	Length parameter = 0.0002093855582093974
	Class 1
		omega = 1.000
		weight = 0.000
	Class 2
		omega = 24.484
		weight = 1.000

[PHASE 1] Branch Node182 log(L) = -10551.544, IC = 22653.993
	2 rate classes
	Node: mixtureTree.Node182
	Length parameter = 0.008742374289693685
	Class 1
		omega = 0.203
		weight = 0.950
	Class 2
		omega = 2.047
		weight = 0.050

[PHASE 1] Branch Node130 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node130
	Length parameter = 0.0170771152088186
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node16 log(L) = -10551.541, IC = 22653.988
	2 rate classes
	Node: mixtureTree.Node16
	Length parameter = 0.006759619554526433
	Class 1
		omega = 0.400
		weight = 0.861
	Class 2
		omega = 0.285
		weight = 0.139

[PHASE 1] Branch Salsola_rosacea_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_rosacea_C4
	Length parameter = 0.01585733203665219
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node112 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node112
	Length parameter = 0.01488213155857851
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node43 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node43
	Length parameter = 0.01300022569750953
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node148 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node148
	Length parameter = 0.01197426442114207
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node137 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node137
	Length parameter = 0.0108082488802091
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node181 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node181
	Length parameter = 0.01005118841736898
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Halostachys_belangeriana_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Halostachys_belangeriana_C3
	Length parameter = 0.009414119316681645
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node65 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node65
	Length parameter = 0.009327999279953944
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node210 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node210
	Length parameter = 0.009327025587868741
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node262 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node262
	Length parameter = 0.009295243840094418
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node256 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node256
	Length parameter = 0.009298242865587697
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Salsola_micranthera_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_micranthera_C4
	Length parameter = 0.009260119534957511
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Anabasis_eriopoda_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Anabasis_eriopoda_C4
	Length parameter = 0.009251368451012279
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node199 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node199
	Length parameter = 0.009236407114928269
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node59 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node59
	Length parameter = 0.009223947326036371
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Achyranthes_aspera_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Achyranthes_aspera_C3
	Length parameter = 0.009225533445343381
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Amaranthus_tricolor_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Amaranthus_tricolor_C4
	Length parameter = 0.009213973432067986
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Roycea_divaricata_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Roycea_divaricata_C3
	Length parameter = 0.009209072421131684
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Anabasis_elatior_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Anabasis_elatior_C4
	Length parameter = 0.009202419270277332
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Node186 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node186
	Length parameter = 0.009197781106431239
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Maireana_brevifolia_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Maireana_brevifolia_C3
	Length parameter = 0.009193244221657605
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Blutaparon_vermiculare_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Blutaparon_vermiculare_C4
	Length parameter = 0.009137726596163987
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Salsola_chinghaiensis_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_chinghaiensis_C4
	Length parameter = 0.009131936509333364
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node342 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node342
	Length parameter = 0.009128987173887361
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node304 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node304
	Length parameter = 0.009116838978342418
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node231 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node231
	Length parameter = 0.009114891565958324
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Atriplex_powellii_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Atriplex_powellii_C4
	Length parameter = 0.009112451890025627
	Class 1
		omega = 0.000
		weight = 0.981
	Class 2
		omega = 0.000
		weight = 0.019

[PHASE 1] Branch Salsola_kali_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_kali_C4
	Length parameter = 0.009096558377792921
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node49 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node49
	Length parameter = 0.009095473683801073
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node337 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node337
	Length parameter = 0.009094800621752362
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Atriplex_phyllostegia_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Atriplex_phyllostegia_C4
	Length parameter = 0.009089406004514973
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Atriplex_lentiformis_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Atriplex_lentiformis_C4
	Length parameter = 0.009084228815164576
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node249 log(L) = -10551.413, IC = 22653.732
	2 rate classes
	Node: mixtureTree.Node249
	Length parameter = 0.009074598572247199
	Class 1
		omega = 0.000
		weight = 0.755
	Class 2
		omega = 0.500
		weight = 0.245

[PHASE 1] Branch Node341 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node341
	Length parameter = 0.009072678886889014
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Atriplex_parryi_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Atriplex_parryi_C4
	Length parameter = 0.009063723584954456
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node327 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node327
	Length parameter = 0.009056088310345196
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Chenopodium_murale_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Chenopodium_murale_C3
	Length parameter = 0.009042106243817261
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node1 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node1
	Length parameter = 0.009039087878327056
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node15 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node15
	Length parameter = 0.009038785445112768
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Einadia_nutans_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Einadia_nutans_C3
	Length parameter = 0.009027896049607085
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.000
		weight = 0.020

[PHASE 1] Branch Node160 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node160
	Length parameter = 0.008960222288438745
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node22 log(L) = -10550.820, IC = 22652.547
	2 rate classes
	Node: mixtureTree.Node22
	Length parameter = 0.001711526437924026
	Class 1
		omega = 0.000
		weight = 0.997
	Class 2
		omega = 1466.370
		weight = 0.003

[PHASE 1] Branch Node31 log(L) = -10550.637, IC = 22652.179
	2 rate classes
	Node: mixtureTree.Node31
	Length parameter = 0.0003223889642164264
	Class 1
		omega = 0.000
		weight = 0.997
	Class 2
		omega = 10000.000
		weight = 0.003

[PHASE 1] Branch Gomphrena_serrata_C4 log(L) = -10551.544, IC = 22653.994
	2 rate classes
	Node: mixtureTree.Gomphrena_serrata_C4
	Length parameter = 1.450350700344416e-05
	Class 1
		omega = 1.000
		weight = 0.276
	Class 2
		omega = 247.043
		weight = 0.724

[PHASE 1] Branch Alternanthera_caracasana_C4 log(L) = -10551.567, IC = 22654.039
	2 rate classes
	Node: mixtureTree.Alternanthera_caracasana_C4
	Length parameter = 0.0001547293154959707
	Class 1
		omega = 1.000
		weight = 0.872
	Class 2
		omega = 125.588
		weight = 0.128

[PHASE 1] Branch Node343 log(L) = -10551.558, IC = 22654.022
	2 rate classes
	Node: mixtureTree.Node343
	Length parameter = 0.0001551439055046272
	Class 1
		omega = 1.000
		weight = 0.677
	Class 2
		omega = 49.926
		weight = 0.323

[PHASE 1] Branch Chenopodium_desertorum_C3 log(L) = -10551.795, IC = 22654.495
	2 rate classes
	Node: mixtureTree.Chenopodium_desertorum_C3
	Length parameter = 0.002014602843374134
	Class 1
		omega = 1.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Dissocarpus_paradoxus_C3 log(L) = -10551.560, IC = 22654.025
	2 rate classes
	Node: mixtureTree.Dissocarpus_paradoxus_C3
	Length parameter = 0.0001521220055488797
	Class 1
		omega = 1.000
		weight = 0.369
	Class 2
		omega = 25.971
		weight = 0.631

[PHASE 1] Branch Chenopodium_auricomum_C3 log(L) = -10551.795, IC = 22654.495
	2 rate classes
	Node: mixtureTree.Chenopodium_auricomum_C3
	Length parameter = 0.002014581794758196
	Class 1
		omega = 1.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Tecticornia_australasica_C3 log(L) = -10551.550, IC = 22654.006
	2 rate classes
	Node: mixtureTree.Tecticornia_australasica_C3
	Length parameter = 4.55099112139756e-05
	Class 1
		omega = 1.000
		weight = 0.869
	Class 2
		omega = 433.814
		weight = 0.131

[PHASE 1] Branch Node213 log(L) = -10551.559, IC = 22654.024
	2 rate classes
	Node: mixtureTree.Node213
	Length parameter = 0.0001219241848193095
	Class 1
		omega = 1.000
		weight = 0.843
	Class 2
		omega = 128.629
		weight = 0.157

[PHASE 1] Branch Atriplex_undulata_C4 log(L) = -10551.545, IC = 22653.995
	2 rate classes
	Node: mixtureTree.Atriplex_undulata_C4
	Length parameter = 2.199024355161806e-05
	Class 1
		omega = 0.000
		weight = 0.000
	Class 2
		omega = 117.606
		weight = 1.000

[PHASE 1] Branch Node328 log(L) = -10551.568, IC = 22654.041
	2 rate classes
	Node: mixtureTree.Node328
	Length parameter = 0.0002299011081784164
	Class 1
		omega = 0.249
		weight = 0.000
	Class 2
		omega = 11.398
		weight = 1.000

[PHASE 1] Branch Node165 log(L) = -10551.559, IC = 22654.024
	2 rate classes
	Node: mixtureTree.Node165
	Length parameter = 0.0001360056132725306
	Class 1
		omega = 1.000
		weight = 0.825
	Class 2
		omega = 104.980
		weight = 0.175

[PHASE 1] Branch Salsola_zaidamica_C4 log(L) = -10551.544, IC = 22653.995
	2 rate classes
	Node: mixtureTree.Salsola_zaidamica_C4
	Length parameter = 1.870494306238242e-05
	Class 1
		omega = 1.000
		weight = 0.056
	Class 2
		omega = 146.368
		weight = 0.944

[PHASE 1] Branch Node77 log(L) = -10551.789, IC = 22654.484
	2 rate classes
	Node: mixtureTree.Node77
	Length parameter = 0.002022381783734846
	Class 1
		omega = 1.000
		weight = 1.000
	Class 2
		omega = 0.261
		weight = 0.000

[PHASE 1] Branch Node163 log(L) = -10551.544, IC = 22653.995
	2 rate classes
	Node: mixtureTree.Node163
	Length parameter = 1.851794886105347e-05
	Class 1
		omega = 1.000
		weight = 0.055
	Class 2
		omega = 147.693
		weight = 0.945

[PHASE 1] Branch Node154 log(L) = -10551.560, IC = 22654.025
	2 rate classes
	Node: mixtureTree.Node154
	Length parameter = 0.0001576503909646042
	Class 1
		omega = 0.999
		weight = 0.000
	Class 2
		omega = 16.125
		weight = 1.000

[PHASE 1] Branch Node153 log(L) = -10551.545, IC = 22653.996
	2 rate classes
	Node: mixtureTree.Node153
	Length parameter = 2.386889557154895e-05
	Class 1
		omega = 0.905
		weight = 0.000
	Class 2
		omega = 108.012
		weight = 1.000

[PHASE 1] Branch Halimione_verrucifera_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Halimione_verrucifera_C3
	Length parameter = 0.008599581098889674
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node301 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node301
	Length parameter = 0.007413947563591138
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Node47 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node47
	Length parameter = 0.007384505679426467
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Hebanthe_occidentalis_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Hebanthe_occidentalis_C3
	Length parameter = 0.00294362874005881
	Class 1
		omega = 0.000
		weight = 1.000
	Class 2
		omega = 0.250
		weight = 0.000

[PHASE 1] Branch Atriplex_spongiosa_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Atriplex_spongiosa_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node188 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node188
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node144 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node144
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node121 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node121
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_arbusculiformis_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_arbusculiformis_C3
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node48 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node48
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Petrosimonia_squarrosa_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Petrosimonia_squarrosa_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_heptapotamica_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_heptapotamica_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node173 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node173
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node187 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node187
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node68 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node68
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node142 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node142
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_dshungarica_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_dshungarica_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_orientalis_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_orientalis_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Halimocnemis_villosa_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Halimocnemis_villosa_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_ferganica_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_ferganica_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Amaranthus_greggii_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Amaranthus_greggii_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node89 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node89
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_sukaczevii_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_sukaczevii_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node76 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node76
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Amaranthus_blitum_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Amaranthus_blitum_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Halimocnemis_karelinii_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Halimocnemis_karelinii_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node75 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node75
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Alternanthera_repens_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Alternanthera_repens_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Petrosimonia_glaucescens_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Petrosimonia_glaucescens_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node167 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node167
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node23 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node23
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Charpentiera_ovata_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Charpentiera_ovata_C3
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Climacoptera_lanata_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Climacoptera_lanata_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Anabasis_brevifolia_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Anabasis_brevifolia_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node306 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node306
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Chenopodium_frutescens_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Chenopodium_frutescens_C3
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Rhagodia_drummondi_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Rhagodia_drummondi_C3
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node305 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node305
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node308 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node308
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node260 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node260
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Kalidium_foliatum_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Kalidium_foliatum_C3
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Chenopodium_album_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Chenopodium_album_C3
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node273 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node273
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node319 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node319
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node325 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node325
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Atriplex_australasica_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Atriplex_australasica_C3
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node352 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node352
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Atriplex_patula_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Atriplex_patula_C3
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node349 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node349
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node332 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node332
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Atriplex_serenana_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Atriplex_serenana_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node329 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node329
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Cremnophyton_lanfrancoi_C3 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Cremnophyton_lanfrancoi_C3
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node336 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node336
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node151 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node151
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Iljinia_regelii_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Iljinia_regelii_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node218 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node218
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_komarovii_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_komarovii_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node197 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node197
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node219 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node219
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Anabasis_salsa_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Anabasis_salsa_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Haloxylon_ammodendron_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Haloxylon_ammodendron_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node211 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node211
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Haloxylon_persicum_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Haloxylon_persicum_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_ruthenica_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_ruthenica_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_paulsenii_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_paulsenii_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node242 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node242
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node230 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node230
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node240 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node240
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_pellucida_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_pellucida_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_collina_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_collina_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node236 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node236
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node235 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node235
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Salsola_praecox_C4 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Salsola_praecox_C4
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020

[PHASE 1] Branch Node233 log(L) = -10551.542, IC = 22653.990
	2 rate classes
	Node: mixtureTree.Node233
	Length parameter = 0
	Class 1
		omega = 0.000
		weight = 0.980
	Class 2
		omega = 0.250
		weight = 0.020


[INFERRED MODEL COMPLEXITY]
	mixtureTree.Halimione_pedunculata_C3 has 1 site rate classes
	mixtureTree.Halimione_verrucifera_C3 has 1 site rate classes
	mixtureTree.Node3 has 1 site rate classes
	mixtureTree.Axyris_prostrata_C3 has 1 site rate classes
	mixtureTree.Ceratocarpus_arenarius_C3 has 2 site rate classes
	mixtureTree.Krascheninnikovia_ceratoides_C3 has 1 site rate classes
	mixtureTree.Node12 has 1 site rate classes
	mixtureTree.Node10 has 2 site rate classes
	mixtureTree.Suckleya_suckleyana_C3 has 1 site rate classes
	mixtureTree.Cycloloma_atriplicifolium_C3 has 1 site rate classes
	mixtureTree.Chenopodium_cristatum_C3 has 1 site rate classes
	mixtureTree.Dysphania_glomulifera_C3 has 1 site rate classes
	mixtureTree.Node24 has 1 site rate classes
	mixtureTree.Chenopodium_ambrosioides_C3 has 1 site rate classes
	mixtureTree.Node23 has 1 site rate classes
	mixtureTree.Chenopodium_botrys_C3 has 1 site rate classes
	mixtureTree.Node22 has 1 site rate classes
	mixtureTree.Node20 has 1 site rate classes
	mixtureTree.Node18 has 1 site rate classes
	mixtureTree.Teloxys_aristata_C3 has 2 site rate classes
	mixtureTree.Node17 has 1 site rate classes
	mixtureTree.Hablitzia_tamnoides_C3 has 1 site rate classes
	mixtureTree.Aphanisma_blitoides_C3 has 1 site rate classes
	mixtureTree.Patellifolia_patellaris_C3 has 1 site rate classes
	mixtureTree.Node35 has 1 site rate classes
	mixtureTree.Node33 has 1 site rate classes
	mixtureTree.Beta_vulgaris_C3 has 1 site rate classes
	mixtureTree.Beta_nana_C3 has 1 site rate classes
	mixtureTree.Node38 has 2 site rate classes
	mixtureTree.Node32 has 1 site rate classes
	mixtureTree.Ptilotus_manglesii_C3 has 1 site rate classes
	mixtureTree.Iresine_palmeri_C3 has 1 site rate classes
	mixtureTree.Gomphrena_elegans_C3 has 1 site rate classes
	mixtureTree.Pseudoplantago_friesii_C3 has 1 site rate classes
	mixtureTree.Hebanthe_occidentalis_C3 has 1 site rate classes
	mixtureTree.Node54 has 1 site rate classes
	mixtureTree.Node52 has 1 site rate classes
	mixtureTree.Guilleminea_densa_C4 has 1 site rate classes
	mixtureTree.Gomphrena_serrata_C4 has 1 site rate classes
	mixtureTree.Gomphrena_haageana_C4 has 1 site rate classes
	mixtureTree.Node61 has 1 site rate classes
	mixtureTree.Node59 has 1 site rate classes
	mixtureTree.Blutaparon_vermiculare_C4 has 1 site rate classes
	mixtureTree.Node58 has 1 site rate classes
	mixtureTree.Alternanthera_pungens_C4 has 1 site rate classes
	mixtureTree.Alternanthera_caracasana_C4 has 1 site rate classes
	mixtureTree.Alternanthera_repens_C4 has 1 site rate classes
	mixtureTree.Node68 has 1 site rate classes
	mixtureTree.Node66 has 1 site rate classes
	mixtureTree.Tidestromia_lanuginosa_C4 has 1 site rate classes
	mixtureTree.Node65 has 1 site rate classes
	mixtureTree.Node57 has 1 site rate classes
	mixtureTree.Node51 has 1 site rate classes
	mixtureTree.Node49 has 1 site rate classes
	mixtureTree.Aerva_javanica_C4 has 1 site rate classes
	mixtureTree.Node48 has 1 site rate classes
	mixtureTree.Pupalia_lappacea_C3 has 1 site rate classes
	mixtureTree.Sericostachys_scandens_C3 has 1 site rate classes
	mixtureTree.Achyranthes_aspera_C3 has 1 site rate classes
	mixtureTree.Nototrichium_humile_C3 has 1 site rate classes
	mixtureTree.Node79 has 1 site rate classes
	mixtureTree.Node77 has 1 site rate classes
	mixtureTree.Pandiaka_angustifolia_C3 has 1 site rate classes
	mixtureTree.Node76 has 1 site rate classes
	mixtureTree.Calicorema_capitata_C3 has 1 site rate classes
	mixtureTree.Node75 has 1 site rate classes
	mixtureTree.Node73 has 1 site rate classes
	mixtureTree.Node47 has 1 site rate classes
	mixtureTree.Node45 has 2 site rate classes
	mixtureTree.Chamissoa_altissima_C3 has 1 site rate classes
	mixtureTree.Amaranthus_greggii_C4 has 1 site rate classes
	mixtureTree.Amaranthus_tricolor_C4 has 1 site rate classes
	mixtureTree.Node89 has 1 site rate classes
	mixtureTree.Amaranthus_blitum_C4 has 1 site rate classes
	mixtureTree.Amaranthus_hypochondriacus_C4 has 2 site rate classes
	mixtureTree.Node92 has 1 site rate classes
	mixtureTree.Node88 has 1 site rate classes
	mixtureTree.Node86 has 1 site rate classes
	mixtureTree.Deeringia_amaranthoides_C3 has 1 site rate classes
	mixtureTree.Hermbstaedtia_glauca_C3 has 2 site rate classes
	mixtureTree.Celosia_trigyna_C3 has 1 site rate classes
	mixtureTree.Celosia_argentea_C3 has 1 site rate classes
	mixtureTree.Node99 has 1 site rate classes
	mixtureTree.Node97 has 1 site rate classes
	mixtureTree.Node95 has 1 site rate classes
	mixtureTree.Node85 has 2 site rate classes
	mixtureTree.Charpentiera_ovata_C3 has 1 site rate classes
	mixtureTree.Charpentiera_obovata_C3 has 1 site rate classes
	mixtureTree.Node102 has 2 site rate classes
	mixtureTree.Node84 has 1 site rate classes
	mixtureTree.Node44 has 2 site rate classes
	mixtureTree.Bosea_yervamora_C3 has 1 site rate classes
	mixtureTree.Node43 has 1 site rate classes
	mixtureTree.Nitrophila_occidentalis_C3 has 1 site rate classes
	mixtureTree.Hemichroa_diandra_C3 has 1 site rate classes
	mixtureTree.Node107 has 1 site rate classes
	mixtureTree.Polycnemum_perenne_C3 has 1 site rate classes
	mixtureTree.Node106 has 1 site rate classes
	mixtureTree.Node42 has 1 site rate classes
	mixtureTree.Oreobliton_thesioides_C3 has 1 site rate classes
	mixtureTree.Node41 has 1 site rate classes
	mixtureTree.Node31 has 1 site rate classes
	mixtureTree.Halocharis_hispida_C4 has 1 site rate classes
	mixtureTree.Salsola_vermiculata_C4 has 1 site rate classes
	mixtureTree.Salsola_implicata_C4 has 1 site rate classes
	mixtureTree.Salsola_orientalis_C4 has 1 site rate classes
	mixtureTree.Salsola_dshungarica_C4 has 1 site rate classes
	mixtureTree.Node124 has 1 site rate classes
	mixtureTree.Salsola_micranthera_C4 has 1 site rate classes
	mixtureTree.Node123 has 1 site rate classes
	mixtureTree.Node121 has 1 site rate classes
	mixtureTree.Node119 has 2 site rate classes
	mixtureTree.Node117 has 1 site rate classes
	mixtureTree.Petrosimonia_glaucescens_C4 has 1 site rate classes
	mixtureTree.Petrosimonia_squarrosa_C4 has 1 site rate classes
	mixtureTree.Node131 has 1 site rate classes
	mixtureTree.Petrosimonia_nigdeensis_C4 has 1 site rate classes
	mixtureTree.Node130 has 1 site rate classes
	mixtureTree.Petrosimonia_sibirica_C4 has 1 site rate classes
	mixtureTree.Node129 has 1 site rate classes
	mixtureTree.Halimocnemis_villosa_C4 has 1 site rate classes
	mixtureTree.Halimocnemis_karelinii_C4 has 1 site rate classes
	mixtureTree.Node138 has 1 site rate classes
	mixtureTree.Salsola_sukaczevii_C4 has 1 site rate classes
	mixtureTree.Salsola_ferganica_C4 has 1 site rate classes
	mixtureTree.Salsola_heptapotamica_C4 has 1 site rate classes
	mixtureTree.Node144 has 1 site rate classes
	mixtureTree.Node142 has 1 site rate classes
	mixtureTree.Climacoptera_lanata_C4 has 1 site rate classes
	mixtureTree.Node141 has 1 site rate classes
	mixtureTree.Node137 has 1 site rate classes
	mixtureTree.Salsola_affinis_C4 has 1 site rate classes
	mixtureTree.Climacoptera_brachiata_C4 has 1 site rate classes
	mixtureTree.Node148 has 1 site rate classes
	mixtureTree.Node136 has 1 site rate classes
	mixtureTree.Node128 has 1 site rate classes
	mixtureTree.Node116 has 1 site rate classes
	mixtureTree.Nanophyton_erinaceum_C4 has 1 site rate classes
	mixtureTree.Kochia_americana_C3 has 1 site rate classes
	mixtureTree.Bassia_diffusa_C3 has 1 site rate classes
	mixtureTree.Node157 has 1 site rate classes
	mixtureTree.Bassia_dasyphylla_C3 has 1 site rate classes
	mixtureTree.Maireana_brevifolia_C3 has 1 site rate classes
	mixtureTree.Sclerolaena_obliquicuspis_C3 has 1 site rate classes
	mixtureTree.Roycea_divaricata_C3 has 1 site rate classes
	mixtureTree.Dissocarpus_paradoxus_C3 has 1 site rate classes
	mixtureTree.Node167 has 1 site rate classes
	mixtureTree.Node165 has 1 site rate classes
	mixtureTree.Node163 has 1 site rate classes
	mixtureTree.Node161 has 1 site rate classes
	mixtureTree.Kochia_densiflora_C4 has 1 site rate classes
	mixtureTree.Chenoleoides_tomentosa_C4 has 1 site rate classes
	mixtureTree.Bassia_prostrata_C4 has 1 site rate classes
	mixtureTree.Panderia_pilosa_C4 has 1 site rate classes
	mixtureTree.Node175 has 1 site rate classes
	mixtureTree.Node173 has 1 site rate classes
	mixtureTree.Node171 has 1 site rate classes
	mixtureTree.Bassia_sedoides_C4 has 1 site rate classes
	mixtureTree.Camphorosma_monspeliaca_C4 has 1 site rate classes
	mixtureTree.Node178 has 1 site rate classes
	mixtureTree.Node170 has 1 site rate classes
	mixtureTree.Node160 has 1 site rate classes
	mixtureTree.Node156 has 1 site rate classes
	mixtureTree.Sympegma_regelii_C3 has 2 site rate classes
	mixtureTree.Halothamnus_bottae_C4 has 1 site rate classes
	mixtureTree.Node182 has 1 site rate classes
	mixtureTree.Salsola_rosacea_C4 has 1 site rate classes
	mixtureTree.Noaea_mucronata_C4 has 1 site rate classes
	mixtureTree.Node190 has 1 site rate classes
	mixtureTree.Ofaiston_monandrum_C4 has 1 site rate classes
	mixtureTree.Node189 has 1 site rate classes
	mixtureTree.Rhaphidophyton_regelii_C3 has 1 site rate classes
	mixtureTree.Node188 has 1 site rate classes
	mixtureTree.Salsola_arbusculiformis_C3 has 1 site rate classes
	mixtureTree.Node187 has 1 site rate classes
	mixtureTree.Salsola_laricifolia_C3 has 1 site rate classes
	mixtureTree.Node186 has 1 site rate classes
	mixtureTree.Anabasis_brevifolia_C4 has 1 site rate classes
	mixtureTree.Anabasis_truncata_C4 has 1 site rate classes
	mixtureTree.Node199 has 1 site rate classes
	mixtureTree.Anabasis_eriopoda_C4 has 1 site rate classes
	mixtureTree.Anabasis_aphylla_C4 has 1 site rate classes
	mixtureTree.Anabasis_salsa_C4 has 1 site rate classes
	mixtureTree.Anabasis_elatior_C4 has 1 site rate classes
	mixtureTree.Node206 has 1 site rate classes
	mixtureTree.Node204 has 1 site rate classes
	mixtureTree.Node202 has 1 site rate classes
	mixtureTree.Node198 has 1 site rate classes
	mixtureTree.Girgensohnia_oppositiflora_C4 has 1 site rate classes
	mixtureTree.Halogeton_glomeratus_C4 has 1 site rate classes
	mixtureTree.Haloxylon_ammodendron_C4 has 1 site rate classes
	mixtureTree.Haloxylon_persicum_C4 has 1 site rate classes
	mixtureTree.Node215 has 1 site rate classes
	mixtureTree.Node213 has 1 site rate classes
	mixtureTree.Node211 has 1 site rate classes
	mixtureTree.Haloxylon_tamariscifolium_C4 has 1 site rate classes
	mixtureTree.Horaninovia_ulicina_C4 has 1 site rate classes
	mixtureTree.Halogeton_arachnoideus_C4 has 1 site rate classes
	mixtureTree.Node221 has 1 site rate classes
	mixtureTree.Node219 has 1 site rate classes
	mixtureTree.Iljinia_regelii_C4 has 1 site rate classes
	mixtureTree.Node218 has 1 site rate classes
	mixtureTree.Node210 has 1 site rate classes
	mixtureTree.Salsola_foliosa_C4 has 1 site rate classes
	mixtureTree.Node209 has 1 site rate classes
	mixtureTree.Node197 has 1 site rate classes
	mixtureTree.Node185 has 1 site rate classes
	mixtureTree.Node181 has 1 site rate classes
	mixtureTree.Node155 has 1 site rate classes
	mixtureTree.Salsola_arbuscula_C4 has 1 site rate classes
	mixtureTree.Salsola_kali_C4 has 1 site rate classes
	mixtureTree.Salsola_chinghaiensis_C4 has 1 site rate classes
	mixtureTree.Salsola_zaidamica_C4 has 1 site rate classes
	mixtureTree.Salsola_komarovii_C4 has 1 site rate classes
	mixtureTree.Salsola_ruthenica_C4 has 1 site rate classes
	mixtureTree.Node236 has 1 site rate classes
	mixtureTree.Salsola_collina_C4 has 1 site rate classes
	mixtureTree.Node235 has 1 site rate classes
	mixtureTree.Node233 has 1 site rate classes
	mixtureTree.Node231 has 1 site rate classes
	mixtureTree.Salsola_praecox_C4 has 1 site rate classes
	mixtureTree.Salsola_pellucida_C4 has 1 site rate classes
	mixtureTree.Salsola_paulsenii_C4 has 1 site rate classes
	mixtureTree.Node242 has 1 site rate classes
	mixtureTree.Node240 has 1 site rate classes
	mixtureTree.Node230 has 1 site rate classes
	mixtureTree.Node228 has 1 site rate classes
	mixtureTree.Node226 has 1 site rate classes
	mixtureTree.Node154 has 1 site rate classes
	mixtureTree.Salsola_genistoides_C3 has 1 site rate classes
	mixtureTree.Node153 has 1 site rate classes
	mixtureTree.Node151 has 1 site rate classes
	mixtureTree.Node115 has 1 site rate classes
	mixtureTree.Arthrocnemum_macrostachyum_C3 has 1 site rate classes
	mixtureTree.Sarcocornia_utahensis_C3 has 1 site rate classes
	mixtureTree.Salicornia_europaea_C3 has 1 site rate classes
	mixtureTree.Node253 has 1 site rate classes
	mixtureTree.Node251 has 1 site rate classes
	mixtureTree.Tecticornia_disarticulata_C3 has 1 site rate classes
	mixtureTree.Sclerostegia_moniliformis_C3 has 1 site rate classes
	mixtureTree.Node257 has 1 site rate classes
	mixtureTree.Tecticornia_australasica_C3 has 1 site rate classes
	mixtureTree.Salicornia_dolichostachya_C3 has 2 site rate classes
	mixtureTree.Halosarcia_indica_C4 has 1 site rate classes
	mixtureTree.Node263 has 1 site rate classes
	mixtureTree.Pachycornia_triandra_C3 has 1 site rate classes
	mixtureTree.Node262 has 1 site rate classes
	mixtureTree.Node260 has 1 site rate classes
	mixtureTree.Node256 has 1 site rate classes
	mixtureTree.Node250 has 1 site rate classes
	mixtureTree.Halostachys_belangeriana_C3 has 1 site rate classes
	mixtureTree.Halopeplis_amplexicaulis_C3 has 1 site rate classes
	mixtureTree.Node268 has 1 site rate classes
	mixtureTree.Kalidium_cuspidatum_C3 has 1 site rate classes
	mixtureTree.Kalidium_caspicum_C3 has 1 site rate classes
	mixtureTree.Kalidium_foliatum_C3 has 1 site rate classes
	mixtureTree.Node273 has 1 site rate classes
	mixtureTree.Node271 has 1 site rate classes
	mixtureTree.Node267 has 1 site rate classes
	mixtureTree.Node249 has 1 site rate classes
	mixtureTree.Allenrolfea_occidentalis_C3 has 2 site rate classes
	mixtureTree.Node248 has 1 site rate classes
	mixtureTree.Bienertia_cycloptera_C4 has 2 site rate classes
	mixtureTree.Node247 has 1 site rate classes
	mixtureTree.Suaeda_maritima_C3 has 1 site rate classes
	mixtureTree.Suaeda_crassifolia_C3 has 1 site rate classes
	mixtureTree.Node279 has 1 site rate classes
	mixtureTree.Suaeda_physophora_C3 has 1 site rate classes
	mixtureTree.Suaeda_microphylla_C4 has 1 site rate classes
	mixtureTree.Node283 has 1 site rate classes
	mixtureTree.Suaeda_altissima_C4 has 1 site rate classes
	mixtureTree.Node282 has 1 site rate classes
	mixtureTree.Node278 has 1 site rate classes
	mixtureTree.Node246 has 1 site rate classes
	mixtureTree.Node114 has 1 site rate classes
	mixtureTree.Agriophyllum_squarrosum_C3 has 1 site rate classes
	mixtureTree.Corispermum_filifolium_C3 has 1 site rate classes
	mixtureTree.Anthochlamys_multinervis_C3 has 1 site rate classes
	mixtureTree.Node289 has 1 site rate classes
	mixtureTree.Node287 has 2 site rate classes
	mixtureTree.Node113 has 1 site rate classes
	mixtureTree.Acroglochin_chenopodioides_C3 has 2 site rate classes
	mixtureTree.Node112 has 1 site rate classes
	mixtureTree.Node30 has 1 site rate classes
	mixtureTree.Node16 has 1 site rate classes
	mixtureTree.Monolepis_nuttalliana_C3 has 1 site rate classes
	mixtureTree.Spinacia_oleracea_C3 has 1 site rate classes
	mixtureTree.Node295 has 1 site rate classes
	mixtureTree.Chenopodium_foliosum_C3 has 2 site rate classes
	mixtureTree.Node294 has 1 site rate classes
	mixtureTree.Chenopodium_bonushenricus_C3 has 1 site rate classes
	mixtureTree.Node293 has 1 site rate classes
	mixtureTree.Node15 has 1 site rate classes
	mixtureTree.Node9 has 1 site rate classes
	mixtureTree.Chenopodium_coronopus_C3 has 2 site rate classes
	mixtureTree.Node8 has 1 site rate classes
	mixtureTree.Microgynoecium_tibeticum_C3 has 1 site rate classes
	mixtureTree.Chenopodium_acuminatum_C3 has 1 site rate classes
	mixtureTree.Chenopodium_album_C3 has 1 site rate classes
	mixtureTree.Chenopodium_murale_C3 has 1 site rate classes
	mixtureTree.Node309 has 1 site rate classes
	mixtureTree.Chenopodium_sanctaeclarae_C3 has 1 site rate classes
	mixtureTree.Node308 has 1 site rate classes
	mixtureTree.Node306 has 1 site rate classes
	mixtureTree.Chenopodium_frutescens_C3 has 1 site rate classes
	mixtureTree.Node305 has 1 site rate classes
	mixtureTree.Micromonolepis_pusilla_C3 has 1 site rate classes
	mixtureTree.Node304 has 1 site rate classes
	mixtureTree.Einadia_nutans_C3 has 1 site rate classes
	mixtureTree.Rhagodia_drummondi_C3 has 1 site rate classes
	mixtureTree.Node316 has 1 site rate classes
	mixtureTree.Chenopodium_desertorum_C3 has 1 site rate classes
	mixtureTree.Chenopodium_auricomum_C3 has 1 site rate classes
	mixtureTree.Node319 has 1 site rate classes
	mixtureTree.Node315 has 1 site rate classes
	mixtureTree.Node303 has 2 site rate classes
	mixtureTree.Node301 has 1 site rate classes
	mixtureTree.Node7 has 2 site rate classes
	mixtureTree.Manochlamys_albicans_C3 has 1 site rate classes
	mixtureTree.Archiatriplex_nanpinensis_C3 has 1 site rate classes
	mixtureTree.Node322 has 1 site rate classes
	mixtureTree.Node6 has 1 site rate classes
	mixtureTree.Node2 has 1 site rate classes
	mixtureTree.Atriplex_parryi_C4 has 1 site rate classes
	mixtureTree.Atriplex_phyllostegia_C4 has 1 site rate classes
	mixtureTree.Atriplex_serenana_C4 has 1 site rate classes
	mixtureTree.Node332 has 1 site rate classes
	mixtureTree.Atriplex_powellii_C4 has 1 site rate classes
	mixtureTree.Node331 has 1 site rate classes
	mixtureTree.Node329 has 1 site rate classes
	mixtureTree.Atriplex_lampa_C4 has 1 site rate classes
	mixtureTree.Atriplex_undulata_C4 has 1 site rate classes
	mixtureTree.Node337 has 1 site rate classes
	mixtureTree.Atriplex_lentiformis_C4 has 1 site rate classes
	mixtureTree.Node336 has 1 site rate classes
	mixtureTree.Node328 has 1 site rate classes
	mixtureTree.Atriplex_spongiosa_C4 has 1 site rate classes
	mixtureTree.Atriplex_rosea_C4 has 1 site rate classes
	mixtureTree.Node343 has 1 site rate classes
	mixtureTree.Atriplex_centralasiatica_C4 has 1 site rate classes
	mixtureTree.Node342 has 1 site rate classes
	mixtureTree.Atriplex_glauca_C4 has 1 site rate classes
	mixtureTree.Node341 has 1 site rate classes
	mixtureTree.Node327 has 1 site rate classes
	mixtureTree.Atriplex_coriacea_C4 has 1 site rate classes
	mixtureTree.Node326 has 1 site rate classes
	mixtureTree.Atriplex_halimus_C4 has 1 site rate classes
	mixtureTree.Cremnophyton_lanfrancoi_C3 has 1 site rate classes
	mixtureTree.Node349 has 1 site rate classes
	mixtureTree.Node325 has 1 site rate classes
	mixtureTree.Node1 has 1 site rate classes
	mixtureTree.Atriplex_australasica_C3 has 1 site rate classes
	mixtureTree.Atriplex_patula_C3 has 1 site rate classes
	mixtureTree.Node352 has 1 site rate classes
	mixtureTree.Atriplex_aucherii_C3 has 1 site rate classes


[PHASE 2] Fitting the full LOCAL alternative model (no constraints)

Log L = -10548.65897437741 with 766 degrees of freedom, IC = 22644.145750789
((((Halimione_pedunculata_C3:0.006329735649071736,Halimione_verrucifera_C3:0.0007305434203567839)Node3:0.00386134544660872,(((((Axyris_prostrata_C3:0.01071506509916469,(Ceratocarpus_arenarius_C3:0.02320284973452376,Krascheninnikovia_ceratoides_C3:0.01099806321941586)Node12:0.008062824241127827)Node10:0.01220412571085811,((((Suckleya_suckleyana_C3:0.01451779234173086,(Cycloloma_atriplicifolium_C3:0.00461270432535816,(((Chenopodium_cristatum_C3:0.004574070022249951,Dysphania_glomulifera_C3:0.001984412878522231)Node24:0.003400272752934886,Chenopodium_ambrosioides_C3:0.006843823078812264)Node23:0,Chenopodium_botrys_C3:0.003837617259947947)Node22:0.0007490123005743581)Node20:0.004719013080471268)Node18:0.00544662971032035,Teloxys_aristata_C3:0.01041038754151692)Node17:0.001718139412361099,((((Hablitzia_tamnoides_C3:0.007581219867251036,(Aphanisma_blitoides_C3:0.004208610073978863,Patellifolia_patellaris_C3:0.005732864921683577)Node35:0.003235878286037855)Node33:0.003039685135883906,(Beta_vulgaris_C3:0.004628184327168476,Beta_nana_C3:0.001495812452163375)Node38:0.006863961812138567)Node32:0.003604003444241227,(((((Ptilotus_manglesii_C3:0.008037551767525413,(((Iresine_palmeri_C3:0.003009046523406567,((Gomphrena_elegans_C3:0.005353064925780439,(Pseudoplantago_friesii_C3:0.002787660631218268,Hebanthe_occidentalis_C3:0.0002480238387011396)Node54:0.006732127791583241)Node52:0.004563713731403052,(((Guilleminea_densa_C4:0.007865757057953244,(Gomphrena_serrata_C4:0.0007451205001740443,Gomphrena_haageana_C4:0.002328130254022568)Node61:0.001602922977585792)Node59:0.0007846904785297573,Blutaparon_vermiculare_C4:0.0007772515377132318)Node58:0.005614392221032068,((Alternanthera_pungens_C4:0.001587578217739578,(Alternanthera_caracasana_C4:0.0007439437931018833,Alternanthera_repens_C4:0)Node68:0)Node66:0.009087423328763592,Tidestromia_lanuginosa_C4:0.01638694640096593)Node65:0.0007971620852869096)Node57:0.003435483635254751)Node51:0.002716590437104434)Node49:0.0007734804594923115,Aerva_javanica_C4:0.01082247199239101)Node48:0,(Pupalia_lappacea_C3:0.003865175737139052,(((Sericostachys_scandens_C3:0.005384022465756629,(Achyranthes_aspera_C3:0.0007858852713312764,Nototrichium_humile_C3:0.003110447209684279)Node79:0.002262539150585439)Node77:0.0007421176942746227,Pandiaka_angustifolia_C3:0.004730653356197071)Node76:0,Calicorema_capitata_C3:0.001521628458656505)Node75:0)Node73:0.001555116976538177)Node47:0.0006185693582032968)Node45:0.01446865207897294,(((Chamissoa_altissima_C3:0.01946207048609774,((Amaranthus_greggii_C4:0,Amaranthus_tricolor_C4:0.0007838040852496023)Node89:0,(Amaranthus_blitum_C4:0,Amaranthus_hypochondriacus_C4:0.09970181458930538)Node92:0.002270209310692829)Node88:0.01028239598467811)Node86:0.008707020546575883,(Deeringia_amaranthoides_C3:0.01014550841692284,(Hermbstaedtia_glauca_C3:0.8684060798950721,(Celosia_trigyna_C3:0.002242050019378885,Celosia_argentea_C3:0.006155546776071847)Node99:0.008303283831877627)Node97:0.005243679696825655)Node95:0.001813850506400183)Node85:0.008228891972800729,(Charpentiera_ovata_C3:0,Charpentiera_obovata_C3:0.001485418089808669)Node102:0.01958329947173916)Node84:0.003118763482822843)Node44:0.04953765904131607,Bosea_yervamora_C3:0.008704875255644156)Node43:0.001116024024049091,((Nitrophila_occidentalis_C3:0.003092298280644959,Hemichroa_diandra_C3:0.002298621614010766)Node107:0.003760840329718217,Polycnemum_perenne_C3:0.01155587012052684)Node106:0.01073592439877234)Node42:0.002663247817488635,Oreobliton_thesioides_C3:0.01829408823354227)Node41:0.001778870220948019)Node31:0.0007456164968411916,((((((Halocharis_hispida_C4:0.006367823771517989,(Salsola_vermiculata_C4:0.008334446034898959,(Salsola_implicata_C4:0.003899304763044821,((Salsola_orientalis_C4:0,Salsola_dshungarica_C4:0)Node124:0.001575954957185974,Salsola_micranthera_C4:0.0007873131335501619)Node123:0.001561879933681288)Node121:0)Node119:0.005309329724401464)Node117:0.003046743342767268,((((Petrosimonia_glaucescens_C4:0,Petrosimonia_squarrosa_C4:0)Node131:0.002381857403520207,Petrosimonia_nigdeensis_C4:0.009429340659972299)Node130:0.001450268535216262,Petrosimonia_sibirica_C4:0.005763049054119205)Node129:0.002226239291401158,(((Halimocnemis_villosa_C4:0,Halimocnemis_karelinii_C4:0)Node138:0.007877982214208573,((Salsola_sukaczevii_C4:0,(Salsola_ferganica_C4:0,Salsola_heptapotamica_C4:0)Node144:0)Node142:0,Climacoptera_lanata_C4:0)Node141:0.002350662475622921)Node137:0.0009233830805747052,(Salsola_affinis_C4:0.003604396479243485,Climacoptera_brachiata_C4:0.00157199200535219)Node148:0.001014759164261699)Node136:0.002354531145451773)Node128:0.004132505830096247)Node116:0.001662600969031276,(Nanophyton_erinaceum_C4:0.01265076314403201,(((((Kochia_americana_C3:0.003756285883823642,Bassia_diffusa_C3:0.003087952816908471)Node157:0.003191934649972373,((Bassia_dasyphylla_C3:0.003962864232579367,(Maireana_brevifolia_C3:0.0007820443000486842,(Sclerolaena_obliquicuspis_C3:0.002268526907243391,(Roycea_divaricata_C3:0.0007833932918434654,Dissocarpus_paradoxus_C3:0.0007424315405155824)Node167:0)Node165:0.0007418961358218174)Node163:0.0007414344440763248)Node161:0.001571780387588046,((Kochia_densiflora_C4:0.006096944031919978,(Chenoleoides_tomentosa_C4:0.002308472264365054,(Bassia_prostrata_C4:0.007891850081985577,Panderia_pilosa_C4:0.006178304088236837)Node175:0.0015167098933326)Node173:0)Node171:0.004707327433303118,(Bassia_sedoides_C4:0.003757998290381917,Camphorosma_monspeliaca_C4:0.007736285278171422)Node178:0.003619242230290848)Node170:0.002230671569991506)Node160:0.0007605037650845447)Node156:0.008754284497266082,((Sympegma_regelii_C3:0.01272526498230496,Halothamnus_bottae_C4:0.00323992463525268)Node182:0.001479976280931324,((((((Salsola_rosacea_C4:0.001348584999037751,Noaea_mucronata_C4:0.00332575946336023)Node190:0.001596517062411941,Ofaiston_monandrum_C4:0.007543884425649981)Node189:0.002592060906086172,Rhaphidophyton_regelii_C3:0.001563133249573968)Node188:0,Salsola_arbusculiformis_C3:0)Node187:0,Salsola_laricifolia_C3:0.001567696933149416)Node186:0.0007825136767504832,(((Anabasis_brevifolia_C4:0,Anabasis_truncata_C4:0.002358576818861968)Node199:0.0007856884370899176,(Anabasis_eriopoda_C4:0.0007869920864930887,(Anabasis_aphylla_C4:0.001565035883129048,(Anabasis_salsa_C4:0,Anabasis_elatior_C4:0.0007828154688716634)Node206:0.001574746172226153)Node204:0.001530439615385818)Node202:0.001583589922508878)Node198:0.001570922289440977,(((Girgensohnia_oppositiflora_C4:0.004803631979196153,(Halogeton_glomeratus_C4:0.004652613558245471,(Haloxylon_ammodendron_C4:0,Haloxylon_persicum_C4:0)Node215:0.003172064080172715)Node213:0.0007422147288883061)Node211:0,((Haloxylon_tamariscifolium_C4:0.001527522527094818,(Horaninovia_ulicina_C4:0.008740124454157432,Halogeton_arachnoideus_C4:0.003158780632736856)Node221:0.00148489357144976)Node219:0,Iljinia_regelii_C4:0)Node218:0)Node210:0.0007935031844652694,Salsola_foliosa_C4:0.004798892475570321)Node209:0.001570254218919755)Node197:0)Node185:0.0038793843262422)Node181:0.0008547941267300769)Node155:0.002248147383132664,(Salsola_arbuscula_C4:0.001520553595099652,(Salsola_kali_C4:0.0007734013577560627,((Salsola_chinghaiensis_C4:0.0007768224556218115,(Salsola_zaidamica_C4:0.0007417826144388038,((Salsola_komarovii_C4:0,Salsola_ruthenica_C4:0)Node236:0,Salsola_collina_C4:0)Node235:0)Node233:0)Node231:0.0007745914446829257,(Salsola_praecox_C4:0,(Salsola_pellucida_C4:0,Salsola_paulsenii_C4:0)Node242:0)Node240:0)Node230:0)Node228:0.001512914040791592)Node226:0.003915665726993132)Node154:0.0007401674061799645,Salsola_genistoides_C3:0.002347975928795706)Node153:0.0007397132391846955)Node151:0)Node115:0.00859461268000467,((((((Arthrocnemum_macrostachyum_C3:0.001576857416256497,(Sarcocornia_utahensis_C3:0.003137863086551267,Salicornia_europaea_C3:0.008059764779345918)Node253:0.001570980744754432)Node251:0.001485161330831809,((Tecticornia_disarticulata_C3:0.001485142269390312,Sclerostegia_moniliformis_C3:0.001595344201323659)Node257:0.003022856844807735,(Tecticornia_australasica_C3:0.0007423867494563498,((Salicornia_dolichostachya_C3:0.02262449169264314,Halosarcia_indica_C4:0.004630424518353958)Node263:0.004880330203710854,Pachycornia_triandra_C3:0.001487509150301473)Node262:0.0007902269362461211)Node260:0)Node256:0.0007906747596008367)Node250:0.001621596887064435,((Halostachys_belangeriana_C3:0.000800577160569429,Halopeplis_amplexicaulis_C3:0.003985489351609938)Node268:0.002272384063920389,(Kalidium_cuspidatum_C3:0.003896931924995807,(Kalidium_caspicum_C3:0.003199264779646075,Kalidium_foliatum_C3:0)Node273:0)Node271:0.002357375361810347)Node267:0.003212741591078361)Node249:0.00134281340646536,Allenrolfea_occidentalis_C3:0.01310199050867239)Node248:0.006041974847357397,Bienertia_cycloptera_C4:0.01155918337145579)Node247:0.004031901437459114,((Suaeda_maritima_C3:0.00306937396894965,Suaeda_crassifolia_C3:0.003223352375145332)Node279:0.0142084490943065,((Suaeda_physophora_C3:0.003092733364739346,Suaeda_microphylla_C4:0.004743910236028633)Node283:0.006534715613140506,Suaeda_altissima_C4:0.01066616509060916)Node282:0.005471149403966289)Node278:0.002909120369699098)Node246:0.006001762334840573)Node114:0.009363143012477442,(Agriophyllum_squarrosum_C3:0.007969868781616008,(Corispermum_filifolium_C3:0.006453067176577846,Anthochlamys_multinervis_C3:0.001521489201259761)Node289:0.004880677713663273)Node287:0.04253361418369292)Node113:0.001936941217690185,Acroglochin_chenopodioides_C3:0.0166626802748134)Node112:0.001252790604279667)Node30:0.002589511346314234)Node16:0.001304777197531716,(((Monolepis_nuttalliana_C3:0.00236343838062908,Spinacia_oleracea_C3:0.01755070941823846)Node295:0.009203189579665231,Chenopodium_foliosum_C3:0.005842081858882703)Node294:0.001552793715147973,Chenopodium_bonushenricus_C3:0.002287839789889359)Node293:0.001532708207208178)Node15:0.000768811932344565)Node9:0.005408042532500623,Chenopodium_coronopus_C3:0.01026756470289787)Node8:0.004669303857511161,(Microgynoecium_tibeticum_C3:0.009702104249000552,((((Chenopodium_acuminatum_C3:0.001516150209677109,((Chenopodium_album_C3:0,Chenopodium_murale_C3:0.0007683140968728492)Node309:0.00232591633286199,Chenopodium_sanctaeclarae_C3:0.003007005844100527)Node308:0)Node306:0,Chenopodium_frutescens_C3:0)Node305:0,Micromonolepis_pusilla_C3:0.003849221975912428)Node304:0.0007753236807662347,((Einadia_nutans_C3:0.0007673575869927523,Rhagodia_drummondi_C3:0)Node316:0.001486269141549888,(Chenopodium_desertorum_C3:0.0007426960247178447,Chenopodium_auricomum_C3:0.0007422221866968955)Node319:0)Node315:0.002291509277642555)Node303:0.01072317626164306)Node301:0.0006245983409887868)Node7:0.04129038431091838,(Manochlamys_albicans_C3:0.003792010319389287,Archiatriplex_nanpinensis_C3:0.006177812098606805)Node322:0.001558915092984091)Node6:0.001539384219530459)Node2:0.00453877902328799,(((((Atriplex_parryi_C4:0.0007705697089598366,((Atriplex_phyllostegia_C4:0.000773140209595827,Atriplex_serenana_C4:0)Node332:0,Atriplex_powellii_C4:0.0007749920235829009)Node331:0.001550315474220777)Node329:0,((Atriplex_lampa_C4:0.001515623787281466,Atriplex_undulata_C4:0.000741916933745616)Node337:0.000773652026517693,Atriplex_lentiformis_C4:0.0007724018144596028)Node336:0)Node328:0.0007418532296358375,(((Atriplex_spongiosa_C4:5.168687220913232e-18,Atriplex_rosea_C4:0.002282837757950542)Node343:0.0007428147346300215,Atriplex_centralasiatica_C4:0.003056358479116241)Node342:0.0007765190935028089,Atriplex_glauca_C4:0.003108242531894198)Node341:0.0007716287520713991)Node327:0.0007700999503434052,Atriplex_coriacea_C4:0.002312904161493579)Node326:0.001484525756593728,(Atriplex_halimus_C4:0.001513568840615057,Cremnophyton_lanfrancoi_C3:0)Node349:0)Node325:0)Node1:0.0007687065011433425,(Atriplex_australasica_C3:0,Atriplex_patula_C3:0)Node352:0,Atriplex_aucherii_C3:0.001538593104834232)

Node: mixtureTree.Halimione_pedunculata_C3
	Length parameter = 0.07683395530043916
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Halimione_verrucifera_C3
	Length parameter = 0.008867754297599255
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node3
	Length parameter = 0.02885554076239066
	Class 1: omega =     0.1848, weight = 1.

Node: mixtureTree.Axyris_prostrata_C3
	Length parameter = 0.09788227649405123
	Class 1: omega =     0.0973, weight = 1.

Node: mixtureTree.Ceratocarpus_arenarius_C3
	Length parameter = 0.193368339254059
	Class 1
		omega = 0.000
		weight = 0.979
	Class 2
		omega = 6.351
		weight = 0.021
...Testing for selection at this branch

Node: mixtureTree.Ceratocarpus_arenarius_C3
	Length parameter = 0.2029359674792435
	Class 1
		omega = 0.000
		weight = 0.923
	Class 2
		omega = 1.000
		weight = 0.077
p-value = 0.1380056108199328

Node: mixtureTree.Krascheninnikovia_ceratoides_C3
	Length parameter = 0.06589423364995226
	Class 1: omega =     0.3036, weight = 1.

Node: mixtureTree.Node12
	Length parameter = 0.08887044974752061
	Class 1: omega =     0.0300, weight = 1.

Node: mixtureTree.Node10
	Length parameter = 0.07672572208589967
	Class 1
		omega = 0.000
		weight = 0.996
	Class 2
		omega = 77.923
		weight = 0.004
...Testing for selection at this branch

Node: mixtureTree.Node10
	Length parameter = 0.08785512478059246
	Class 1
		omega = 0.000
		weight = 0.963
	Class 2
		omega = 1.000
		weight = 0.037
p-value = 0.006949551393990672

Node: mixtureTree.Suckleya_suckleyana_C3
	Length parameter = 0.1490820506266214
	Class 1: omega =     0.0539, weight = 1.

Node: mixtureTree.Cycloloma_atriplicifolium_C3
	Length parameter = 0.03790977237607286
	Class 1: omega =     0.1412, weight = 1.

Node: mixtureTree.Chenopodium_cristatum_C3
	Length parameter = 0.02831880537677029
	Class 1: omega =     0.2843, weight = 1.

Node: mixtureTree.Dysphania_glomulifera_C3
	Length parameter = 0.005915711027130069
	Class 1: omega =     0.9091, weight = 1.

Node: mixtureTree.Node24
	Length parameter = 0.03227097061433348
	Class 1: omega =     0.0826, weight = 1.

Node: mixtureTree.Chenopodium_ambrosioides_C3
	Length parameter = 0.03764896569506008
	Class 1: omega =     0.3571, weight = 1.

Node: mixtureTree.Node23
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Chenopodium_botrys_C3
	Length parameter = 0.03756430707271153
	Class 1: omega =     0.0711, weight = 1.

Node: mixtureTree.Node22
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node22
	Length parameter = 0.002097557797308058
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3532267438719278

Node: mixtureTree.Node20
	Length parameter = 0.0572820825685335
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node18
	Length parameter = 0.04795845604181888
	Class 1: omega =     0.1120, weight = 1.

Node: mixtureTree.Teloxys_aristata_C3
	Length parameter = 0.06771718888034084
	Class 1
		omega = 0.000
		weight = 0.983
	Class 2
		omega = 15.439
		weight = 0.017
...Testing for selection at this branch

Node: mixtureTree.Teloxys_aristata_C3
	Length parameter = 0.07700324179750907
	Class 1
		omega = 0.000
		weight = 0.856
	Class 2
		omega = 1.000
		weight = 0.144
p-value = 0.06419916224537855

Node: mixtureTree.Node17
	Length parameter = 0.02085575988132066
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Hablitzia_tamnoides_C3
	Length parameter = 0.05793495036010556
	Class 1: omega =     0.1741, weight = 1.

Node: mixtureTree.Aphanisma_blitoides_C3
	Length parameter = 0.02162850760888287
	Class 1: omega =     0.4031, weight = 1.

Node: mixtureTree.Patellifolia_patellaris_C3
	Length parameter = 0.04485703640943864
	Class 1: omega =     0.1632, weight = 1.

Node: mixtureTree.Node35
	Length parameter = 0.03017591565279305
	Class 1: omega =     0.0893, weight = 1.

Node: mixtureTree.Node33
	Length parameter = 0.0255814004228932
	Class 1: omega =     0.1309, weight = 1.

Node: mixtureTree.Beta_vulgaris_C3
	Length parameter = 0.04714720353268594
	Class 1: omega =     0.0567, weight = 1.

Node: mixtureTree.Beta_nana_C3
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Beta_nana_C3
	Length parameter = 0.004188591841676026
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.257676191771082

Node: mixtureTree.Node38
	Length parameter = 0.02957362949545723
	Class 1
		omega = 0.002
		weight = 0.989
	Class 2
		omega = 49.782
		weight = 0.011
...Testing for selection at this branch

Node: mixtureTree.Node38
	Length parameter = 0.04032459950411738
	Class 1
		omega = 0.000
		weight = 0.796
	Class 2
		omega = 1.000
		weight = 0.204
p-value = 0.02145734934141097

Node: mixtureTree.Node32
	Length parameter = 0.02563616020200516
	Class 1: omega =     0.2091, weight = 1.

Node: mixtureTree.Ptilotus_manglesii_C3
	Length parameter = 0.0885464681003789
	Class 1: omega =     0.0301, weight = 1.

Node: mixtureTree.Iresine_palmeri_C3
	Length parameter = 0.00944496591474963
	Class 1: omega =     0.8486, weight = 1.

Node: mixtureTree.Gomphrena_elegans_C3
	Length parameter = 0.06497856688344958
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Pseudoplantago_friesii_C3
	Length parameter = 0.01581204025944642
	Class 1: omega =     0.3374, weight = 1.

Node: mixtureTree.Hebanthe_occidentalis_C3
	Length parameter = 0.003010655356357793
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node54
	Length parameter = 0.06367309369480065
	Class 1: omega =     0.0839, weight = 1.

Node: mixtureTree.Node52
	Length parameter = 0.05539697015530901
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Guilleminea_densa_C4
	Length parameter = 0.05922202387394246
	Class 1: omega =     0.1812, weight = 1.

Node: mixtureTree.Gomphrena_serrata_C4
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Gomphrena_serrata_C4
	Length parameter = 0.002098078720970948
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3528175400474592

Node: mixtureTree.Gomphrena_haageana_C4
	Length parameter = 0.01921449208598847
	Class 1: omega =     0.1393, weight = 1.

Node: mixtureTree.Node61
	Length parameter = 0.01945719683063462
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node59
	Length parameter = 0.009525022290761433
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Blutaparon_vermiculare_C4
	Length parameter = 0.009434724168080222
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node58
	Length parameter = 0.06815070721210499
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Alternanthera_pungens_C4
	Length parameter = 0.01927093335021694
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Alternanthera_caracasana_C4
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Alternanthera_caracasana_C4
	Length parameter = 0.002094017993478579
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3525344250392655

Node: mixtureTree.Alternanthera_repens_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node68
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node66
	Length parameter = 0.1103083472278633
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Tidestromia_lanuginosa_C4
	Length parameter = 0.1898746127278351
	Class 1: omega =     0.0141, weight = 1.

Node: mixtureTree.Node65
	Length parameter = 0.009676409794004831
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node57
	Length parameter = 0.01458944186799074
	Class 1: omega =     0.5500, weight = 1.

Node: mixtureTree.Node51
	Length parameter = 0.03297553006730897
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node49
	Length parameter = 0.009388948661562323
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Aerva_javanica_C4
	Length parameter = 0.08608316895516095
	Class 1: omega =     0.1557, weight = 1.

Node: mixtureTree.Node48
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Pupalia_lappacea_C3
	Length parameter = 0.03789059823492786
	Class 1: omega =     0.0705, weight = 1.

Node: mixtureTree.Sericostachys_scandens_C3
	Length parameter = 0.0381961207254275
	Class 1: omega =     0.2104, weight = 1.

Node: mixtureTree.Achyranthes_aspera_C3
	Length parameter = 0.009539525369846367
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Nototrichium_humile_C3
	Length parameter = 0.03775638906947171
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node79
	Length parameter = 0.009412186707673102
	Class 1: omega =     0.5676, weight = 1.

Node: mixtureTree.Node77
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node77
	Length parameter = 0.0020839835857272
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3522745484701522

Node: mixtureTree.Pandiaka_angustifolia_C3
	Length parameter = 0.05742337889975267
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node76
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Calicorema_capitata_C3
	Length parameter = 0.009453885095006923
	Class 1: omega =     0.2823, weight = 1.

Node: mixtureTree.Node75
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node73
	Length parameter = 0.01887690021933398
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node47
	Length parameter = 0.007508549022167041
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node45
	Length parameter = 0.08583741090967405
	Class 1
		omega = 0.000
		weight = 0.988
	Class 2
		omega = 25.475
		weight = 0.012
...Testing for selection at this branch

Node: mixtureTree.Node45
	Length parameter = 0.1076712361025622
	Class 1
		omega = 0.000
		weight = 0.894
	Class 2
		omega = 1.000
		weight = 0.106
p-value = 0.008347888593696895

Node: mixtureTree.Chamissoa_altissima_C3
	Length parameter = 0.1906796819501846
	Class 1: omega =     0.0707, weight = 1.

Node: mixtureTree.Amaranthus_greggii_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Amaranthus_tricolor_C4
	Length parameter = 0.009514262741636184
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node89
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Amaranthus_blitum_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Amaranthus_hypochondriacus_C4
	Length parameter = 0.005483231629782167
	Class 1
		omega = 0.000
		weight = 0.992
	Class 2
		omega = 8479.625
		weight = 0.008
...Testing for selection at this branch

Node: mixtureTree.Amaranthus_hypochondriacus_C4
	Length parameter = 0.02953697168525933
	Class 1
		omega = 0.000
		weight = 0.726
	Class 2
		omega = 1.000
		weight = 0.274
p-value = 1.237219097899311e-05

Node: mixtureTree.Node92
	Length parameter = 0.00950803507479593
	Class 1: omega =     0.5618, weight = 1.

Node: mixtureTree.Node88
	Length parameter = 0.07991725082749782
	Class 1: omega =     0.1663, weight = 1.

Node: mixtureTree.Node86
	Length parameter = 0.08993664907963619
	Class 1: omega =     0.0518, weight = 1.

Node: mixtureTree.Deeringia_amaranthoides_C3
	Length parameter = 0.08690577617963244
	Class 1: omega =     0.1234, weight = 1.

Node: mixtureTree.Hermbstaedtia_glauca_C3
	Length parameter = 0.06633659146407749
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 10000.000
		weight = 0.005
...Testing for selection at this branch

Node: mixtureTree.Hermbstaedtia_glauca_C3
	Length parameter = 0.08829261476421804
	Class 1
		omega = 0.000
		weight = 0.936
	Class 2
		omega = 1.000
		weight = 0.064
p-value = 0.0002718993764596056

Node: mixtureTree.Celosia_trigyna_C3
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Celosia_trigyna_C3
	Length parameter = 0.006419854315955293
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.2006165060221698

Node: mixtureTree.Celosia_argentea_C3
	Length parameter = 0.03838664159469572
	Class 1: omega =     0.2801, weight = 1.

Node: mixtureTree.Node99
	Length parameter = 0.09180499146418616
	Class 1: omega =     0.0290, weight = 1.

Node: mixtureTree.Node97
	Length parameter = 0.0378899869104857
	Class 1: omega =     0.2012, weight = 1.

Node: mixtureTree.Node95
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node95
	Length parameter = 0.005733660435319656
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3328858825300691

Node: mixtureTree.Node85
	Length parameter = 0.09085651261189065
	Class 1
		omega = 0.029
		weight = 1.000
	Class 2
		omega = 0.481
		weight = 0.000

Node: mixtureTree.Charpentiera_ovata_C3
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Charpentiera_obovata_C3
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Charpentiera_obovata_C3
	Length parameter = 0.004147231422082146
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.255607992585026

Node: mixtureTree.Node102
	Length parameter = 0.1234136271253014
	Class 1
		omega = 0.000
		weight = 0.982
	Class 2
		omega = 15.419
		weight = 0.018
...Testing for selection at this branch

Node: mixtureTree.Node102
	Length parameter = 0.1262983667802658
	Class 1
		omega = 0.000
		weight = 0.890
	Class 2
		omega = 1.000
		weight = 0.110
p-value = 0.06583839834923452

Node: mixtureTree.Node84
	Length parameter = 0.02638474449557734
	Class 1: omega =     0.1287, weight = 1.

Node: mixtureTree.Node44
	Length parameter = 0.0258923013038943
	Class 1
		omega = 0.020
		weight = 0.994
	Class 2
		omega = 1013.247
		weight = 0.006
...Testing for selection at this branch

Node: mixtureTree.Node44
	Length parameter = 0.05012473664921171
	Class 1
		omega = 0.000
		weight = 0.889
	Class 2
		omega = 1.000
		weight = 0.111
p-value = 0.0001780156485715056

Node: mixtureTree.Bosea_yervamora_C3
	Length parameter = 0.07856511289214416
	Class 1: omega =     0.1021, weight = 1.

Node: mixtureTree.Node43
	Length parameter = 0.01354693856615944
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Nitrophila_occidentalis_C3
	Length parameter = 0.03753608697790454
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Hemichroa_diandra_C3
	Length parameter = 0.02790198519102878
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node107
	Length parameter = 0.03662460365079519
	Class 1: omega =     0.0729, weight = 1.

Node: mixtureTree.Polycnemum_perenne_C3
	Length parameter = 0.1402717676572242
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node106
	Length parameter = 0.08456738240311765
	Class 1: omega =     0.1601, weight = 1.

Node: mixtureTree.Node42
	Length parameter = 0.0323280268099226
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Oreobliton_thesioides_C3
	Length parameter = 0.1949713717934653
	Class 1: omega =     0.0411, weight = 1.

Node: mixtureTree.Node41
	Length parameter = 0.02159294520643156
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node31
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node31
	Length parameter = 0.002137640392073062
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3397616081534051

Node: mixtureTree.Halocharis_hispida_C4
	Length parameter = 0.0772962907374557
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Salsola_vermiculata_C4
	Length parameter = 0.03803203655689409
	Class 1: omega =     0.4913, weight = 1.

Node: mixtureTree.Salsola_implicata_C4
	Length parameter = 0.0473319937003233
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Salsola_orientalis_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Salsola_dshungarica_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node124
	Length parameter = 0.01912984355889968
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Salsola_micranthera_C4
	Length parameter = 0.00955685757895958
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node123
	Length parameter = 0.01895899286516332
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node121
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node119
	Length parameter = 0.009151532014107254
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 332.144
		weight = 0.005
...Testing for selection at this branch

Node: mixtureTree.Node119
	Length parameter = 0.01930342425580032
	Class 1
		omega = 0.000
		weight = 0.722
	Class 2
		omega = 1.000
		weight = 0.278
p-value = 0.004946923660512359

Node: mixtureTree.Node117
	Length parameter = 0.02800030491494021
	Class 1: omega =     0.0949, weight = 1.

Node: mixtureTree.Petrosimonia_glaucescens_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Petrosimonia_squarrosa_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node131
	Length parameter = 0.02891234885945512
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Petrosimonia_nigdeensis_C4
	Length parameter = 0.08732925242102105
	Class 1: omega =     0.0919, weight = 1.

Node: mixtureTree.Node130
	Length parameter = 0.01760418980921912
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Petrosimonia_sibirica_C4
	Length parameter = 0.06995518896328157
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node129
	Length parameter = 0.01803592059298451
	Class 1: omega =     0.1475, weight = 1.

Node: mixtureTree.Halimocnemis_villosa_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Halimocnemis_karelinii_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node138
	Length parameter = 0.08663414145546788
	Class 1: omega =     0.0307, weight = 1.

Node: mixtureTree.Salsola_sukaczevii_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Salsola_ferganica_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Salsola_heptapotamica_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node144
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node142
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Climacoptera_lanata_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node141
	Length parameter = 0.02853368696446555
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node137
	Length parameter = 0.01120855250068195
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Salsola_affinis_C4
	Length parameter = 0.04375222810637722
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Climacoptera_brachiata_C4
	Length parameter = 0.01908173898061459
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node148
	Length parameter = 0.01231772772043465
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node136
	Length parameter = 0.0106086863039418
	Class 1: omega =     0.5014, weight = 1.

Node: mixtureTree.Node128
	Length parameter = 0.05016272176784878
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node116
	Length parameter = 0.02018160245850863
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Nanophyton_erinaceum_C4
	Length parameter = 0.1445808268707536
	Class 1: omega =     0.0184, weight = 1.

Node: mixtureTree.Kochia_americana_C3
	Length parameter = 0.009435904158618495
	Class 1: omega =     1.1342, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Kochia_americana_C3
	Length parameter = 0.01043289464143576
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.4812276530172262

Node: mixtureTree.Bassia_diffusa_C3
	Length parameter = 0.0284793402267552
	Class 1: omega =     0.0936, weight = 1.

Node: mixtureTree.Node157
	Length parameter = 0.03874553027405912
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Bassia_dasyphylla_C3
	Length parameter = 0.04810351493152246
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Maireana_brevifolia_C3
	Length parameter = 0.009492901461329707
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Sclerolaena_obliquicuspis_C3
	Length parameter = 0.00951520889217273
	Class 1: omega =     0.5605, weight = 1.

Node: mixtureTree.Roycea_divaricata_C3
	Length parameter = 0.009509276296079098
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Dissocarpus_paradoxus_C3
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Dissocarpus_paradoxus_C3
	Length parameter = 0.002083248898977597
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3514180677307241

Node: mixtureTree.Node167
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node165
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node165
	Length parameter = 0.002083246062399817
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3516645024978881

Node: mixtureTree.Node163
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node163
	Length parameter = 0.00208494122330995
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3558333954903069

Node: mixtureTree.Node161
	Length parameter = 0.01907917024303494
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Kochia_densiflora_C4
	Length parameter = 0.0469572568759697
	Class 1: omega =     0.1705, weight = 1.

Node: mixtureTree.Chenoleoides_tomentosa_C4
	Length parameter = 0.02802155802486625
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Bassia_prostrata_C4
	Length parameter = 0.0867887894227201
	Class 1: omega =     0.0307, weight = 1.

Node: mixtureTree.Panderia_pilosa_C4
	Length parameter = 0.04792141180447503
	Class 1: omega =     0.1672, weight = 1.

Node: mixtureTree.Node175
	Length parameter = 0.01841069305400468
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node173
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node171
	Length parameter = 0.05714023549277038
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Bassia_sedoides_C4
	Length parameter = 0.04561673483231094
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Camphorosma_monspeliaca_C4
	Length parameter = 0.07583795173719858
	Class 1: omega =     0.0705, weight = 1.

Node: mixtureTree.Node178
	Length parameter = 0.04393243433229468
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node170
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node170
	Length parameter = 0.006297510212444772
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.2000799733591279

Node: mixtureTree.Node160
	Length parameter = 0.009231430115235662
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node156
	Length parameter = 0.09727584424917035
	Class 1: omega =     0.0273, weight = 1.

Node: mixtureTree.Sympegma_regelii_C3
	Length parameter = 0.05745966409818509
	Class 1
		omega = 0.038
		weight = 0.997
	Class 2
		omega = 164.639
		weight = 0.003
...Testing for selection at this branch

Node: mixtureTree.Sympegma_regelii_C3
	Length parameter = 0.06755597175006957
	Class 1
		omega = 0.000
		weight = 0.919
	Class 2
		omega = 1.000
		weight = 0.081
p-value = 0.002849184908457314

Node: mixtureTree.Halothamnus_bottae_C4
	Length parameter = 0.03932806019131349
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node182
	Length parameter = 0.00897147604080485
	Class 1: omega =     0.2967, weight = 1.

Node: mixtureTree.Salsola_rosacea_C4
	Length parameter = 0.01636989682975227
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Noaea_mucronata_C4
	Length parameter = 0.03134422856687116
	Class 1: omega =     0.0852, weight = 1.

Node: mixtureTree.Node190
	Length parameter = 0.019379438164647
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Ofaiston_monandrum_C4
	Length parameter = 0.05550464361295284
	Class 1: omega =     0.1923, weight = 1.

Node: mixtureTree.Node189
	Length parameter = 0.03146391932235711
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Rhaphidophyton_regelii_C3
	Length parameter = 0.01897420633103526
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node188
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Salsola_arbusculiformis_C3
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node187
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Salsola_laricifolia_C3
	Length parameter = 0.01902960293514031
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node186
	Length parameter = 0.009498599024470497
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Anabasis_brevifolia_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Anabasis_truncata_C4
	Length parameter = 0.02862975579393564
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node199
	Length parameter = 0.00953713608313036
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Anabasis_eriopoda_C4
	Length parameter = 0.009552960525970308
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Anabasis_aphylla_C4
	Length parameter = 0.01899730158645016
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Anabasis_salsa_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Anabasis_elatior_C4
	Length parameter = 0.009502262350023785
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node206
	Length parameter = 0.01911517063498629
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node204
	Length parameter = 0.009581674783145235
	Class 1: omega =     0.2779, weight = 1.

Node: mixtureTree.Node202
	Length parameter = 0.01922252113927011
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node198
	Length parameter = 0.01906875415643502
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Girgensohnia_oppositiflora_C4
	Length parameter = 0.05830923520849463
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Halogeton_glomeratus_C4
	Length parameter = 0.0384442689266933
	Class 1: omega =     0.1388, weight = 1.

Node: mixtureTree.Haloxylon_ammodendron_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Haloxylon_persicum_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node215
	Length parameter = 0.03850432992124423
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node213
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node213
	Length parameter = 0.002091891860658099
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3532524787260719

Node: mixtureTree.Node211
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Haloxylon_tamariscifolium_C4
	Length parameter = 0.009542619697205795
	Class 1: omega =     0.2791, weight = 1.

Node: mixtureTree.Horaninovia_ulicina_C4
	Length parameter = 0.08804360215390955
	Class 1: omega =     0.0607, weight = 1.

Node: mixtureTree.Halogeton_arachnoideus_C4
	Length parameter = 0.03834308783103588
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node221
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node221
	Length parameter = 0.00419440928689021
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.2625410017080548

Node: mixtureTree.Node219
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Iljinia_regelii_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node218
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node210
	Length parameter = 0.009631995960984829
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Salsola_foliosa_C4
	Length parameter = 0.05825170439995497
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node209
	Length parameter = 0.019060644733955
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node197
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node185
	Length parameter = 0.04709018803327585
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node181
	Length parameter = 0.01037598050937377
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node155
	Length parameter = 0.00929243151683491
	Class 1: omega =     0.5732, weight = 1.

Node: mixtureTree.Salsola_arbuscula_C4
	Length parameter = 0.009469920846224679
	Class 1: omega =     0.2809, weight = 1.

Node: mixtureTree.Salsola_kali_C4
	Length parameter = 0.00938798847939926
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Salsola_chinghaiensis_C4
	Length parameter = 0.009429515723990263
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Salsola_zaidamica_C4
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Salsola_zaidamica_C4
	Length parameter = 0.002076794199977731
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3528014938119902

Node: mixtureTree.Salsola_komarovii_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Salsola_ruthenica_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node236
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Salsola_collina_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node235
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node233
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node231
	Length parameter = 0.00940243443588335
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Salsola_praecox_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Salsola_pellucida_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Salsola_paulsenii_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node242
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node240
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node230
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node228
	Length parameter = 0.009374656171008839
	Class 1: omega =     0.2838, weight = 1.

Node: mixtureTree.Node226
	Length parameter = 0.04753059244794415
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node154
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node154
	Length parameter = 0.002079756061580664
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3545696300759597

Node: mixtureTree.Salsola_genistoides_C3
	Length parameter = 0.02850107612093609
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node153
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node153
	Length parameter = 0.002084190605897288
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3530985364508795

Node: mixtureTree.Node151
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node115
	Length parameter = 0.09533617538796596
	Class 1: omega =     0.0279, weight = 1.

Node: mixtureTree.Arthrocnemum_macrostachyum_C3
	Length parameter = 0.01914079812378664
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Sarcocornia_utahensis_C3
	Length parameter = 0.02909409230370344
	Class 1: omega =     0.0915, weight = 1.

Node: mixtureTree.Salicornia_europaea_C3
	Length parameter = 0.09783403938506249
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node253
	Length parameter = 0.01906946372049743
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node251
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node251
	Length parameter = 0.004209771168557975
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.264731106492794

Node: mixtureTree.Tecticornia_disarticulata_C3
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Tecticornia_disarticulata_C3
	Length parameter = 0.004187165758554341
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.2613582202912261

Node: mixtureTree.Sclerostegia_moniliformis_C3
	Length parameter = 0.01936520130525401
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node257
	Length parameter = 0.00964973178523645
	Class 1: omega =     0.8294, weight = 1.

Node: mixtureTree.Tecticornia_australasica_C3
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Tecticornia_australasica_C3
	Length parameter = 0.002087387434206626
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3550516324051683

Node: mixtureTree.Salicornia_dolichostachya_C3
	Length parameter = 0.08812271004615199
	Class 1
		omega = 0.039
		weight = 0.993
	Class 2
		omega = 89.221
		weight = 0.007
...Testing for selection at this branch

Node: mixtureTree.Salicornia_dolichostachya_C3
	Length parameter = 0.1122012839340393
	Class 1
		omega = 0.000
		weight = 0.899
	Class 2
		omega = 1.000
		weight = 0.101
p-value = 4.475645189117028e-05

Node: mixtureTree.Halosarcia_indica_C4
	Length parameter = 0.03820638408418829
	Class 1: omega =     0.1394, weight = 1.

Node: mixtureTree.Node263
	Length parameter = 0.05924024217003337
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Pachycornia_triandra_C3
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Pachycornia_triandra_C3
	Length parameter = 0.005018910599253167
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3971400052874772

Node: mixtureTree.Node262
	Length parameter = 0.009592226984335683
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node260
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node256
	Length parameter = 0.009597662920609543
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node250
	Length parameter = 0.01968387143534375
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Halostachys_belangeriana_C3
	Length parameter = 0.009717863933032454
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Halopeplis_amplexicaulis_C3
	Length parameter = 0.03938013554917461
	Class 1: omega =     0.0676, weight = 1.

Node: mixtureTree.Node268
	Length parameter = 0.009567363283981434
	Class 1: omega =     0.5573, weight = 1.

Node: mixtureTree.Kalidium_cuspidatum_C3
	Length parameter = 0.02926222939071641
	Class 1: omega =     0.1825, weight = 1.

Node: mixtureTree.Kalidium_caspicum_C3
	Length parameter = 0.03883450758479062
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Kalidium_foliatum_C3
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node273
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node271
	Length parameter = 0.01961411897464906
	Class 1: omega =     0.1358, weight = 1.

Node: mixtureTree.Node267
	Length parameter = 0.03899809683789515
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node249
	Length parameter = 0.009350733637821117
	Class 1: omega =     0.2199, weight = 1.

Node: mixtureTree.Allenrolfea_occidentalis_C3
	Length parameter = 0.02054197992174844
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 377.306
		weight = 0.005
...Testing for selection at this branch

Node: mixtureTree.Allenrolfea_occidentalis_C3
	Length parameter = 0.03934766261299478
	Class 1
		omega = 0.000
		weight = 0.827
	Class 2
		omega = 1.000
		weight = 0.173
p-value = 6.447292344613498e-06

Node: mixtureTree.Node248
	Length parameter = 0.07334094993624508
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Bienertia_cycloptera_C4
	Length parameter = 0.03289113150108547
	Class 1
		omega = 0.000
		weight = 0.975
	Class 2
		omega = 38.407
		weight = 0.025
...Testing for selection at this branch

Node: mixtureTree.Bienertia_cycloptera_C4
	Length parameter = 0.04397470773689462
	Class 1
		omega = 0.000
		weight = 0.580
	Class 2
		omega = 1.000
		weight = 0.420
p-value = 0.01894504911613343

Node: mixtureTree.Node247
	Length parameter = 0.03788127831234949
	Class 1: omega =     0.0864, weight = 1.

Node: mixtureTree.Suaeda_maritima_C3
	Length parameter = 0.01001854170825592
	Class 1: omega =     0.8047, weight = 1.

Node: mixtureTree.Suaeda_crassifolia_C3
	Length parameter = 0.03912689660993994
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node279
	Length parameter = 0.1544074603980392
	Class 1: omega =     0.0346, weight = 1.

Node: mixtureTree.Suaeda_physophora_C3
	Length parameter = 0.03754136827774286
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Suaeda_microphylla_C4
	Length parameter = 0.03036124268251713
	Class 1: omega =     0.2654, weight = 1.

Node: mixtureTree.Node283
	Length parameter = 0.07932211946240622
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Suaeda_altissima_C4
	Length parameter = 0.1114375396986354
	Class 1: omega =     0.0479, weight = 1.

Node: mixtureTree.Node282
	Length parameter = 0.05736183255194766
	Class 1: omega =     0.0467, weight = 1.

Node: mixtureTree.Node278
	Length parameter = 0.02630792870699173
	Class 1: omega =     0.1013, weight = 1.

Node: mixtureTree.Node246
	Length parameter = 0.07285282743626528
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node114
	Length parameter = 0.07760008124471511
	Class 1: omega =     0.1375, weight = 1.

Node: mixtureTree.Agriophyllum_squarrosum_C3
	Length parameter = 0.08772349920952106
	Class 1: omega =     0.0304, weight = 1.

Node: mixtureTree.Corispermum_filifolium_C3
	Length parameter = 0.07833102399286218
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Anthochlamys_multinervis_C3
	Length parameter = 0.009446226741606879
	Class 1: omega =     0.2827, weight = 1.

Node: mixtureTree.Node289
	Length parameter = 0.05924446044479725
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node287
	Length parameter = 0.02012680236139298
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 1519.686
		weight = 0.005
...Testing for selection at this branch

Node: mixtureTree.Node287
	Length parameter = 0.043290707745702
	Class 1
		omega = 0.000
		weight = 0.874
	Class 2
		omega = 1.000
		weight = 0.126
p-value = 0.001822877048653138

Node: mixtureTree.Node113
	Length parameter = 0.01449434173135214
	Class 1: omega =     0.1841, weight = 1.

Node: mixtureTree.Acroglochin_chenopodioides_C3
	Length parameter = 0.1088458269995762
	Class 1
		omega = 0.000
		weight = 0.984
	Class 2
		omega = 15.447
		weight = 0.016
...Testing for selection at this branch

Node: mixtureTree.Acroglochin_chenopodioides_C3
	Length parameter = 0.1287034011050689
	Class 1
		omega = 0.000
		weight = 0.889
	Class 2
		omega = 1.000
		weight = 0.111
p-value = 0.0117515449659652

Node: mixtureTree.Node112
	Length parameter = 0.01520708962058318
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node30
	Length parameter = 0.02241400274432155
	Class 1: omega =     0.1191, weight = 1.

Node: mixtureTree.Node16
	Length parameter = 0.006824434068994598
	Class 1: omega =     0.3909, weight = 1.

Node: mixtureTree.Monolepis_nuttalliana_C3
	Length parameter = 0.02868876821407665
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Spinacia_oleracea_C3
	Length parameter = 0.194988527299977
	Class 1: omega =     0.0274, weight = 1.

Node: mixtureTree.Node295
	Length parameter = 0.05717366684480991
	Class 1: omega =     0.2823, weight = 1.

Node: mixtureTree.Chenopodium_foliosum_C3
	Length parameter = 0.0187205539331207
	Class 1
		omega = 0.030
		weight = 0.990
	Class 2
		omega = 81.396
		weight = 0.010
...Testing for selection at this branch

Node: mixtureTree.Chenopodium_foliosum_C3
	Length parameter = 0.02848185233887083
	Class 1
		omega = 0.000
		weight = 0.714
	Class 2
		omega = 1.000
		weight = 0.286
p-value = 0.01780629583774107

Node: mixtureTree.Node294
	Length parameter = 0.01884869914243241
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Chenopodium_bonushenricus_C3
	Length parameter = 0.01874742569346725
	Class 1: omega =     0.1425, weight = 1.

Node: mixtureTree.Node293
	Length parameter = 0.009588881596945244
	Class 1: omega =     0.2783, weight = 1.

Node: mixtureTree.Node15
	Length parameter = 0.00933227940615014
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node9
	Length parameter = 0.05664064282533004
	Class 1: omega =     0.0471, weight = 1.

Node: mixtureTree.Chenopodium_coronopus_C3
	Length parameter = 0.03864853984710311
	Class 1
		omega = 0.000
		weight = 0.995
	Class 2
		omega = 128.995
		weight = 0.005
...Testing for selection at this branch

Node: mixtureTree.Chenopodium_coronopus_C3
	Length parameter = 0.04060774543336959
	Class 1
		omega = 0.000
		weight = 0.866
	Class 2
		omega = 1.000
		weight = 0.134
p-value = 0.0332698108034355

Node: mixtureTree.Node8
	Length parameter = 0.0566786835599988
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Microgynoecium_tibeticum_C3
	Length parameter = 0.1177696961637301
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Chenopodium_acuminatum_C3
	Length parameter = 0.009397308212522834
	Class 1: omega =     0.2837, weight = 1.

Node: mixtureTree.Chenopodium_album_C3
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Chenopodium_murale_C3
	Length parameter = 0.009326236394166475
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node309
	Length parameter = 0.02823330411561301
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Chenopodium_sanctaeclarae_C3
	Length parameter = 0.009404680380912842
	Class 1: omega =     0.8527, weight = 1.

Node: mixtureTree.Node308
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node306
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Chenopodium_frutescens_C3
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node305
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Micromonolepis_pusilla_C3
	Length parameter = 0.0377144761621641
	Class 1: omega =     0.0707, weight = 1.

Node: mixtureTree.Node304
	Length parameter = 0.009411322736692967
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Einadia_nutans_C3
	Length parameter = 0.009314625729606958
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Rhagodia_drummondi_C3
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node316
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node316
	Length parameter = 0.004151458373221423
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.2559301712103361

Node: mixtureTree.Chenopodium_desertorum_C3
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Chenopodium_desertorum_C3
	Length parameter = 0.002075845153172484
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3521874183630014

Node: mixtureTree.Chenopodium_auricomum_C3
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Chenopodium_auricomum_C3
	Length parameter = 0.002076456573461026
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3499631369383454

Node: mixtureTree.Node319
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node315
	Length parameter = 0.01877503714650628
	Class 1: omega =     0.1425, weight = 1.

Node: mixtureTree.Node303
	Length parameter = 0.05947510067174491
	Class 1
		omega = 0.000
		weight = 0.991
	Class 2
		omega = 40.083
		weight = 0.009
...Testing for selection at this branch

Node: mixtureTree.Node303
	Length parameter = 0.06931265279385528
	Class 1
		omega = 0.000
		weight = 0.881
	Class 2
		omega = 1.000
		weight = 0.119
p-value = 0.03309783628689328

Node: mixtureTree.Node301
	Length parameter = 0.007581732267017937
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node7
	Length parameter = 0.003952363087742009
	Class 1
		omega = 0.332
		weight = 0.996
	Class 2
		omega = 10000.000
		weight = 0.004
...Testing for selection at this branch

Node: mixtureTree.Node7
	Length parameter = 0.01889622698996755
	Class 1
		omega = 0.000
		weight = 0.715
	Class 2
		omega = 1.000
		weight = 0.285
p-value = 2.34246891637202e-05

Node: mixtureTree.Manochlamys_albicans_C3
	Length parameter = 0.02800960368327348
	Class 1: omega =     0.1904, weight = 1.

Node: mixtureTree.Archiatriplex_nanpinensis_C3
	Length parameter = 0.05693468048897463
	Class 1: omega =     0.0939, weight = 1.

Node: mixtureTree.Node322
	Length parameter = 0.01892300393130717
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node6
	Length parameter = 0.01868592700722821
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node2
	Length parameter = 0.01884628729065568
	Class 1: omega =     0.5692, weight = 1.

Node: mixtureTree.Atriplex_parryi_C4
	Length parameter = 0.009353616305094056
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Atriplex_phyllostegia_C4
	Length parameter = 0.009384818513513997
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Atriplex_serenana_C4
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node332
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Atriplex_powellii_C4
	Length parameter = 0.009407296891916481
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node331
	Length parameter = 0.01881861683517969
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node329
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Atriplex_lampa_C4
	Length parameter = 0.00939177972709508
	Class 1: omega =     0.2838, weight = 1.

Node: mixtureTree.Atriplex_undulata_C4
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Atriplex_undulata_C4
	Length parameter = 0.002079743190138091
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3534561223543733

Node: mixtureTree.Node337
	Length parameter = 0.009391031240344443
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Atriplex_lentiformis_C4
	Length parameter = 0.009375855450593813
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node336
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node328
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node328
	Length parameter = 0.002078294205518562
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3505068991530206

Node: mixtureTree.Atriplex_spongiosa_C4
	Length parameter = 6.274048473917521e-17
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Atriplex_rosea_C4
	Length parameter = 0.01868377740962551
	Class 1: omega =     0.1430, weight = 1.

Node: mixtureTree.Node343
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node343
	Length parameter = 0.002192863066529184
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.3523047156369445

Node: mixtureTree.Atriplex_centralasiatica_C4
	Length parameter = 0.02808832939576348
	Class 1: omega =     0.0950, weight = 1.

Node: mixtureTree.Node342
	Length parameter = 0.009425833340904535
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Atriplex_glauca_C4
	Length parameter = 0.03772962742820162
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node341
	Length parameter = 0.009366471576720914
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node327
	Length parameter = 0.009347914106054801
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Atriplex_coriacea_C4
	Length parameter = 0.02807535492962627
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Node326
	Length parameter = 0
	Class 1: omega =   Infinite, weight = 1.
...Testing for selection at this branch

Node: mixtureTree.Node326
	Length parameter = 0.00415302236495156
	Class 1: omega =     1.0000, weight = 1.
p-value = 0.2568109729318359

Node: mixtureTree.Atriplex_halimus_C4
	Length parameter = 0.009336615111084683
	Class 1: omega =     0.2864, weight = 1.

Node: mixtureTree.Cremnophyton_lanfrancoi_C3
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node349
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node325
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node1
	Length parameter = 0.009330999621866705
	Class 1: omega =     0.0000, weight = 1.

Node: mixtureTree.Atriplex_australasica_C3
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Atriplex_patula_C3
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Node352
	Length parameter = 0
	Class 1: omega =  Undefined, weight = 1.

Node: mixtureTree.Atriplex_aucherii_C3
	Length parameter = 0.01867632400410495
	Class 1: omega =     0.0000, weight = 1.


Summary of branches under episodic selection (355 were tested, of which 50 required optimizations) :
	Allenrolfea_occidentalis_C3 p = 0.002295236074682405
	Amaranthus_hypochondriacus_C4 p = 0.004392127797542555
	Node7 p = 0.008292339963956952
	Salicornia_dolichostachya_C3 p = 0.01579902751758311


 === CPU TIME REPORT === 
	MG94xREV model fit : 00:12:40
	Rate class complexity analysis : 01:05:00
	Adaptive model fit : 00:02:33
	Individual branch selection testing : 06:32:01
	Total time : 07:52:19

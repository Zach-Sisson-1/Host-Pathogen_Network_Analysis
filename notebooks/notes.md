# Network Notes

## 10/8/21

I forked the Repo that Zach made, so I can start working on it myself. 

### <u>Databases</u>

Downloaded all of the hopefully required files from the Databases that were provided to us by Parisa.

Databases:
1. apid
2. proteinatlas
3. string
4. uniprot

------------------------------------------------------------------------------

**protein_atlas**: https://www.proteinatlas.org/search/cell_type_category_rna%3AMacrophages%3BCell+type+enriched%2CGroup+enriched%2CCell+type+enhanced+AND+sort_by%3Atissue+specific+score 

I downloaded all of the genes within macrophages in a tsv.

File: 

Renamed *cell_type_category_rna:Macrophages;Cell+type+enriched,Group+enriched,Cell+type+enhanced+AND+sort_by:tissue+specific+score?format=tsv* 

to 

*proteinatlas_macrophage_genes.tsv*

```
Gene    "Gene synonym"  Ensembl "Gene description"      Uniprot Chromosome      Position        "Protein class" "Biological process"    "Molecular function"    "Disease involvement"   Eviden
CATSPER1        CATSPER ENSG00000175294 "Cation channel sperm associated 1"     Q8NEC5  11      66016752-66026517       "Disease related genes, Predicted membrane proteins"    "Calcium trans
HIST1H1B        "H1.5, H1b, H1F5, H1s-3"        ENSG00000184357 "Histone cluster 1 H1 family member b"  P16401  6       27866849-27867529       "Plasma proteins, Predicted intracellular prot
FCER1A  FCE1A   ENSG00000179639 "Fc fragment of IgE receptor Ia"        P12319  1       159289714-159308224     "FDA approved drug targets, Predicted membrane proteins"                "IgE-b
ADAMDEC1        M12.219 ENSG00000134028 "ADAM like decysin 1"   O15204  8       24384285-24406013       "Plasma proteins, Predicted intracellular proteins, Predicted secreted proteins"
STAC3   MGC2793 ENSG00000185482 "SH3 and cysteine rich domain 3"        Q96MF2  12      57243453-57251193       "Disease related genes, Predicted intracellular proteins"               
```

<u>**APID**</u>: http://cicblade.dep.usal.es:8080/APID/init.action

I downloaded the Level 2 interactomes for Homo sapiens (binary interactomes)

File: *9606_Q1.txt*

File Preview:
```
InteractionID   UniprotID_A     UniprotName_A   GeneName_A      UniprotID_B     UniprotName_B   GeneName_B
1495672 A0A024R0Y4      A0A024R0Y4_HUMAN        TADA2A  Q8WWY3  PRP31_HUMAN     PRPF31  1       3       1
1591599 A0A024R4B0      A0A024R4B0_HUMAN        SPATA3  O15354  GPR37_HUMAN     GPR37   1       3       1
1532709 A0A024R4Q5      A0A024R4Q5_HUMAN        TFPT    Q96D03  DDT4L_HUMAN     DDIT4L  1       2       1
1532710 A0A024R4Q5      A0A024R4Q5_HUMAN        TFPT    P51911  CNN1_HUMAN      CNN1    1       2       1
1714250 A0A024R6G0      A0A024R6G0_HUMAN        TCL6    P50222  MEOX2_HUMAN     MEOX2   1       3       1
2014506 A0A024R9H7      A0A024R9H7_HUMAN        CCDC26  P60409  KR107_HUMAN     KRTAP10-7       1       1

```


**string**: https://string-db.org/cgi/download?sessionId=%24input-%3E%7BsessionId%7D&species_text=Homo+sapiens

I downloaded 2 files from the String database.
1. *9606.protein.links.full.v11.5.txt.gz* (Interaction Data)
```
protein1 protein2 neighborhood neighborhood_transferred fusion cooccurence homology coexpression coexpression_t
9606.ENSP00000000233 9606.ENSP00000379496 0 0 0 0 0 0 54 0 0 0 0 103 85 155
9606.ENSP00000000233 9606.ENSP00000314067 0 0 0 0 0 0 0 0 180 0 0 0 61 197
9606.ENSP00000000233 9606.ENSP00000263116 0 0 0 0 0 0 62 0 152 0 0 0 101 222
9606.ENSP00000000233 9606.ENSP00000361263 0 0 0 0 0 0 0 0 161 0 0 47 58 181
9606.ENSP00000000233 9606.ENSP00000409666 0 0 0 0 0 60 63 0 213 0 0 0 72 270

```
2. *9606.protein.sequences.v11.5.fa.gz* (Accessory Data)
```
>9606.ENSP00000000233
MGLTVSALFSRIFGKKQMRILMVGLDAAGKTTILYKLKLGEIVTTIPTIGFNVETVEYKNICFTVWDVGGQDKIRPLWRH
YFQNTQGLIFVVDSNDRERVQESADELQKMLQEDELRDAVLLVFANKQDMPNAMPVSELTDKLGLQHLRSRTWYVQATCA
TQGTGLYDGLDWLSHELSKR
>9606.ENSP00000000412
MFPFYSCWRTGLLLLLLAVAVRESWQTEEKTCDLVGEKGKESEKELALVKRLKPLFNKSFESTVGQGSDTYIYIFRVCRE
AGNHTSGAGLVQINKSNGKETVVGRLNETHIFNGSNWIMLIYKGGDEYDNHCGKEQRRAVVMISCNRHTLADNFNPVSEE
RGKVQDCFYLFEMDSSLACSPEISHLSVGSILLVTFASLVAVYVVGGFLYQRLVVGAKGMEQFPHLAFWQDLGNLVADGC
DFVCRSKPRNVPAAYRGVGDDQLGEESEERDDHLLPM
>9606.ENSP00000001008
MTAEEMKATESGAQSAPLPMEGVDISPKQDEGVLKVIKREGTGTEMPMIGDRVFVHYTGWLLDGTKFDSSLDRKDKFSFD
LGKGEVIKAWDIAIATMKVGEVCHITCKPEYAYGSAGSPPKIPPNATLVFEVELFEFKGEDLTEEEDGGIIRRIQTRGEG
YAKPNEGAIVEVALEGYYKDKLFDQRELRFEIGEGENLDLPYGLERAIQRMEKGEHSIVYLKPSYAFGSVGKEKFQIPPN
AELKYELHLKSFEKAKESWEMNSEEKLEQSTIVKERGTVYFKEGKYKQALLQYKKIVSWLEYESSFSNEEAQKAQALRLA
SHLNLAMCHLKLQAFSAAIESCNKALELDSNNEKGLFRRGEAHLAVNDFELARADFQKVLQLYPNNKAAKTQLAVCQQRI
RRQLAREKKLYANMFERLAEEENKAKAEASSGDHPTDTEMKEEQKSNTAGSQSQVETEA
```
**uniprot**: https://www.uniprot.org/uniprot/?query=homo+sapiens&sort=score

I downloaded the 'homo sapiens' proteins file:

File: *uniprot-homo+sapiens.fasta.gz*

### Exploratory Analysis 

```
# Check what different species are in the uniprot file
gzcat uniprot-homo+sapiens.fasta.gz | grep "^>" | cut -d "|" -f3 | cut -d " " -f1 | cut -d "_" -f2 | sort | uniq -c | sort -n 

# Small subset of the tail output
8799 HHV1
9225 9INFB
10195 EBVG
13805 HE71
14734 HRSV
16468 HEV
16607 HCMV
75730 SARS2
138569 HBV
202186 HUMAN
1077900 9HIV1
```


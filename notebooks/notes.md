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
# Will not show all columns as this is a copy and paste of less -S

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

```
# Will not show all columns as this is a copy and paste of less -S
less -S

Entry   Entry name      Protein names   Gene names      Organism        Intramembrane   Subcellular location [CC]       Topological domain      Transmembrane   Gene ontology (biological process)      Gene o
Q53XC5  Q53XC5_HUMAN    Bone morphogenetic protein 4 (Bone morphogenetic protein 4, isoform CRA_a) (Full-length cDNA clone CS0DC002YH22 of Neuroblastoma of Homo sapiens (human)) (Full-length cDNA clone CS0D
A8K571  A8K571_HUMAN    Bone morphogenetic protein 7 (Osteogenic protein 1), isoform CRA_b (cDNA FLJ78019, highly similar to Homo sapiens bone morphogenetic protein 7 (osteogenic protein 1), mRNA) (cDNA, FL
A8K660  A8K660_HUMAN    Adiponectin (Adiponectin, C1Q and collagen domain containing) (cDNA FLJ78108, highly similar to Homo sapiens adiponectin, C1Q and collagen domain containing (ADIPOQ), mRNA)    ADIPOQ
Q5U0J5  Q5U0J5_HUMAN    cAMP responsive element binding protein 1 (cAMP responsive element binding protein 1, isoform CRA_a) (cDNA, FLJ93156, Homo sapiens cAMP responsive element binding protein 1 (CREB1),t
```

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


## 10/9/21

### Jupyter Notebook

First I created a conda env to house the necessary tools I will need for this project.

```
# Env create command
conda create --name network_uo python=3.9 numpy pandas

# Install jupyter notebooks
conda activate network_uo
conda install jupyter notebooks

# Env Versions
conda list
# packages in environment at /Users/andrewpowers/miniconda3/envs/network_uo:
#
# Name                    Version                   Build  Channel
appnope                   0.1.2            py39h6e9494a_1    conda-forge
argon2-cffi               20.1.0           py39h9ed2024_1  
async_generator           1.10               pyhd3eb1b0_0  
attrs                     21.2.0             pyhd3eb1b0_0  
backcall                  0.2.0              pyh9f0ad1d_0    conda-forge
backports                 1.0                        py_2    conda-forge
backports.functools_lru_cache 1.6.4              pyhd8ed1ab_0    conda-forge
blas                      1.0                         mkl  
bleach                    4.0.0              pyhd3eb1b0_0  
bottleneck                1.3.2            py39he3068b8_1  
ca-certificates           2021.9.30            hecd8cb5_1  
certifi                   2021.5.30        py39hecd8cb5_0  
cffi                      1.14.6           py39h2125817_0  
debugpy                   1.4.1            py39h9fcab8e_0    conda-forge
decorator                 5.1.0              pyhd8ed1ab_0    conda-forge
defusedxml                0.7.1              pyhd3eb1b0_0  
entrypoints               0.3             pyhd8ed1ab_1003    conda-forge
icu                       58.2                 h0a44026_3  
importlib-metadata        4.8.1            py39hecd8cb5_0  
importlib_metadata        4.8.1                hd3eb1b0_0  
intel-openmp              2021.3.0          hecd8cb5_3375  
ipykernel                 6.4.1            py39h71a6800_0    conda-forge
ipython                   7.28.0           py39h71a6800_0    conda-forge
ipython_genutils          0.2.0                      py_1    conda-forge
ipywidgets                7.6.4              pyhd3eb1b0_0  
jedi                      0.18.0           py39h6e9494a_2    conda-forge
jinja2                    3.0.1              pyhd3eb1b0_0  
jpeg                      9d                   h9ed2024_0  
jsonschema                3.2.0              pyhd3eb1b0_2  
jupyter                   1.0.0            py39hecd8cb5_7  
jupyter_client            7.0.6              pyhd8ed1ab_0    conda-forge
jupyter_console           6.4.0              pyhd3eb1b0_0  
jupyter_core              4.8.1            py39h6e9494a_0    conda-forge
jupyterlab_pygments       0.1.2                      py_0  
jupyterlab_widgets        1.0.0              pyhd3eb1b0_1  
libcxx                    12.0.0               h2f01273_0  
libffi                    3.3                  hb1e8313_2  
libpng                    1.6.37               ha441bb4_0  
libsodium                 1.0.18               hbcb3906_1    conda-forge
markupsafe                2.0.1            py39h9ed2024_0  
matplotlib-inline         0.1.3              pyhd8ed1ab_0    conda-forge
mistune                   0.8.4           py39h9ed2024_1000  
mkl                       2021.3.0           hecd8cb5_517  
mkl-service               2.4.0            py39h9ed2024_0  
mkl_fft                   1.3.0            py39h4a7008c_2  
mkl_random                1.2.2            py39hb2f4e1b_0  
nbclient                  0.5.3              pyhd3eb1b0_0  
nbconvert                 6.1.0            py39hecd8cb5_0  
nbformat                  5.1.3              pyhd3eb1b0_0  
ncurses                   6.2                  h0a44026_1  
nest-asyncio              1.5.1              pyhd8ed1ab_0    conda-forge
notebook                  6.4.3            py39hecd8cb5_0  
numexpr                   2.7.3            py39h5873af2_1  
numpy                     1.20.3           py39h4b4dc7a_0  
numpy-base                1.20.3           py39he0bd621_0  
openssl                   1.1.1l               h9ed2024_0  
packaging                 21.0               pyhd3eb1b0_0  
pandas                    1.3.3            py39h5008ddb_0  
pandocfilters             1.4.3            py39hecd8cb5_1  
parso                     0.8.2              pyhd8ed1ab_0    conda-forge
pexpect                   4.8.0              pyh9f0ad1d_2    conda-forge
pickleshare               0.7.5                   py_1003    conda-forge
pip                       21.2.4           py39hecd8cb5_0  
prometheus_client         0.11.0             pyhd3eb1b0_0  
prompt-toolkit            3.0.20             pyha770c72_0    conda-forge
prompt_toolkit            3.0.20               hd3eb1b0_0  
ptyprocess                0.7.0              pyhd3deb0d_0    conda-forge
pycparser                 2.20                       py_2  
pygments                  2.10.0             pyhd8ed1ab_0    conda-forge
pyparsing                 2.4.7              pyhd3eb1b0_0  
pyqt                      5.9.2            py39h23ab428_6  
pyrsistent                0.18.0           py39h9ed2024_0  
python                    3.9.7                h88f2d9e_1  
python-dateutil           2.8.2              pyhd3eb1b0_0  
python_abi                3.9                      2_cp39    conda-forge
pytz                      2021.1             pyhd3eb1b0_0  
pyzmq                     22.3.0           py39h7fec2f1_0    conda-forge
qt                        5.9.7                h468cd18_1  
qtconsole                 5.1.1              pyhd3eb1b0_0  
qtpy                      1.10.0             pyhd3eb1b0_0  
readline                  8.1                  h9ed2024_0  
send2trash                1.8.0              pyhd3eb1b0_1  
setuptools                58.0.4           py39hecd8cb5_0  
sip                       4.19.13          py39h23ab428_0  
six                       1.16.0             pyhd3eb1b0_0  
sqlite                    3.36.0               hce871da_0  
terminado                 0.9.4            py39hecd8cb5_0  
testpath                  0.5.0              pyhd3eb1b0_0  
tk                        8.6.11               h7bc2e8c_0  
tornado                   6.1              py39h89e85a6_1    conda-forge
traitlets                 5.1.0              pyhd8ed1ab_0    conda-forge
tzdata                    2021a                h5d7bf9c_0  
wcwidth                   0.2.5              pyh9f0ad1d_2    conda-forge
webencodings              0.5.1            py39hecd8cb5_1  
wheel                     0.37.0             pyhd3eb1b0_1  
widgetsnbextension        3.5.1            py39hecd8cb5_0  
xz                        5.2.5                h1de35cc_0  
zeromq                    4.3.4                he49afe7_1    conda-forge
zipp                      3.6.0              pyhd3eb1b0_0  
zlib                      1.2.11               h1de35cc_3  
```

After creating the environment and setting up the packages. I created a jupyter file *exploratory_work.ipynb* in the jupyter_notebooks folder.

This will be a jupyter notebookt that I can play around with and try to discover ways of merging the database files into one dataframe.

I realized while I was working that the string database file *9606.protein.links.full.v11.5.txt.gz* has protein_ids in them. I remembered that I could go onto Ensembl and download the pep file that would have all of the protein_ids and the gene names. 

So what i did was make a dictionary with the protein_ids as the keys and the gene names as the values. This dict was then used to created columns in the string database file *9606.protein.links.full.v11.5.txt.gz* `gene1` and `gene2` this way I can combine files on just the gene names if they only have them in their files. 


**Ensembl Data**: http://ftp.ensembl.org/pub/release-104/fasta/homo_sapiens/pep/

File: *Homo_sapiens.GRCh38.pep.all.fa.gz*

```
>ENSP00000488240.1 pep chromosome:GRCh38:CHR_HSCHR7_2_CTG6:142847306:142847317:1 gene:ENSG00000282253.1 transcript:ENST00000631435.1 gene_biotype:TR_D_gene transcript_biotype:TR_D_gene gene_symbol:TRBD1 description:T cell receptor beta diversity 1 [Source:HGNC Symbol;Acc:HGNC:12158]
GTGG
>ENSP00000451042.1 pep chromosome:GRCh38:14:22438547:22438554:1 gene:ENSG00000223997.1 transcript:ENST00000415118.1 gene_biotype:TR_D_gene transcript_biotype:TR_D_gene gene_symbol:TRDD1 description:T cell receptor delta diversity 1 [Source:HGNC Symbol;Acc:HGNC:12254]
EI
>ENSP00000452494.1 pep chromosome:GRCh38:14:22449113:22449125:1 gene:ENSG00000228985.1 transcript:ENST00000448914.1 gene_biotype:TR_D_gene transcript_biotype:TR_D_gene gene_symbol:TRDD3 description:T cell receptor delta diversity 3 [Source:HGNC Symbol;Acc:HGNC:12256]
TGGY
>ENSP00000451515.1 pep chromosome:GRCh38:14:22439007:22439015:1 gene:ENSG00000237235.2 transcript:ENST00000434970.2 gene_biotype:TR_D_gene transcript_biotype:TR_D_gene gene_symbol:TRDD2 description:T cell receptor delta diversity 2 [Source:HGNC Symbol;Acc:HGNC:12255]
PSY
>ENSP00000487941.1 pep chromosome:GRCh38:7:142786213:142786224:1 gene:ENSG00000282431.1 transcript:ENST00000632684.1 gene_biotype:TR_D_gene transcript_biotype:TR_D_gene gene_symbol:TRBD1 description:T cell receptor beta diversity 1 [Source:HGNC Symbol;Acc:HGNC:12158]
GTGG
```

I used this to combine majority of the other dataframes with the string dataframe. 

However, after talking with V. It seems that we don'ot actually need to use STRING as the APID data has UniprotIDs.
So I will create another Jupyter notebook called *database_merging.ipynb*. 

I will write out in a Markdown fashion how to combine the 3 dataframes together. 

I also uploaded the `network_uo` conda environment to my kernel.
```
# Download the ipykernel package
conda install ipykernel
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /Users/andrewpowers/miniconda3/envs/network_uo

  added / updated specs:
    - ipykernel


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ipykernel-6.4.1            |   py39hecd8cb5_1         194 KB
    ------------------------------------------------------------
                                           Total:         194 KB

The following packages will be UPDATED:

  ipykernel          conda-forge::ipykernel-6.4.1-py39h71a~ --> pkgs/main::ipykernel-6.4.1-py39hecd8cb5_1


Proceed ([y]/n)? y


Downloading and Extracting Packages
ipykernel-6.4.1      | 194 KB    | ################################################################################################################################################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done


# Upload to the kernel
python -m ipykernel install --user --name=network_uo
Installed kernelspec network_uo in ~/Library/Jupyter/kernels/network_uo
```

Uploaded the final version to github and asked Dr. Hosseinzadeh to look over the file.

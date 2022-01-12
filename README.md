# **A Network Analysis of Host-Pathogen Interactions**
### Authored by Andrew Powers, Zach Sisson, and Vandana Reddy

# Introduction and Goals:
While not a large problem, in the United States, Tuberculosis is still incredibly prevalent in other areas of the world. Tuberculosis is caused by the bacteria, *Mycobacteria tuberculosis* (Mtb). A total of 1.5 million people died from Tuberculosis in 2020 and worldwide, Tuberculosis is the 13th leading cause of death and the second leading infectious killer after the COVID-19 virus. 

Tuberculosis is spread through the air and infection begins when the bacteria enters the hosts’ lungs and infects the alveolar air sacs, specifically the alveolar macrophages. Macrophages are special immune cells that are tasked with the detection, destruction, and clearing of bacteria and other infections. While the macrophages try to clear the bacteria, it can actually survive and reproduce in the macrophage, killing the immune cell and spreading to nearby epithelial and endothelial cells. 

Currently, there are 4 main first line drugs used to combat Tuberculosis infections, isoniazid (INH), rifampin (RIF), ethambutol (EMB), and pyrazinamide (PZA). The majority of normal infections, like those that happen in healthy, non-immunocompromised people can be treated with these medications, but they are quite expensive and the regime is very long. The bigger problem comes from drug resistance in Tuberculosis, specifically extensively drug resistant Tuberculosis that is resistant to most treatments created against the bacteria. While it is only estimated to be a small part of the current Tuberculosis burden worldwide, experts expect that number to grow with time. 

Because the drugs we regularly use to treat Tuberculosis infections have been in use for almost 5 decades, we desperately need new treatments against the bacteria. To be able to do that, we need to first better understand how the Tuberculosis bacteria infects humans. Given this, **our overall goal of this project** is to develop a workflow that will enable us to 
**1)** Better understand the protein interactions that exist between Mtb and human proteins found within the macrophage. 
**2)** Identify key protein interactions and network features that reveal, to some extent, the impact that *M. tuberculosis* is having on the macrophage protein network as well as provide a list of potential drug targets.
**3)** Implement graph neural networks to predict novel protein interactions within the network.

# Workflow:
The project was broken into four main parts with the following file structure:

Part 1: Notebooks > Network_Construction <br />
Part 2: Notebooks > Whole_Network_Analysis <br />
Part 3: Notebooks > Subnetwork_Construction, Notebooks > Subnetwork_Analysis <br />
Part 4: Edge_Prediction <br \>

# **Part 1 - Constructing The Protein Networks**
First, the healthy and diseased macrophage protein-protein interaction networks must be constructd. The notebook titled **Network_Construction** under **Notebooks** provides this workflow.

First, we first needed to prepare the data to construct the networks. From the [APID database](http://cicblade.dep.usal.es:8080/APID/init.action), we got a list of all the binary protein interactions in a human cell and combined that with information from [Uniprot database](https://www.uniprot.org/uniprot/?query=proteome:UP000005640), that has specific protein infomation like subcellular location and function. Because the Tuberculosis bacteria infects macrophages, we filtered this list to only include those proteins expressed in macrophages using the [Protein Atlas database](https://www.proteinatlas.org/humanproteome/single+cell+type/blood+%26+immune+cells#macrophages). This gave us the list of all the Protein-Protein Interactions in macrophage cells. 

From the paper 'An Mtb-Human Protein-Protein Interaction Map Identifies a Switch between Host Antiviral and Antibacterial Responses' from *Molecular Cell*, we got the Tuberculosis proteins that interact with these macrophage proteins. We visualized both the healthy protein and the diseased protein networks. 

# **Part 2 - Whole Network Analysis**
Once the healthy and diseased networks were constructed, we began by comparing network features between the healthy and diseased networks, looking primarily at measures of centrality and community composition. The code and conlusions for this analysis can be found in **Whole_Network_Analysis** under **Notebooks**

# **Part 3 - Subnetwork Analysis**
With the entire network containing a lot of noise, we chose to focus our analysis on the second degree subnetwork. The code for creating these subnetworks (both healthy and diseased) can be found in **Subnetwork_Construction** under **Notebooks**. The code for the comparison and analysis of these subnetworks can be found in **Subnetwork_Analysis** under **Notebooks**.

# **Part 4 - Edge Predicton**

# **Next Steps**
Currently, we are working on utilizing alphafold and rostta tp 

- Using Alphafold and Rosetta to examine protein interactions and identify ligand binding sites  


- Using Spektral to perform node prediction

# **A Network Analysis of Host-Pathogen Interactions**
### Authored by Andrew Powers, Zach Sisson, and Vandana Reddy

### Workflow
Part 1: Notebooks > Network_Construction
Part 2: Notebooks > Whole_Network_Analysis
Part 3: Notebooks > Subnetwork_Construction
        Notebooks > Subnetwork_Analysis


### Mini Abstract Here
# Introduction:
While not a large problem, in the United States, Tuberculosis is still incredibly prevalent in other areas of the world. Tuberculosis is caused by the bacteria, *Mycobacteria tuberculosis*. A total of 1.5 million people died from Tuberculosis in 2020 and worldwide, Tuberculosis is the 13th leading cause of death and the second leading infectious killer after the COVID-19 virus. 

Tuberculosis is spread through the air and infection begins when the bacteria enters the hosts’ lungs and infects the alveolar air sacs, specifically the alveolar macrophages. Macrophages are special immune cells that are tasked with the detection, destruction, and clearing of bacteria and other infections. While the macrophages try to clear the bacteria, it can actually survive and reproduce in the macrophage, killing the immune cell and spreading to nearby epithelial and endothelial cells. 

Currently, there are 4 main first line drugs used to combat Tuberculosis infections, isoniazid (INH), rifampin (RIF), ethambutol (EMB), and pyrazinamide (PZA). The majority of normal infections, like those that happen in healthy, non-immunocompromised people can be treated with these medications, but they are quite expensive and the regime is very long. The bigger problem comes from drug resistance in Tuberculosis, specifically extensively drug resistant Tuberculosis that is resistant to most treatments created against the bacteria. While it is only estimated to be a small part of the current Tuberculosis burden worldwide, experts expect that number to grow with time. 

Because the drugs we regularly use to treat Tuberculosis infections have been in use for almost 5 decades, we desperately need new treatments against the bacteria. To be able to do that, we need to first better understand how the Tuberculosis bacteria infects humans. That is the overall goal of our project, to better understand the protein interactions between Tuberculosis proteins and the proteins of a macrophage cell, the cell that *M. tuberculosis* infects. By better understanding the network of interactions, we can hopefully find new drug targets. 

# **Part 1 - Constructing The Protein Networks**
First, the healthy and diseased macrophage protein-protein interaction networks must be constructd. The notebook titled **Network_Construction** under **Notebooks** provides this workflow.

First, we first needed to prepare the data to construct the networks. From the [APID database] (http://cicblade.dep.usal.es:8080/APID/init.action), we got a list of all the binary protein interactions in a human cell and combined that with information from Uniport database [https://www.uniprot.org/uniprot/?query=proteome:UP000005640], that has specific protein infomation like subcellular location and function. Because the Tuberculosis bacteria infects macrophages, we filtered this list to only include those proteins expressed in macrophages using the Protein Atlas database [https://www.proteinatlas.org/humanproteome/single+cell+type/blood+%26+immune+cells#macrophages]. This gave us the list of all the Protein-Protein Interactions in macrophage cells. 

Using a paper from *Molecular Cell*, we got the Tuberculosis proteins that interact with these macrophage proteins. We visualized both the healthy protein and the diseased protein networks. 

# **Part 2 - Whole Network Analysis**
Once the healthy and diseased networks were constructed, we began by comparing network features between the healthy and diseased networks, looking primarily at measures of centrality and community composition. The code for this analysis can be found in **Whole_Network_Analysis** under **Notebooks**
# **Part 3 - Subnetwork Analysis**
With the entire network containing a lot of noise, we chose to focus our analysis on the second degree subnetwork. The code for creating these subnetworks (both healthy and diseased) can be found in **Subnetwork_Construction** under **Notebooks**. The code for the comparison and analysis of these subnetworks can be found in **Subnetwork_Analysis** under **Notebooks**.
# **Part 4 - Edge Predicton**
# Part 5 - Exploration of Protein Interactions using Alphafold 
# **Concluding Remarks and Next Steps**
- Using Spektral to perform node prediction
# **A Network Analysis of Host-Pathogen Interactions**
### Authored by Andrew Powers, Zach Sisson, and Vandana Reddy
### Mini Abstract Here
# Introduction:
While not a large problem, in the United States, Tuberculosis is still incredibly prevalent in other areas of the world. Tuberculosis is caused by the bacteria, *Mycobacteria tuberculosis*. A total of 1.5 million people died from Tuberculosis in 2020 and worldwide, Tuberculosis is the 13th leading cause of death and the second leading infectious killer after the COVID-19 virus. 
Tuberculosis is spread through the air and infection begins when the bacteria enters the hosts’ lungs and infects the alveolar air sacs, specifically the alveolar macrophages. Macrophages are special immune cells that are tasked with the detection, destruction, and clearing of bacteria and other infections. While the macrophages try to clear the bacteria, it can actually survive and reproduce in the macrophage, killing the immune cell and spreading to nearby epithelial and endothelial cells. 
Currently, there are 4 main first line drugs used to combat Tuberculosis infections, isoniazid (INH), rifampin (RIF), ethambutol (EMB), and pyrazinamide (PZA). The majority of normal infections, like those that happen in healthy, non-immunocompromised people can be treated with these medications, but they are quite expensive and the regime is very long. The bigger problem comes from drug resistance in Tuberculosis, specifically extensively drug resistant Tuberculosis that is resistant to most treatments created against the bacteria. While it is only estimated to be a small part of the current Tuberculosis burden worldwide, experts expect that number to grow with time. 

Currently, There is a vaccine but it is not very effective and the only treatment is long and difficult. As a result, we desperately need new tools to help battle the infection. The issue is that the mechanism by which mycobacteria infects human cells is not very well understood. Many of the specifics for this process are not yet known, making it hard to develop any therapeutics against this bacterial infection. The ultimate goal for this project is to better understand the pathogenesis of mycobacteria and find possible targets for new therapeutics using a protein-protein interaction network yada yada, our goal and rationale for this project
# **Part 1 - Constructing The Protein Networks**
First, the healthy and diseased macrophage protein-protein interaction networks must be constructd. The notebook titled **Network_Construction** under **Notebooks** provides this workflow.
# **Part 2 - Whole Network Analysis**
Once the healthy and diseased networks were constructed, we began by comparing network features between the healthy and diseased networks, looking primarily at measures of centrality and community composition. The code for this analysis can be found in **Whole_Network_Analysis** under **Notebooks**
# **Part 3 - Subnetwork Analysis**
With the entire network containing a lot of noise, we chose to focus our analysis on the second degree subnetwork. The code for creating these subnetworks (both healthy and diseased) can be found in **Subnetwork_Construction** under **Notebooks**. The code for the comparison and analysis of these subnetworks can be found in **Subnetwork_Analysis** under **Notebooks**.
# **Part 4 - Edge Predicton**
# Part 5 - Exploration of Protein Interactions using Alphafold 
# **Concluding Remarks and Next Steps**

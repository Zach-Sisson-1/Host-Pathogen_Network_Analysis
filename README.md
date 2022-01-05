# **A Network Analysis of Host-Pathogen Interactions**
### Authored by Andrew Powers, Zach Sisson, and Vandana Reddy
### Mini Abstract Here
# Introduction:
While not a large problem, in the United States, Tuberculosis is still incredibly prevalent in other areas of the world. Mycobacteria tuberculosis, the bacteria that causes tuberculosis, is still the leading cause of infectious disease deaths in the world, killing 1.5 million people a year. TB is spread through the air and infection begins when the bacteria enters the hosts’ lungs and infects the alveolar air sacs, specifically the alveolar macrophages. Macrophages are special immune cells that are tasked with the detection, destruction, and clearing of bacteria and other infections. While the macrophages try to kill the mycobacteria by phagocytosis and with reactive oxygen species, the bacteria can actually survive and reproduce in the macrophage, killing the immune cell and spreading to nearby epithelial and endothelial cells. There is a vaccine but it is not very effective and the only treatment is long and difficult. As a result, we desperately need new tools to help battle the infection. The issue is that the mechanism by which mycobacteria infects human cells is not very well understood. Many of the specifics for this process are not yet known, making it hard to develop any therapeutics against this bacterial infection. The ultimate goal for this project is to better understand the pathogenesis of mycobacteria and find possible targets for new therapeutics using a protein-protein interaction network yada yada, our goal and rationale for this project
# **Part 1 - Constructing The Protein Networks**
First, the healthy and diseased macrophage protein-protein interaction networks must be constructd. The notebook titled **Network_Construction** under **Notebooks** provides this workflow.
# **Part 2 - Whole Network Analysis**
Once the healthy and diseased networks were constructed, we began by comparing network features between the healthy and diseased networks, looking primarily at measures of centrality and community composition. The code for this analysis can be found in **Whole_Network_Analysis** under **Notebooks**
# **Part 3 - Subnetwork Analysis**
With the entire network containing a lot of noise, we chose to focus our analysis on the second degree subnetwork. The code for creating these subnetworks (both healthy and diseased) can be found in **Subnetwork_Construction** under **Notebooks**. The code for the comparison and analysis of these subnetworks can be found in **Subnetwork_Analysis** under **Notebooks**.
# **Part 4 - Edge Predicton**
# Part 5 - Exploration of Protein Interactions using Alphafold 
# **Concluding Remarks and Next Steps**

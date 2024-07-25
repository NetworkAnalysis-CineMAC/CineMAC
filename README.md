# CineMAC
Repository for the Network Analysis project within the MA course of "Digital Humanities and Digital Knowledge"


## About <a name = "about"></a>

Project CineMAC is a network analysis project that aims to study the influence, trends and patterns of cinematic production through the creation and analysis of a network of film citations, and a corresponding network consisting of various film agents. Unlike previous studies that failed to stress the domination of the USA cinematic industry in the available data, our project addresses the power asymmetries underlying the present westernised vision of cinematic history, undermining the role of East-Asian artistic influence.

To this scope, we modelled two networks comprised of information on film citations and related agents (e.g. actors, directors), respectively.  Several network analysis techniques were used, each addressing a specific way of assessing a film’s potential impact and surrounding agents in the history of cinematic production. 
The entire documentation of the project can be found at the project report <a href="https://github.com/NetworkAnalysis-CineMAC/CineMAC/blob/main/CineMAC-ProjectProposal1.pdf"> here</a>.


## Contributions

• The creation of a long-term impact rank that assesses USA and East Asian films according to their influence in Cinema History.
• A general long-term impact film rank where the representation of East Asian cinema is more weighted and balanced.
• The individuation of central figures in transnational film production collaboration to assess how production with transnational teams relates to the success of the film, and to what extent it agrees with the most famous ranks used to measure film success.


 ## Data
The project’s data is acquired by the Internet Movie Database, which provides datasets in tab-separated values format, freely accessible on their dedicated <a href="https://developer.imdb.com/non-commercial-datasets/">website</a> for non-commercial use.

## Details
## <a href="https://github.com/NetworkAnalysis-CineMAC/CineMAC/tree/main/src/scripts">Scripts folder</a>

+ [Data description; cleaning and processing for both graphs/networks]
+ [Graph Modelling for <a href = "https://github.com/NetworkAnalysis-CineMAC/CineMAC/blob/main/src/scripts/graph1_modelling.ipynb">Network of Citations</a> and Network of Agents](#materials)
+ [Network Analysis for both graphs:  In-Degree, Out-Degree and EigenVector Centrality, Closeness and Betweenness Centrality, Clustering Coefficient, PageRank and Louvain Community Detection Algorithm).
## Graph files folder:

+ [Final data used for graph modelling (zipped csv)]
+ [Graph files in edgelist and gexf format (used for visualisation w/ open software Gephi)]

## Results folder
Results of all the measures used for Network Analysis

For a more comprehensive documentation of the project, please consult the CineMAC report.


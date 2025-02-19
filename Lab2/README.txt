Community Detection Metrics for METIS Graphs

Overview
This script processes graph partitioning results. main.py is for graphs from .metis datasets, and mainForCNM.py
is for graph datasets and partitions made from .txt files. Both files have the same functionality and structure, 
but just handle either graphs from .metis or from .txt files. The output results from these files can be manually
loaded into CorrelationHeatmap.py to create the visualization of the correlation matrix.  

Key community detection metrics evaluated:
1. Modularity: Measures the strength of community structure.
2. Conductance: Evaluates the separation between communities.
3. Normalized Cut (NCut): Assesses inter-community edge connectivity.

Features

- Reads METIS-formatted graph files and partitions.
- Computes modularity, conductance, and normalized cut for different partitioning methods.
- Supports multiple partitioning results for comparison.

Usage
- Running the Script:
    python script.py

The script is currently set up to process the p2p-Gnutella08 graph dataset, but you can modify the paths in the compute_metrics function to analyze other graphs.

Example Function Calls:
compute_metrics(
"path/to/graph.metis",
"path/to/partition1.metis.part", ## One partition method using .metis
"path/to/partition2.metis.part"  ## Another partition method using .metis
)

Dependencies:
- Python 3.x
- NetworkX

Install dependencies using:
pip install networkx

Output Metrics (for each partitioning method): 
- modularity, 
- conductance 
- ncut score

CorrelationHeatmap.py Usage:
- Load the scores in manually to visualize the correlation matrix of the graph Measures
- Example Implementation:
metrics_results = {
    "CNM": {"modularity": 0.8160, "conductance": 0.0175, "ncut": 0.0002},
    "MLRMCL": {"modularity": 0.7427413738676999, "conductance": 0.1738296615132966, "ncut": 0.17415314672067236},
    "GPMetis": {"modularity": 0.3461386598176384, "conductance": 0.48873626632514905, "ncut": 0.4896096516715551}
}

For the YouTube dataset 
(inputs and outputs same format as the others, requires a graph and partition result(s) as inputs)

Files:
mainYT.py
    - Runs the YouTube dataset to calculate entropy of MLRMCL and GPMetis .metis partition results
mainYT_CNM.py
    - Runs the YouTube dataset to calculate entropy of the CNM output .txt partition results

Author:
- Sal Hargis
- Developed for CSE5245 Lab 2.

Modify the script paths as needed to run on different network datasets.


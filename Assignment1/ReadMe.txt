Lab 1 for CSE 5245 Network Science
=========================

This project performs centrality analysis on four provided datasets, using various centrality measures such as degree centrality, closeness centrality, betweenness centrality, eigenvector centrality, PageRank, and clustering coefficient. The results are saved to a CSV file, and correlations between these measures are analyzed and visualized using a heatmap.
In order to run this, you will need to specify the pathway to the network data for the network you wish to analyze, the code will execute one network analysis at a time.

Features
--------
- Load a graph from an raw data file
- Compute centrality measures for each node
- Save the centrality measures to a CSV file
- Analyze correlations between centrality metrics
- Visualize the correlations using a heatmap

Requirements
------------
- Python 3.x
- NetworkX
- Matplotlib
- Pandas
- Seaborn

To install the necessary packages, you can use:

    pip install networkx matplotlib pandas seaborn

Usage
-----
1. Modify the path to the network data you wish to import
2. Compute centrality measures for each node
2. Save the computed centrality measures to a CSV file
3. Compute and print the correlation matrix for the different centrality measures
4. Visualize the correlations in a heatmap

Output
------
The results of the analysis are saved as a CSV file in the results folder:

    /Users/sal/PycharmProjects/NetworkScience/Results

The correlation matrix is printed in the terminal and visualized as a heatmap.

------
Author: Sal Hargis
This project was created to analyze the centrality measures of four real world network datasets










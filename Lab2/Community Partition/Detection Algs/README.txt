Community Detection and Graph Partitioning Executables

This repository contains executable files for performing community detection and graph partitioning on large networks.

System Requirements

- These executables are designed to run on **Linux** systems (macOS is not compatible).
- The examples below use **COE Linux**, a remote Linux server provided by **Ohio State University**.

Executable Files
Multi-Level Random Walk Markov Clustering (MLRMCL):
- Make file executable: chmod +x mlrmcl 
- Run with path to graph (default parameters): ./mlrmcl graph.txt
- Run with custom parameters: ./mlrmcl -c 500 -b 0.6 -i 2.5 -o output.txt graph.txt
    -   -c <integer>            size of coarsest graph (default 1000)
    -   -b <float>              balance parameter (default 0.5)
    -   -i <float>              inflation parameter (default 2.0)
    -   -o <string>             output file

GPMetis:
- Run algorithm: ./gpmetis graph.metis 10 (10 = number of set partitions)
- Has many different parameters to choose from, command ./gpmetis to see all parameters

Community:
- Run algorithm: ./community
- Parameters:
   -i: Input graph (undirected graph) (default:'graph.txt')
   -o: Output file (default:'communities.txt')
   -a: Algorithm: 1:Girvan-Newman, 2:Clauset-Newman-Moore
- Run on a graph: ./community -i graph.txt -a 2

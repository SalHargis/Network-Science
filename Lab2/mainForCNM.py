import networkx as nx
import numpy as np

def load_graph(edgelist_file):
    G = nx.read_edgelist(edgelist_file, nodetype=int, create_using=nx.Graph())
    return G

def load_partition(partition_file):
    partition = {}
    with open(partition_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            node, community = map(int, line.strip().split())
            partition[node] = community
    return partition

def calculate_modularity(G, partition):
    communities = {}
    for node, community in partition.items():
        if community not in communities:
            communities[community] = set()
        communities[community].add(node)
    return nx.community.quality.modularity(G, communities.values())

def calculate_conductance(G, partition):
    communities = {}
    for node, community in partition.items():
        if community not in communities:
            communities[community] = set()
        communities[community].add(node)
    
    conductance_values = []
    for community in communities.values():
        cut_size = nx.cut_size(G, community)
        vol = sum(G.degree(n) for n in community)
        if vol > 0:
            conductance_values.append(cut_size / vol)
    
    return np.mean(conductance_values)

def calculate_ncut(G, partition):
    communities = {}
    for node, community in partition.items():
        if community not in communities:
            communities[community] = set()
        communities[community].add(node)
    
    ncut_values = []
    for community in communities.values():
        cut_size = nx.cut_size(G, community)
        vol_inside = sum(G.degree(n) for n in community)
        vol_outside = sum(G.degree(n) for n in G.nodes if n not in community)
        if (vol_inside + vol_outside) > 0:
            ncut_values.append(cut_size / (vol_inside + vol_outside))
    
    return np.mean(ncut_values)

if __name__ == "__main__":
    graph_file = "/home/hargis.29/CSE5245/Lab2/CommDetectExe/com-youtube.ungraph.txt"
    partition_file = "/home/hargis.29/CSE5245/Lab2/ResultsCNM/GnutellaCNM.txt"
    
    G = load_graph(graph_file)
    partition = load_partition(partition_file)
    
    modularity = calculate_modularity(G, partition)
    conductance = calculate_conductance(G, partition)
    ncut = calculate_ncut(G, partition)
    
    print(f"Modularity: {modularity:.4f}")
    print(f"Conductance: {conductance:.4f}")
    print(f"Normalized Cut: {ncut:.4f}")

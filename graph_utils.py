import networkx as nx

def build_digraph_with_weights():
    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])


    graph = nx.DiGraph() #crear un grafo
    for i in range(1, num_nodes+1):
        graph.add_node(i)


    for i in range(1, num_edges+1):
        linea = input().split()
        graph.add_edge(int(linea[0]), int(linea[1]))
        graph.add_weighted_edges_from([(int(linea[0]), int(linea[1]), int(linea[2]))])

    return graph

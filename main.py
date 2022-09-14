import networkx  as nx

from graph_utils import *
from solve       import *

graph    = build_digraph_with_weights()
solution = dfs_topological_sort(graph)

print(dict(sorted(solution.items())))
# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("\nStarting breadth search")
print("Breadth search", search.breadth_first_graph_search(ab).path())
print("\nStarting depth search")
print("Depth search: ", search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
print("\nInitial node: " + ab.initial + "\nGoal node: " + ab.goal)
print("\nStarting breadth search")
print("Breadth search", search.breadth_first_graph_search(ab).path())
print("\nStarting depth search")
print("Depth search: ", search.depth_first_graph_search(ab).path())
print("\nStarting branch and bound search")
print("Branch and Bound search: ", search.branch_and_bound_graph_search(ab).path())
print("\nStarting branch and bound with subestimation search")
print("Branch and Bound with subestimation search: ",
      search.branch_and_bound_with_subestimation_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450


# Other searches
oe = search.GPSProblem('O', 'E'
                       , search.romania)
print("\nInitial node: " + oe.initial + "\nGoal node: " + oe.goal)
print("\nStarting breadth search")
print("Breadth search", search.breadth_first_graph_search(oe).path())
print("\nStarting depth search")
print("Depth search: ", search.depth_first_graph_search(oe).path())
print("\nStarting branch and bound search")
print("Branch and Bound search: ", search.branch_and_bound_graph_search(oe).path())
print("\nStarting branch and bound with subestimation search")
print("Branch and Bound with subestimation search: ",
      search.branch_and_bound_with_subestimation_graph_search(oe).path())

gz = search.GPSProblem('G', 'Z'
                       , search.romania)
print("\nInitial node: " + gz.initial + "\nGoal node: " + gz.goal)
print("\nStarting breadth search")
print("Breadth search", search.breadth_first_graph_search(gz).path())
print("\nStarting depth search")
print("Depth search: ", search.depth_first_graph_search(gz).path())
print("\nStarting branch and bound search")
print("Branch and Bound search: ", search.branch_and_bound_graph_search(gz).path())
print("\nStarting branch and bound with subestimation search")
print("Branch and Bound with subestimation search: ",
      search.branch_and_bound_with_subestimation_graph_search(gz).path())

nd = search.GPSProblem('N', 'D'
                       , search.romania)
print("\nInitial node: " + nd.initial + "\nGoal node: " + nd.goal)
print("\nStarting breadth search")
print("Breadth search", search.breadth_first_graph_search(nd).path())
print("\nStarting depth search")
print("Depth search: ", search.depth_first_graph_search(nd).path())
print("\nStarting branch and bound search")
print("Branch and Bound search: ", search.branch_and_bound_graph_search(nd).path())
print("\nStarting branch and bound with subestimation search")
print("Branch and Bound with subestimation search: ",
      search.branch_and_bound_with_subestimation_graph_search(nd).path())

mf = search.GPSProblem('M', 'F'
                       , search.romania)
print("\nInitial node: " + mf.initial + "\nGoal node: " + mf.goal)
print("\nStarting breadth search")
print("Breadth search", search.breadth_first_graph_search(mf).path())
print("\nStarting depth search")
print("Depth search: ", search.depth_first_graph_search(mf).path())
print("\nStarting branch and bound search")
print("Branch and Bound search: ", search.branch_and_bound_graph_search(mf).path())
print("\nStarting branch and bound with subestimation search")
print("Branch and Bound with subestimation search: ",
      search.branch_and_bound_with_subestimation_graph_search(mf).path())

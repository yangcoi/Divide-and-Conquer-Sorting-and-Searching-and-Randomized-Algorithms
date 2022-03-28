from random import randint

"""
The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to
200. The first column in the file represents the vertex label, and the particular row (other entries except the first
column) tells all the vertices that the vertex is adjacent to. So for example, the 6th6^{th}6th row looks like :
"6 155 56 52 120 ......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the
vertices with labels 155,56,52,120,......,etc
Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above
graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions.
Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction.
But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make sure
to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.) Write
your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.
"""


class KargerMinCut(object):
    # "graph" begins as a list of lists (edges) populated by read_file() and then modified by min_cut()
    # Example structure: [[1, 2],[1, 3],[2, 4]]
    graph = []
    # "vertices" begins as a count of the number of input lines from the input file populated by read_file() and then
    # modified by min_cut(); each iteration of min_cut() reduces the count by 1
    vertices = 0

    def min_cut(self):
        # Check the number of vertices in "self.vertices", which is reduced each iteration; when it equals 2, then
        # len(self.graph) is the number of edges between the two remaining vertices
        # Example structure: [[2, 9], [2, 9], [2, 9]]
        if self.vertices == 2:
            return len(self.graph)
        else:
            # "edge_to_cut" represents a randomly determined edge *index* from all the remaining edges in the graph;
            # the "-1" term prevents searching for an index equaling the length of the graph (randint() does not work
            # like range() in terms of inclusivity)
            edge_to_cut = randint(0, len(self.graph)-1)
            # "cut_edge" is the actual list representation of the "edge_to_cut", like [53, 117]
            cut_edge = self.graph[edge_to_cut]
            first_vertex = cut_edge[0]
            second_vertex = cut_edge[1]
            # Contract the edge by replacing all instances of "second_vertex" in the graph with "first_vertex"
            for _ in range(len(self.graph)):
                if self.graph[_][0] == second_vertex:
                    self.graph[_][0] = first_vertex
                if self.graph[_][1] == second_vertex:
                    self.graph[_][1] = first_vertex
            # After edge contraction, reduce number of remaining vertices by 1
            self.vertices -= 1
            # Instantiate list of "edges_to_cut"; in addition to "edge_to_cut", other equivalent edges (self loops)
            # also need to be removed
            edges_to_cut = []
            # "i" keeps track of the current index so we know which edges to delete
            i = 0
            # Find edges that have two of the same vertex (self loops) for elimination
            for edge in self.graph:
                if edge[0] == edge[1]:
                    edges_to_cut.extend([i])
                i += 1
            # Delete self loops; the "[::-1]" syntax means that the last item in "edges_to_cut" is deleted first to
            # prevent index confusion (deleting the first item first changes the indices of all remaining items)
            for edge in edges_to_cut[::-1]:
                del self.graph[edge]
            # Call min_cut() recursively until the number of vertices == 2
            return self.min_cut()

    def read_file(self, filename):
        with open(filename) as input_file:
            for line in input_file:
                # Instantiate temporary list of integers from each line
                adjacency_list = [int(vertex) for vertex in line.split()]
                # Increment "self.vertices" for each line in the file
                self.vertices += 1
                # Create a list of edges, "self.graph", consisting of vertex pairs; the "vertex != ..." condition
                # ensures that same vertex pairs are not created, i.e., skip the first item in the list, and the
                # "vertex > ..." condition ensures that the resulting graph does not have duplicate edges (any vertex
                # < than the first item will already be represented in the graph)
                self.graph.extend([adjacency_list[0], vertex] for vertex in adjacency_list
                                  if vertex != adjacency_list[0] and vertex > adjacency_list[0])


results = []
executions = 100
while executions > 0:
    min_cut = KargerMinCut()
    min_cut.read_file('D:\w4.txt')
    results.extend([min_cut.min_cut()])
    executions -= 1
print(min(results), ":", results.count(min(results)), "times")
# 17, about 1% of the time; 20 is far more common
# 1000 executions takes about 150s
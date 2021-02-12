from collections import defaultdict


class Graphs:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, origin, destination):
        # add edge to graph
        self.graph[origin].append(destination)

    def addWeight(self):
        weight_matrix = [[0] * len(g.graph) for i in range(len(self.graph))]
        for origin in self.graph:
            for destination in self.graph[origin]:
                weight = input(f'Enter the weight between {origin} and {destination}: ')
                weight_matrix[origin][destination] = int(weight)
        return weight_matrix

    def BellmanFord(self, source, weight_matrix):
        distanceList = [9999] * len(g.graph)
        distanceList[source] = 0
        for i in range(len(self.graph) - 1):
            for node in list(self.graph.keys()):
                for destination in range(len(self.graph)):
                    if distanceList[node] + weight_matrix[node][destination] < distanceList[destination] and \
                            weight_matrix[node][destination] != 0:
                        distanceList[destination] = weight_matrix[node][destination] + distanceList[node]
        for node in list(self.graph.keys()):
            for destination in range(len(self.graph)):
                if distanceList[node] + weight_matrix[node][destination] < distanceList[destination] and \
                        weight_matrix[node][destination] != 0:
                    return False
        return distanceList


g = Graphs()
g.addEdge(0, 1)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)
g.addEdge(3, 2)
# g.addEdge(4, 1)
# g.addEdge(4, 4)
wt_matrix = g.addWeight()
print('The weight matrix is:\n')
print(wt_matrix)
src = int(input('Enter the source: '))
BellmanDistance = g.BellmanFord(src, wt_matrix)
if BellmanDistance:
    print(f'The distances are: {BellmanDistance}')
else:
    print('There is a negative edge cycle in the graph !!!')


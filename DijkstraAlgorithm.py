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

    def DijkshtrasAlgo(self, source, weight_matrix):
        distanceList = [9999] * len(g.graph)
        unvisitedNodes = list(self.graph.keys())
        distanceList[source] = 0
        visiting = source
        while unvisitedNodes:
            for node in range(len(g.graph)):
                if distanceList[visiting] + weight_matrix[visiting][node] < distanceList[node] and \
                        weight_matrix[visiting][node] != 0:
                    distanceList[node] = weight_matrix[visiting][node] + distanceList[visiting]
            unvisitedNodes.remove(visiting)
            minDist = 99999
            for restNode in unvisitedNodes:
                if distanceList[restNode] < minDist:
                    visiting = restNode
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
DjAlgoDist = g.DijkshtrasAlgo(src, wt_matrix)
print(f'The distances are: {DjAlgoDist}')


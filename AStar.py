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

    def AStarAlgo(self, source, destination,weight_matrix):
        # Change the heuristic values according to number of nodes and destination selected
        heuristicWt = [0] * len(self.graph)
        for i in range(len(self.graph)):
            htWt = int(input(f'Enter the heuristic weight for {i}: '))
            heuristicWt[i] = htWt
        heuristicWt[destination] = 0
        distanceList = [9999] * len(self.graph)
        unvisitedNodes = [source]
        distanceList[source] = 0
        visiting = source
        while visiting:
            for node in range(len(self.graph)):
                if distanceList[visiting] + weight_matrix[visiting][node] + heuristicWt[node] < distanceList[node] and \
                        weight_matrix[visiting][node] != 0:
                    unvisitedNodes.append(node)
                    distanceList[node] = distanceList[visiting] + weight_matrix[visiting][node]
            minDist = 9999
            if unvisitedNodes:
                for restNode in unvisitedNodes:
                    if distanceList[restNode] < minDist:
                        minDist = distanceList[restNode]
                        visiting = restNode
                        unvisitedNodes.remove(restNode)
            else:
                visiting = False
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
dest = int(input('Enter the destination: '))
AStarAlgoDist = g.AStarAlgo(src, dest, wt_matrix)
print(f'The distance from source {src} to {dest}: {AStarAlgoDist[dest]}')

from collections import defaultdict


class Graphs:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, origin, destination):
        self.graph[origin].append(destination)

    def BFSUtil(self, discover_queue, vertex, explored):
        for i in self.graph[vertex]:
            if i not in discover_queue:
                discover_queue.append(i)
        explored[vertex] = True
        print(vertex, end=' ')
        for bfs_vertex in discover_queue:
            if not explored[bfs_vertex]:
                self.BFSUtil(discover_queue, bfs_vertex, explored)

    def BFS(self, start_vertex):
        explored = [False] * (max(self.graph) + 1)
        discover_queue = []
        self.BFSUtil(discover_queue, start_vertex, explored)


g = Graphs()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 2)
print()
print("Following is DFS from (starting from vertex 3)")
g.BFS(3)

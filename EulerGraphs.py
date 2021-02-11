from collections import defaultdict


class EulerGraph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.last_visited = None
        self.euler_path_edges = 0

    def addEdge(self, origin, destination):
        # Add edge to graph
        self.graph[origin].append(destination)

    def euler_path(self, vertex, visited, order_of_visit):
        flag = False
        visited[vertex] = True
        order_of_visit.append(vertex)
        for destination in self.graph[vertex]:
            self.last_visited = vertex
            for second_path in self.graph[destination]:
                if not visited[second_path]:
                    flag = True
            if not visited[destination] or flag:
                # print(destination)
                self.euler_path_edges += 1
                self.euler_path(destination, visited, order_of_visit)

    def euler_origin(self, origin_vertex):
        cycle = False
        vertex_order_of_visit = []
        visited = [False] * (max(self.graph) + 1)
        number_of_edges = 0
        for vertex_edges in self.graph:
            for edges in self.graph[vertex_edges]:
                number_of_edges += 1
        self.euler_path(origin_vertex, visited, vertex_order_of_visit)
        print(number_of_edges)
        print(visited)
        # print(SALT VERTEX -- >{vertex_order_of_visit[vertex_order_of_visit.__len__()-1]}')
        for final_path in self.graph[vertex_order_of_visit[vertex_order_of_visit.__len__() - 1]]:
            if origin_vertex == final_path or final_path == vertex_order_of_visit[vertex_order_of_visit.__len__() - 1]:
                self.euler_path_edges += 1
                if origin_vertex == final_path:
                    cycle = True
                break
        if self.euler_path_edges == number_of_edges:
            if cycle:
                print('Euler Cycle is present in the graph !!!')
            else:
                print('Euler path is present in the graph !!!')
        else:
            print('No Euler construct is present in graph !!')


g = EulerGraph()
g.addEdge(0, 1)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)
# g.addEdge(3, 2)
# g.addEdge(4, 1)
# g.addEdge(4, 4)
print(g.graph)
g.euler_origin(0)

# graph.py

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # Yönsüz graf için

    def print_graph(self):
        for i in range(self.V):
            print(f"{i} -> {self.adj_list[i]}")

    def bfs(self, start):
        visited = [False]*self.V
        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for neighbor in self.adj_list[s]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = [False]*self.V
        self.dfs_util(start, visited)
        print()

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.print_graph()
    print("BFS starting at vertex 0:")
    g.bfs(0)
    print("DFS starting at vertex 0:")
    g.dfs(0)

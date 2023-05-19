import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.heuristics = {}

    def add_edge(self, src, dest, cost):
        if src not in self.edges:
            self.edges[src] = []
        self.edges[src].append((dest, cost))

    def set_heuristic(self, node, h_value):
        self.heuristics[node] = h_value

    def greedy_search(self, start, goal):
        visited = set()
        frontier = [(self.heuristics[start], start)]

        while frontier:
            (_, current_node) = heapq.heappop(frontier)

            if current_node == goal:
                return True

            if current_node not in visited:
                visited.add(current_node)
                for neighbor, _ in self.edges[current_node]:
                    if neighbor not in visited:
                        heapq.heappush(frontier, (self.heuristics[neighbor], neighbor))

        return False

# Example usage
graph = Graph()

# Adding edges
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'D', 5)
graph.add_edge('B', 'E', 12)
graph.add_edge('C', 'F', 8)
graph.add_edge('E', 'G', 6)
graph.add_edge('F', 'G', 2)

# Setting heuristic values
graph.set_heuristic('A', 10)
graph.set_heuristic('B', 6)
graph.set_heuristic('C', 4)
graph.set_heuristic('D', 5)
graph.set_heuristic('E', 2)
graph.set_heuristic('F', 3)
graph.set_heuristic('G', 0)

# Perform Greedy Best-First Search
result = graph.greedy_search('A', 'G')
print("Path found:", result)
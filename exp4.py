from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
    visited = set()
    queue = PriorityQueue()
    queue.put((0 + heuristic[start], 0, start))  # (f_score, g_score, node)
    
    while not queue.empty():
        (f_score, cost, node) = queue.get()
        
        if node not in visited:
            visited.add(node)
            
            if node == goal:
                return cost
            
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    g_score = cost + weight
                    h_score = heuristic[neighbor]
                    f_score = g_score + h_score
                    queue.put((f_score, g_score, neighbor))

    return None

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 5, 'E': 12},
    'C': {'A': 4, 'F': 8},
    'D': {'B': 5},
    'E': {'B': 12, 'G': 6},
    'F': {'C': 8, 'G': 2},
    'G': {'E': 6, 'F': 2}
}

heuristic = {
    'A': 10,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 3,
    'G': 0
}

result = a_star_search(graph, 'A', 'G', heuristic)
print("Path found with cost:", result)

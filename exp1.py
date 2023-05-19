graph = {
    '6' : ['3', '7'],
    '4' : ['2', '5'],
    '8' : ['9'],
    '3' : [],
    '5' : ['9'],
    '9' : [],
    '7' : []
}

visited = []
queue = []
def BFS (visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end="")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("BFS:")
BFS(visited, graph, '6')
                
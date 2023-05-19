graph = {
    '6' : ['4', '8'],
    '4' : ['3', '5'],
    '3' : [],
    '5' : ['9'],
    '9' : [],
    '8' : []
}

visited = set()
def DFS(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            DFS(visited, graph, neighbour)
            
print("DFS: ")
DFS(visited, graph, '6')
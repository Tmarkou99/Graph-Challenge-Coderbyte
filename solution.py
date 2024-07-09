def GraphChallenge(strArr):
    
    edges = [tuple(pair.split('-')) for pair in strArr]
    
    
    graph = {}
    for edge in edges:
        node1, node2 = edge
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    
    def dfs(node, parent, visited):
        max_path = 0
        for neighbor in graph[node]:
            if neighbor != parent and not visited[neighbor]:
                visited[neighbor] = True
                max_path = max(max_path, 1 + dfs(neighbor, node, visited))
                visited[neighbor] = False
        return max_path
    
    
    max_path_length = 0
    for node in graph.keys():
        visited = {key: False for key in graph.keys()}
        visited[node] = True
        max_path_length = max(max_path_length, dfs(node, None, visited))
    
    return max_path_length

  
print(GraphChallenge(input()))

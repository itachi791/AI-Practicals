def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    visited = set()
    
    while len(visited) < len(graph):
        current_node = None
        for node in graph:
            if node not in visited and (current_node is None or distances[node] < distances[current_node]):
                current_node = node
        
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances

graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 8},
    'D': {'B': 9, 'C': 8}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print("Shortest distances from", start_node, "to each node:", distances)

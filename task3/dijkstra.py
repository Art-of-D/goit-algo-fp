import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    
    previous_nodes = {vertex: None for vertex in graph.nodes}

    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        if current_vertex == end:
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]["weight"]
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_distance, neighbor))


    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path if path[0] == start else None
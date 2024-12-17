import heapq

def bfs(cities, roads, start_city, goal_city):
    visited = set()
    frontier = [(start_city, [start_city])]

    while frontier:
        current_city, path = frontier.pop(0)

        if current_city in visited:
            continue

        visited.add(current_city)

        if current_city == goal_city:
            return path

        for neighbor, _ in roads.get(current_city, []):
            if neighbor not in visited:
                frontier.append((neighbor, path + [neighbor]))

    return None 

def dfs(cities, roads, start_city, goal_city):
    visited = set()
    frontier = [(start_city, [start_city])]

    while frontier:
        current_city, path = frontier.pop()

        if current_city in visited:
            continue

        visited.add(current_city)

        if current_city == goal_city:
            return path

        for neighbor, _ in roads.get(current_city, []):
            if neighbor not in visited:
                frontier.append((neighbor, path + [neighbor]))

    return None 

def weighted_bfs(cities, roads, start_city, goal_city):

    visited = set()
    frontier = [(0, start_city, [start_city])]
    
    while frontier:
        cost, current_city, path = heapq.heappop(frontier)

        if current_city in visited:
            continue

        visited.add(current_city)

        if current_city == goal_city:
            return path, cost

        for neighbor, distance in roads.get(current_city, []):
            if neighbor not in visited:
                heapq.heappush(frontier, (cost + distance, neighbor, path + [neighbor]))

    return None, float('inf')

def traverse_all_cities(cities, roads, start_city, strategy):

    def visit_all(current_city, visited, path):
        if len(visited) == len(cities):
            return path

        for neighbor, _ in roads.get(current_city, []):
            if neighbor not in visited:
                new_path = visit_all(neighbor, visited | {neighbor}, path + [neighbor])
                if new_path:
                    return new_path

        return None

    if strategy not in ['bfs', 'dfs']:
        raise ValueError("Invalid strategy. Use 'bfs' or 'dfs'.")

    path = visit_all(start_city, {start_city}, [start_city])
    return path, None

def traverse_all_cities_with_revisits(cities, roads, start_city, strategy):

    if strategy not in ['bfs', 'dfs']:
        raise ValueError("Invalid strategy. Use 'bfs' or 'dfs'.")

    def visit_all_with_revisits_bfs():
        queue = [(start_city, [start_city], {start_city})]  # (current_city, path, visited)
        while queue:
            current_city, path, visited = queue.pop(0)
            if len(visited) == len(cities):
                return path
            for neighbor, _ in roads.get(current_city, []):
                queue.append((neighbor, path + [neighbor], visited | {neighbor}))
        return None

    def visit_all_with_revisits_dfs(current_city, visited, path):
        if len(visited) == len(cities):
            return path
        for neighbor, _ in roads.get(current_city, []):
            new_path = visit_all_with_revisits_dfs(neighbor, visited | {neighbor}, path + [neighbor])
            if new_path:
                return new_path
        return None

    if strategy == 'bfs':
        return visit_all_with_revisits_bfs()
    elif strategy == 'dfs':
        return visit_all_with_revisits_dfs(start_city, {start_city}, [start_city])


def dijkstra(cities, roads, start_city, goal_city):

    distances = {city: float('inf') for city in cities}
    distances[start_city] = 0
    priority_queue = [(0, start_city, [])] 

    while priority_queue:
        current_distance, current_city, path = heapq.heappop(priority_queue)

        if current_distance > distances[current_city]:
            continue

        path = path + [current_city]

        if current_city == goal_city:
            return path, current_distance

        for neighbor, weight in roads.get(current_city, []):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor, path))

    return None, float('inf') 

def a_star(cities, roads, start_city, goal_city, heuristic):

    distances = {city: float('inf') for city in cities}
    distances[start_city] = 0
    priority_queue = [(0, start_city, [])] 

    while priority_queue:
        _, current_city, path = heapq.heappop(priority_queue)
        
        path = path + [current_city]

        if current_city == goal_city:
            return path, distances[current_city]

        for neighbor, weight in roads.get(current_city, []):
            tentative_distance = distances[current_city] + weight

            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                priority = tentative_distance + heuristic(neighbor, goal_city)
                heapq.heappush(priority_queue, (priority, neighbor, path))

    return None, float('inf')

def floyd_warshall(cities, roads):

    distance = {city: {other: float('inf') for other in cities} for city in cities}
    
    for city in cities:
        distance[city][city] = 0

    for city, connections in roads.items():
        for neighbor, weight in connections:
            distance[city][neighbor] = weight

    for k in cities:
        for i in cities:
            for j in cities:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

def bellman_ford(cities, roads, start_city):

    distance = {city: float('inf') for city in cities}
    distance[start_city] = 0

    edges = []
    for city, connections in roads.items():
        for neighbor, weight in connections:
            edges.append((city, neighbor, weight))

    for _ in range(len(cities) - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Check for negative weight cycles
    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return distance

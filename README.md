#Problem Title: Traveling Ethiopia Problem (Simplistic Version)
#Problem Statement
Ethiopia, known for its rich cultural heritage and diverse geography, has numerous cities connected by road networks. You are tasked to develop an AI agent that plans a tour across Ethiopia, starting from a designated city and visiting other cities based on specific constraints. The agent should implement uninformed search strategies to find paths under different conditions.
Graph Representation
The cities are represented as nodes, and roads between them are edges. The graph is undirected and may include varying distances (costs). You will be provided the following:
City Data:
cities: A list of city names.
roads: A dictionary where each key is a city, and the value is a list of tuples (connected_city, distance).
Input:
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}


Visualization:
Create a visualization of the road network using NetworkX or another library, plotting the graph and highlighting the path found by the agent.

Path finding Problem
Allow any selected strategy to guid the agent traveling from any random position to the goal state.
Initial State: The agent starts in a designated city.
Goal State: The agent needs to find:
A path to a target city.
A path visiting all cities exactly once (optional extended task for students).
Constraints:
The roads may be unweighted (for BFS/DFS) or weighted (for exploring cost-sensitive variations).
The agent should avoid revisiting a city (except if the problem demands revisiting).
Implementation:
Implement Breadth-First Search (BFS) to find the shortest path based on the number of roads (unweighted).
Implement Depth-First Search (DFS) to find a feasible path to the target city.
Extend BFS to work for weighted graphs (using cumulative path cost as a priority heuristic).

Function Specifications:
Path Finder:

def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - goal_city: The destination city (for specific tasks).
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').
    
    Returns:
    - path: List of cities representing the path from start_city to goal_city.
    - cost: Total cost (number of steps or distance) of the path.
    """
    pass

Travel All Cities (Extended Task)

3. Create an agent guided by any strategy t go from one random state to all other states optimally.
def traverse_all_cities(cities, roads, start_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').
    
    Returns:
    - path: List of cities representing the traversal path.
    - cost: Total cost (distance) of the traversal.
    """
    pass

Example Expected Output:
=BFS Path: ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Mekelle'] with cost 990.=
Advanced Challenges (Bonus)
Extend the agent to handle dynamic road conditions (e.g., roads becoming blocked).
Add the ability to find the k-shortest paths between two cities.

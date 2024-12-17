from visualize_data import visualize_graph, visualize_matrix, visualize_row_matrix
from data import cities, roads
from algorithms import bfs, dfs, weighted_bfs, dijkstra, a_star, floyd_warshall, bellman_ford, traverse_all_cities, traverse_all_cities_with_revisits
import streamlit as st
import numpy as np

def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    """
    Wrapper to select BFS, DFS, Weighted BFS, Dijkstra, or A* based on the strategy.
    """
    if strategy == 'bfs':
        return bfs(cities, roads, start_city, goal_city), None
    elif strategy == 'dfs':
        return dfs(cities, roads, start_city, goal_city), None
    elif strategy == 'weighted_bfs':
        return weighted_bfs(cities, roads, start_city, goal_city)
    elif strategy == 'dijkstra':
        return dijkstra(cities, roads, start_city, goal_city)
    elif strategy == 'a_star':
        heuristic = lambda x, y: 0 
        return a_star(cities, roads, start_city, goal_city, heuristic)
    else:
        raise ValueError("Invalid strategy. Use 'bfs', 'dfs', 'weighted_bfs', 'dijkstra', or 'a_star'.")

# Streamlit UI
st.sidebar.title("Dashboard")
selection = st.sidebar.radio("Select a Feature", ["Traveling Ethiopia Problem", "All Pairs Shortest Paths", "Traverse All Cities"])

if selection == "Traveling Ethiopia Problem":
    st.title("Traveling Ethiopia Problem")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Input")
        start_city = st.selectbox("Select Start City:", cities)
        goal_city = st.selectbox("Select Goal City (optional):", [None] + cities)
        strategy = st.radio("Select Strategy:", ['bfs', 'dfs', 'weighted_bfs', 'dijkstra', 'a_star'])
        path = None
        if st.button("Find Path"):
            if not start_city or not strategy:
                st.error("Please select a start city and strategy.")
            else:
                try:
                    if goal_city:
                        path, cost = uninformed_path_finder(cities, roads, start_city, goal_city, strategy)
                        if path:
                            st.success(f"Path: {path} with cost: {cost}")
                        else:
                            st.error("No path found.")
                    else:
                        st.error("Goal city must be selected to find a specific path.")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    with col2:
        st.header("Visualization")
        visualize_graph(cities, roads, path)

elif selection == "All Pairs Shortest Paths":
    st.title("All Pairs Shortest Paths")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Floyd-Warshall")
        try:
            distances_fw = floyd_warshall(cities, roads)
            st.success("Floyd-Warshall completed. Visualizing shortest paths:")
            visualize_matrix(cities, distances_fw)

        except Exception as e:
            st.error(f"Error: {str(e)}")

    with col2:
        st.header("Bellman-Ford")
        start_city = st.selectbox("Select Start City for Bellman-Ford:", cities)
        
        if st.button("Run Bellman-Ford"):
            if start_city:
                try:
                    distances_bf = bellman_ford(cities, roads, start_city)
                    st.success("Bellman-Ford completed. Visualizing shortest paths:")
                    visualize_row_matrix(cities, distances_bf)
                except ValueError as e:
                    st.error(f"Error: {str(e)}")
                    
elif selection == "Traverse All Cities": 
    st.title("Traverse All Cities")
    col1, col2 = st.columns([1,2])

    with col1:
        
        st.header("Input")
        start_city = st.selectbox("Select Start City:", cities)
        strategy = st.radio("Select Strategy:", ['bfs', 'dfs'])
        path = None
            
    
    with col2:
        if st.button("Only once visit"):
                if not start_city or not strategy:
                    st.error("Please select a start city and strategy.")
                else:
                    try:
                        path, _ = traverse_all_cities(cities, roads, start_city, strategy)
                        if path:
                            st.success(f"Traversal Path: {path}")
                            visualize_graph(cities, roads, path)
                        else:
                            st.error("Traversal not possible.")
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
   
        if st.button("Repeated visit"):
                if not start_city or not strategy:
                    st.error("Please select a start city and strategy.")
                else:
                    try:
                        path = traverse_all_cities_with_revisits(cities, roads, start_city, strategy)
                        if path:
                            st.success(f"Traversal Path: {path}")
                            visualize_graph(cities, roads, path)
                        else:
                            st.error("Traversal not possible.")
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        
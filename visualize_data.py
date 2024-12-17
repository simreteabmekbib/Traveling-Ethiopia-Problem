import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def visualize_graph(cities, roads, path=None):

    graph = nx.Graph()
    for city in cities:
        graph.add_node(city)
    for city, connections in roads.items():
        for neighbor, distance in connections:
            graph.add_edge(city, neighbor, weight=distance)

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): d['weight'] for u, v, d in graph.edges(data=True)})

    if path:
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='red', width=2)

    fig = plt.gcf() 
    st.pyplot(fig)
    
def visualize_matrix(cities, distances):

    n = len(cities)
    city_indices = {city: i for i, city in enumerate(cities)}

    # Create a matrix representation of distances
    matrix = np.full((n, n), float('inf'))
    for i in range(n):
        matrix[i][i] = 0

    for city, row in distances.items():
        for target_city, distance in row.items():
            if distance != float('inf'):
                matrix[city_indices[city]][city_indices[target_city]] = distance

    # Plot the matrix
    fig, ax = plt.subplots(figsize=(10, 8))
    cax = ax.matshow(matrix, cmap="coolwarm")
    fig.colorbar(cax)

    # Set labels
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(cities, rotation=90)
    ax.set_yticklabels(cities)

    for i in range(n):
        for j in range(n):
            value = matrix[i][j]
            if value != float('inf'):
                ax.text(j, i, f"{int(value)}", va='center', ha='center', color='black')

    plt.title("All Pairs Shortest Paths Matrix")
    st.pyplot(fig)
    
def visualize_row_matrix(cities, distances):

    n = len(cities)
    city_indices = {city: i for i, city in enumerate(cities)}

    # Create a row matrix representation of distances
    row_matrix = np.full((1, n), float('inf'))

    for target_city, distance in distances.items():
        if distance != float('inf'):
            row_matrix[0][city_indices[target_city]] = distance

    fig, ax = plt.subplots(figsize=(10, 2))
    cax = ax.matshow(row_matrix, cmap="coolwarm")
    fig.colorbar(cax)

    # Set labels
    ax.set_xticks(range(n))
    ax.set_yticks([])
    ax.set_xticklabels(cities, rotation=90)

    for j in range(n):
        value = row_matrix[0][j]
        if value != float('inf'):
            ax.text(j, 0, f"{int(value)}", va='center', ha='center', color='black')

    plt.title("Shortest Paths from Source City")
    st.pyplot(fig)
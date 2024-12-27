# Traveling Ethiopia Problem (Simplistic Version)

## Problem Statement
Ethiopia, known for its rich cultural heritage and diverse geography, has numerous cities connected by road networks. This project aims to develop an AI agent that can plan a tour across Ethiopia using uninformed search strategies. The agent should find paths under specific conditions, such as traveling between cities or visiting all cities exactly once.

## Graph Representation
The cities are represented as nodes, and roads between them are edges. The graph is:
- **Undirected** (roads can be traveled in both directions).
- **Weighted or unweighted**, depending on the search strategy.

### Input
- **Cities**: `['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']`
- **Roads**:
  ```python
  roads = {
      'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
      'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
      'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
      'Hawassa': [('Addis Ababa', 275)],
      'Mekelle': [('Gondar', 300)]
  }

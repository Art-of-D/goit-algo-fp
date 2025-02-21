import os
import matplotlib.pyplot as plt
import networkx as nx
import random

# Generate a random graph
def generate_random_graph(num_nodes: int, file_name: str = "new_transport_network"):
  G = nx.Graph()

  for i in range(num_nodes):
      G.add_node(i, label=f"Район {i}")

  for _ in range(num_nodes * 2):
      u, v = random.sample(range(num_nodes), 2)
      weight = random.randint(1, 10)
      G.add_edge(u, v, weight=weight)

  script_dir = os.path.dirname(os.path.abspath(__file__))  
  graph_path = os.path.join(script_dir, f"{file_name}.graphml")  

  nx.write_graphml(G, graph_path)

  print(f"Your graph has been saved to {graph_path}")

  return graph_path

#Load graph
def load_graph(file_path: str):
  G = nx.read_graphml(file_path)
  return G

#Graph visualization
def graph_data(graph: dict):
  G = nx.Graph(graph)

  pos = nx.spring_layout(G)
  labels = nx.get_edge_attributes(G, 'weight')

  num_nodes = G.number_of_nodes()
  num_edges = G.number_of_edges()
  degrees = dict(G.degree())
  degree_centrality = nx.degree_centrality(G)
  closeness_centrality = nx.closeness_centrality(G)
  betweenness_centrality = nx.betweenness_centrality(G)

  print(f"Кількість вершин: {num_nodes}")
  print(f"Кількість ребер: {num_edges}")
  print(f"Центральність ступеня:{degree_centrality}")
  print(f"Близькість вузлів:{closeness_centrality}")
  print(f"Посередництво вузлів:{betweenness_centrality}")
  print("Ступінь кожної вершини:")
  for node, degree in degrees.items():
      print(f"- Вершина {node}: ребер {degree}")
      

  plt.figure(figsize=(10, 10))
  nx.draw(G, pos, with_labels=True, node_color='green', edge_color='black', node_size=2000, font_size=12)
  nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

  plt.title("Your graph")
  plt.show()
  return G
from dijkstra import dijkstra
from graph import generate_random_graph, load_graph, graph_data
def shortest_paths_from(graph, start):

    print(f"The shortest paths from {start} to:")
    for target in graph.nodes:
        if target != start:
            path = dijkstra(graph, start, target)
            if path:
                print(f"{target} next -> {path}")
            else:
                print(f"{target}: don`t exist")


graph = {}
# if you want to generate a random graph uncomment the line below
graph = generate_random_graph(30) # You can change the number of nodes as needed and the file name as well
file_name = "./task3/new_transport_network.graphml" if graph == {} else graph
file = load_graph(file_name)

G = graph_data(file)


start_G = input("Enter the start node: ")
end_G = input("Enter the end node: ")

print("Dijkstra:")
path = dijkstra(file, start_G, end_G)
print(path)

print("Shortest paths to all other nodes:")
shortest_paths_from(file, start_G)
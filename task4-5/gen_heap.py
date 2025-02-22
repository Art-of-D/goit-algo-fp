import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла
  def get (self):
    return self

  def __lt__(self, other):
        return self.val < other.val

  def __le__(self, other):
      return self.val <= other.val

  def __eq__(self, other):
      return self.val == other.val

  def __ne__(self, other):
      return self.val != other.val

  def __gt__(self, other):
      return self.val > other.val

  def __ge__(self, other):
      return self.val >= other.val


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, node):
        heapq.heappush(self.heap, node)

    def get_tree(self):
        if not self.heap:
            return None
        return self.build_tree(0)

    def build_tree(self, index):
        if index >= len(self.heap):
            return None

        node = self.heap[index] 
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        node.left = self.build_tree(left_index)
        node.right = self.build_tree(right_index)

        return node


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()

def generate_color(step, total_steps=255):
    ratio = step / total_steps
    base = int(50 + ratio * 200)
    red = (base + random.randint(-15, 15)) % 255
    green = (base + random.randint(-15, 15)) % 255
    blue = (base + random.randint(-15, 15)) % 255
    
    return f'#{red:02X}{green:02X}{blue:02X}'

def reset_colors(tree_root, color="skyblue"):
    if tree_root is None:
        return

    tree_root.color = color
    if tree_root.left:
        reset_colors(tree_root.left)
    if tree_root.right:
        reset_colors(tree_root.right)

def dfs_traversal(tree_root, total_steps):
    if tree_root is None:
        return

    visited_nodes = []
    stack = [tree_root]

    while stack:
        node = stack.pop()

        if node not in visited_nodes:
            node.color = generate_color(len(visited_nodes), total_steps)
            visited_nodes.append(node)

            draw_tree(tree_root)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def bfs_traversal(tree_root, total_steps):
    queue = [tree_root]
    visited_nodes = []
    
    while queue:
        node = queue.pop(0)
        node.color = generate_color(len(visited_nodes), total_steps)
        visited_nodes.append(node)
        draw_tree(tree_root)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Make tree
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
#make heap
heap = BinaryHeap()
nodes = [root, root.left, root.right, root.left.left, root.left.right]
for node in nodes:
   heap.insert(node)

tree_root = heap.get_tree()
# Visualization of heap
draw_tree(tree_root)

# DFS traversal
dfs_traversal(tree_root, len(nodes))

# Reset colors
reset_colors(tree_root)

# BFS traversal
bfs_traversal(tree_root, len(nodes))
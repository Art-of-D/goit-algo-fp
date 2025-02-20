class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

  def __str__(self):
    return str(self.data)
  
  def get (self):
    return self

  def __lt__(self, other):
        return self.data < other.data

  def __le__(self, other):
      return self.data <= other.data

  def __eq__(self, other):
      return self.data == other.data

  def __ne__(self, other):
      return self.data != other.data

  def __gt__(self, other):
      return self.data > other.data

  def __ge__(self, other):
      return self.data >= other.data
class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  def reverse_list(self):
    prev = None
    current_node = self.head
    while current_node:
      next = current_node.next
      current_node.next = prev
      prev = current_node
      current_node = next
    self.head = prev

  def merge_sort(self):
    if self.head is None or self.head.next is None:
      return
    left = self.head
    right = self.head.next
    while right and right.next:
      left = left.next
      right = right.next.next
    mid = left.next
    left.next = None
    left = LinkedList()
    right = LinkedList()
    left.head = self.head
    right.head = mid
    left.merge_sort()
    right.merge_sort()
    self.head = self.merge(left.head, right.head)

  def merge(self, left, right):
    if left is None:
      return right
    if right is None:
      return left  
    if left.data < right.data:
      left.next = self.merge(left.next, right)
      return left
    else:
      right.next = self.merge(left, right.next)
      return right
  
  @staticmethod
  def merge_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    list = LinkedList()

    list1_next, list2_next = list1.head, list2.head
    if list1_next < list2_next:
        list.head = list1_next
        list1_next = list1.head.next
    else:
        list.head  = list2.head
        list2_next = list2.head.next
    current = list.head
    
    while list1_next is not None and list2_next is not None:
        if list1_next < list2_next:
            current.next = list1_next
            list1_next = list1_next.next
        else:
            current.next = list2_next
            list2_next = list2_next.next
        current = current.next

    while list1_next is not None:
        current.next = list1_next
        list1_next = list1_next.next
        current = current.next

    while list2_next is not None:
        current.next = list2_next
        list2_next = list2_next.next
        current = current.next
      

    return list

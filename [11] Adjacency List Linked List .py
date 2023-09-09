class Node:

  def __init__(self, info, next=None):
    self.info = info
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0  # number of nodes in my LL

  def addToHead(self, info):  # O(1)
    n = Node(info)

    if self.size == 0:  #LL is empty
      self.head = n
      self.tail = n
      self.size += 1
    else:  # LL is NOT empty
      n.next = self.head
      self.head = n
      self.size += 1

  def addToTail(self, info):  #O(1)
    n = Node(info)

    if self.size == 0:  #LL is empty
      self.head = n
      self.tail = n
      self.size += 1
    else:
      self.tail.next = n
      self.tail = n

  def search(self, key):  # O(n), n being the number of elements in my list
    if self.size == 0:
      return False  # LL is empty

    current = self.head

    while current != None:
      if current.info == key:
        return True
      current = current.next
    return False

  def printLL(self):  # O(n), n being the number of elements in my list
    current = self.head
    while current != None:
      print(current.info, end=" -> ")
      current = current.next

  def deleteHead(self):  #O(1)
    if self.size == 0:
      return None
    if self.size == 1:
      temp = self.head.info
      self.head = None
      self.tail = None
      self.size = 0
      return temp

    temp = self.head.info
    self.head = self.head.next
    self.size -= 1
    return temp

  def deleteTail(self):  # O(n), n being the number of elements in the list
    if self.size == 0:
      return None
    if self.size == 1:
      temp = self.head.info
      self.head = None
      self.tail = None
      self.size = 0
      return temp

    temp = self.tail.info
    current = self.head

    for i in range(self.size - 1):  # the number of jumps is size -2
      current = current.next

    self.tail = current
    self.tail.next = None
    self.size -= 1
    return temp

  def deleteNode(self, info):
    # remove the value info from my linked list
    pass


class AdjacencyList:

  def __init__(self, V): # V is the capacity of the Adjacency List
    self.adjacency_list = []
    for i in range(V):
      self.adjacency_list.append(LinkedList()) # Initializing the adjacency list with V number of LinkedLists. Each LinkedList is different than the other and are unrelated. They store their own values. Like different key:value pairs of the same dictionary.
      # it is not an actual dictionary. No keys exist. We simply access a linked list based on its location in self.adjacency_list. Location as in its index.
      # Which means that the index is similar to a key in a dictionary

  def addEdge(self, A, B): #O(V)
    if self.adjacency_list[A].search(B)==True: #O(V) Before adding an edge we check if this edge already exists
      return None
    # To add an edge we are adding 2 new nodes at indicies A and B. 
    self.adjacency_list[A].addToTail(B)  # Add a node B at the end of the Adjacency List of index A (0,1,2,3...)
    self.adjacency_list[B].addToTail(A)  # Add a node A at the end of the adjacency List of index B

  def deleteEdge(self, A, B):
    self.adjacency_list[A].deleteNode(B)
    self.adjacency_list[B].deleteNode(A)

  def printList(self): # Initially 
    for i in range(len(self.adjacency_list)):
      print(i, ":", end=" ") # print the keys which point towards the linked list
      self.adjacency_list[i].printLL() # print the linked list inside each key
      print()

G = AdjacencyList(5)
G.addEdge(1, 2)
G.addEdge(0, 1)
G.addEdge(2, 3)
G.addEdge(3, 1)
G.addEdge(4, 3)
G.printList()
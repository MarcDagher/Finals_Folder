
class Node:
  def __init__(self,info,next=None):
    self.info=info
    self.next=next

class LinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
    self.size=0 # number of nodes in my LL


  def addToTail(self,info): #O(1)
    n=Node(info)
    if self.size==0: #LL is empty
      self.head=n
      self.tail=n
      self.size+=1
    else:
      self.tail.next=n
      self.tail=n
      self.size+=1

  def deleteHead(self): #O(1)
    
    if self.size==0:
      return None
    if self.size==1:
      temp=self.head.info
      self.head=None
      self.tail=None
      self.size=0
      return temp
      
    temp=self.head.info
    self.head=self.head.next
    self.size-=1
    return temp
    
class Queue:
  def __init__(self):
    self.elements=LinkedList()
  def isEmpty(self):
    return self.elements.size==0 # returns True if the LinkedList of the queue is empty, False otherwise
    
  def enqueue(self,item):
    self.elements.addToTail(item)
    
  def dequeue(self):
    return self.elements.deleteHead()
    
class Stack:
  def __init__(self):
    self.elements=[]
  def push(self,item):
    self.elements.append(item)
  def isEmpty(self):
    return len(self.elements) == 0
  def pop(self):
    if len(self.elements)==0:
      return None
    return self.elements.pop()

class AdjacencyMatrix:
  # V: is the number of vertices (plural vertex) in the graph
  def __init__(self,V):
    self.matrix=[]
    for i in range(V):
      self.matrix.append([-1]*V)

  def printMatrix(self):
    for i in range(len(self.matrix)):
      for j in range(len(self.matrix)):
        print(self.matrix[j][i],end=" ")
      print()

  def addEdge(self,A,B,weight): #O(1)
    # adding an edge from A to B
    self.matrix[A][B]=weight
    self.matrix[B][A]=weight

  def deleteEdge(self,A,B): #O(1)
    # deleted the edge from A to B
    self.matrix[A][B]=-1
    self.matrix[B][A]=-1

  def BFS(self,start):# O(V^2) , O(V+E), E being the number of edges in the graph
    visited=[False]*len(self.matrix) # O(V), V is the number of vertices in the graph
    visited[start]=True
    Q=Queue()
    Q.enqueue(start) # keeps track of the nodes that I wwant to check their neighbors
    
    while Q.isEmpty() ==False: # O(V)
      current=Q.dequeue() # give me a node to visit its neighbors, O(1)
      print(current,end=" ")
      for i in range(len(self.matrix[current])): #O(V)
         if self.matrix[current][i] != -1 and visited[i] ==False: # i is a neighor of current AND it is unvisited) O(1)
           visited[i]=True
           Q.enqueue(i)
    print()
    
  def DFS(self,start):# O(V^2)
    visited=[False]*len(self.matrix)
    visited[start]=True
    S=Stack()
    S.push(start) # keeps track of the nodes that I wwant to check their neighbors
    
    while S.isEmpty() ==False:
      current=S.pop() # give me a node to visit its neighbors
      print(current,end=" ")
      for i in range(len(self.matrix[current])):
         if self.matrix[current][i] != -1 and visited[i] ==False: # i is a neighor of current AND it is unvisited
           visited[i]=True
           S.push(i)
    print()
    

G=AdjacencyMatrix(7)
# G.printMatrix()

G.addEdge(0,1,1)
G.addEdge(1,3,1)
G.addEdge(3,5,1)
G.addEdge(0,2,1)
G.addEdge(2,4,1)
G.addEdge(4,6,1)

G.printMatrix()
# print()
G.BFS(0)
G.DFS(0)
# print()
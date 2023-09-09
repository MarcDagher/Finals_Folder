# Adjacency Matrix is a grid of the edges and their weights 
# In this Grid, Edges with pointers pointed towards them are filled with the weight.
# Edges with no pointers pointed towards them are filled with 0
# Edges with a path that reaches this edge but not directly, is filled with a dummy value -1

class AdjacencyMatrix:
  # V: is the number of vertices (plural vertex) in the graph
  def __init__(self,V):
    self.matrix=[]
    for i in range(V):
      self.matrix.append([-1]*V) # Create a grid

  def printMatrix(self): 
    for i in self.matrix:
      for j in i:
        print(j, end="")
      print()
    # for i in range(len(self.matrix)):
    #   for j in range(len(self.matrix)):
    #     print(self.matrix[i][j],end=" ")   # is the column and j is the row
    #   print()

  def addEdge(self,A,B,weight): #O(1) A is column B is row
    # adding an edge from A to B
    self.matrix[A][B]=weight # [A] is the column and [B] is the row. [A] is which list [B] is which index of that list

  def deleteEdge(self,A,B): #O(1) A is column B is row
    # deleted the edge from A to B
    self.matrix[A][B]=-1


G=AdjacencyMatrix(4)
# G.printMatrix()

G.addEdge(0,1,15)
G.addEdge(1,0,20)
G.addEdge(1,3,1)
G.addEdge(2,0,6)
G.addEdge(2,3,2)
# print()
G.printMatrix()
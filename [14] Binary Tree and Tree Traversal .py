class Node:

  def __init__(self, info, right=None, left=None):
    self.info = info
    self.right = right
    self.left = left


class BST:

  def __init__(self, n=None): # initialize an empty root node
    self.root = n

  def add(self, info): # O(n),  being the number of elements in my ttree
    n = Node(info)
    if self.root == None:
      self.root = n
      return

    current = self.root
    added = False
    while not added:
      if current.info > info:  # I look to the left subtree
        if current.left == None:  # the left subtree is empty
          current.left = n  # I add my node
          added = True
        else:
          current = current.left  # I jump to the left subtree
      else:  #I look to the right subtree
        if current.right == None:
          current.right = n  # added the node to the right of current
          added = True
        else:
          current = current.right

  def search(self, info): # O(n),  being the number of elements in my ttree
    current = self.root
    while current != None: # While tree hasn't finished
      if current.info == info: # info found
        return True
      else:  # info not found yet
        if current.info > info:  # the current node has a higher value than what I want
          current = current.left  # jump to the left subtree
        else:
          current = current.right
    return False
  
  # tree traversal
  def inOrder(self,current): #O(n) returns a sorted result. 
    if current==None: # base case
      return
    self.inOrder(current.left) # first we check neighbors on the left
    print(current.info) # when current.left returns none, we print the root node on our way back to traversing the right subtree
    self.inOrder(current.right) # then we check neighbors on the right
    

  
  def preOrder(self,current): # Similar to DFS
    if current==None: # base case
      return
    print(current.info)
    self.preOrder(current.left)
    self.preOrder(current.right)
    
    
  def postOrder(self,current):
    if current==None: # base case
      return
    self.postOrder(current.left)
    self.postOrder(current.right)
    print(current.info)

  
tree=BST()
tree.add(30)
tree.add(25)
tree.add(24)
tree.add(23)
tree.add(27)
tree.add(35)
tree.add(32)

# print(tree.search(32))
# print(tree.search(36))

tree.inOrder(tree.root)
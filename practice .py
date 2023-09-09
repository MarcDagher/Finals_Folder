class Node:
  def __init__(self, info, next = None, previous = None):
    self.info = info
    self.next = next
    self.previous = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  # addHead - adddTail - deleteHead - deleteTail - print_list
  def addHead(self, info):
    new_node = Node(info)

    if self.size == 0:
      self.head = new_node
      self.tail = new_node
      self.size += 1
    
    else:
      self.head.previous = new_node
      new_node.next = self.head
      self.head = new_node
      self.size += 1
  
  def addTail(self, info):
    new_node = Node(info)

    if self.size == 0:
      self.tail = new_node
      self.head = new_node
      self.size += 1

    else:
      new_node.previous = self.tail
      self.tail.next = new_node
      self.tail = new_node
      self.size += 1
    
  def deleteHead(self):
    if self.size == 0: return None
    else:
      self.head = self.head.next 
      self.head.previous = None
      self.size -= 1
    
  def deleteTail(self):
    
    if self.size == 0:
      return None
    else:

      self.tail = self.tail.previous
      self.tail.next = None
      self.size -= 1

  def print_list_forward(self):
    current = self.head
    while current != None:
      print(current.info)
      current = current.next

  def print_list_backwards(self):
    current = self.tail
    while current != None:
      print(current.info)
      current = current.previous

class Stack:
  def __init__(self):
    self.stack = LinkedList()

  def push(self, info):
    self.stack.addTail(info)
  
  def pop(self):
    return self.stack.deleteTail()

  def print_stack(self):
    current = self.stack.head
    while current != None:
      print(current.info)
      current = current.next

class Queue:
  def __init__(self):
    self.queue = LinkedList()
  
  def enqueue(self, info):
    self.queue.addHead(info)

  def dequeue(self):
    return self.queue.deleteTail()

  def print_queue(self):
    self.queue.print_list_forward()



class AdjacencyMatrix:
  def __init__(self, size):
    self.matrix = []
    for i in range(size):
      self.matrix.append([-1] * size ) 
      
  def printMatrix(self):
    # for i in self.matrix:
    #   for j in i:
    #     print(j, end=" ")
    #   print()
    for i in range(len(self.matrix)):   #i is the row and j is the column
      for j in range(len(self.matrix)):
        print(self.matrix[i][j],end=" ")
      print()
  
  def addEdge(self, A, B):
    self.matrix[A][B] = 5
  
  def deleteEdge(self, A, B):
    self.matrix[A][B] = -1

obj = AdjacencyMatrix(4)
obj.addEdge(1,2)
obj.addEdge(3,3)
obj.addEdge(2,2)
# obj.deleteEdge(1,2)
obj.printMatrix()






# obj = Queue()
# obj.enqueue(1)
# obj.enqueue(2)
# obj.enqueue(3)
# obj.enqueue(4)
# obj.dequeue()
# obj.print_queue()

# obj = Stack()
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.push(4)
# obj.push(5)
# obj.pop()
# obj.pop()
# obj.print_stack()


# Linked List => addHead - adddTail - deleteHead - deleteTail - print_list

# obj = LinkedList()
# obj.addHead(2)
# obj.addHead(6)
# obj.addTail(4)

# obj.deleteHead()
# obj.deleteTail()
# obj.print_list_forward()
# print("***************")
# obj.print_list_backwards()
# nehna ta ysir 3anna "elements" badna nzidon manually
# w wa2ta nzidon aam yenzedo 3ala shakel nodes
# fa lamma badna nem7iyon aw ennabesh bayneton, badne nabbesh bayneton ka nodes la nerja3 nem7iyon fe henne minnon w fiyon byeje be albon nodes(info, next)

class Node:
  def __init__(self, info, next=None):
    self.info=info
    self.next=next

# info is the what we want to create/insert/delete
# next is always none referring to the end of the list

class LinkedList:
  def __init__(self): # empty linked list
    self.head=None # empty head
    self.tail=None # empty tail
    self.size=0 # empty list

  def addToHead(self,info): # O(1) Assigning a new head
    n=Node(info) # n is the node we are adding

    if self.size==0: #LL is empty
      self.head=n
      self.tail=n
      self.size+=1
      
    else: # LL is NOT empty
      n.next=self.head # current head is now the next element 
      self.head=n # n is now the new head
      self.size+=1
  
  def addToTail(self, info): # O(1)
    n = Node(info)

    if self.size == 0: # if list is empty
      self.head = n
      self.tail = n
      self.size += 1
    else:
      self.tail.next = n # self.tail.next is the next element after the current tail. We assign now n as the next node after the tail.
      self.tail = n # computer doesn;t know which is tail and which is what. So we need to tell it thet self.tail is now this n.
      self.size += 1
    
  def search(self, key):  # O(n), n being the number of elements in my list
    if self.size == 0:
      return False
    else:
      current = self.head # since we are starting at the head
      while current != None: 
        if current.info == key: # current.info is the data inside the  current node
          return True
        
        current = current.next # if not, current will move to the next node
    return False
  
  def deleteHead(self): 
    if self.size == 0:
      return None
    elif self.size == 1:
      temporary_head = self.head.info # keep the data of deleted head
      self.head = None
      self.tail = None
      self.size = 0
      return temporary_head # similar to pop() return the deleted data
    else: 
      temporary_head = self.head.info
      self.head = self.head.next # head is now the next node. 
      self.size -=1
      return temporary_head
  
  def deleteTail(self):
    if self.size == 0:
      return None
    elif self.size == 1:
      temp = self.tail.info
      self.head = None
      self.tail = None
      self.size = 0
      return temp

    temp = self.tail.info # save the data in the tail
    current = self.head # this is to indicate the position where we start the loop
    for i in range(self.size - 2): # size - 1 wil end up in the node before the tail. Number of jumps = size - 2. (size = 4 we jump twize to end up at the node before the tail)
      current = current.next # increment reaching the node before the tail

    self.tail = current # the element before the last one is now the new tail
    self.tail.next = None # in order to tell the computer that the new tail is current and next is none
    self.size -=1
    return temp # similar to pop()
  
  def print(self):
    if self.size == 0: return None

    current = self.head
    count = 1
    while current != None:
      print("Node {}: ".format(count), current.info)
      count += 1
      current = current.next

n = LinkedList()
n.addToHead(23)
n.addToTail(45)
n.addToHead(21)

n.deleteTail()
n.print()
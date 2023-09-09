#Stacks and Queues

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
    
class Queue: # Using Linked List
  def __init__(self):
    self.elements=LinkedList()

  def enqueue(self,item):
    self.elements.addToTail(item)
    
  def dequeue(self):
    return self.elements.deleteHead()
    
class Stack: # Using list
  def __init__(self):
    self.elements=[]
  def push(self,item):
    self.elements.append(item)
    
  def pop(self):
    if len(self.elements)==0:
      return None
    return self.elements.pop()
    
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print("***")
s=Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.pop())
print(s.pop())
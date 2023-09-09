# My way
def sequential_sort(l): # O(n^2)
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[j] < l[i]: # for descending change here
        temp = l[i]
        l[i] = l[j]
        l[j] = temp
  print(l)

################################################################ 
# Teacher's way
def selection_sort(list1):
  border=0
  while border<len(list1)-1:
    minIndex=border
    
    for i in range(border,len(list1)): 
      if list1[i]<list1[minIndex]: 
        minIndex=i

    temp=list1[border] 
    list1[border]=list1[minIndex]
    list1[minIndex]=temp 

    border+=1

  print(list1)


list1=[1,2,3,4,5,6,7,8,9,10]

# selection_sort(list1)
# print(list1)
sequential_sort(list1)
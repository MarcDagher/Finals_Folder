def selection_sort(list1):
  border=0
  while border<len(list1)-1:
    minIndex=border
    for i in range(border,len(list1)): # looking for minimum
        if (list1[i] % 2 == 0) and (list1[i] > list1[minIndex] or list1[minIndex] % 2 != 0):
 #  found a smaller number, update the index
            minIndex=i
    # swap the min element, with the element at my border
    temp=list1[border]
    list1[border]=list1[minIndex]
    list1[minIndex]=temp
    
    print(list1)

    border+=1


list1=[2,0,3,0,10,-1,6]

selection_sort(list1)

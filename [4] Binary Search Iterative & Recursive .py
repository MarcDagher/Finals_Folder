def binarySearch_iterative(list1,item):
  
  start=0
  end=len(list1)-1
  mid=(start+end)//2 
  
  while mid<=end and mid>=start and start<=end: 

    if list1[mid]==item:
      return True
    
    elif list1[mid]>item:
      end=mid-1
    
    else:
      start=mid+1
    mid=(start+end)//2
  
  return False

# ex=[-10,2,2,3,5,12,54,67,89,100]
# print(binarySearch_iterative(ex,53))

#############################################################################

def recursive_binary_search(list1,start,end, item):

  mid=(start+end)//2 

  if start==end and item != list1[mid]: 
    return False
  
  if list1[mid] == item:
    return True
  
  if list1[mid] > item:
    return recursive_binary_search(list1,start,mid, item)

  elif list1[mid] < item:
    return recursive_binary_search(list1,mid+1,end, item)

# numbers = [2,5,6,3,1,4,55,667,3,123]
# numbers.sort()
# print(numbers)

# print(recursive_binary_search(numbers, 0, len(numbers)-1, 99))
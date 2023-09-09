def merge(list1,start,end): #O(n)
  mid=(start+end)//2

  merged_list=[]

  index1=start 
  index2=mid+1 


  while index1<=mid and index2<= end: 
    if list1[index1]<list1[index2]: 
      merged_list.append(list1[index1]) 
      index1+=1
    else: 
      merged_list.append(list1[index2])
      index2+=1
  
  while index1<=mid: 
      merged_list.append(list1[index1]) 
      index1+=1
  
  while index2<=end: 
      merged_list.append(list1[index2]) 
      index2+=1
      
  
  list1[start:end+1]=merged_list 

def mergesort(list1,start,end):  
   
  if start==end: 
    return
    
  mid=(start+end)//2 
  mergesort(list1,start,mid) 
  mergesort(list1,mid+1,end)

  merge(list1,start,end)

list1=[10,9,8,7,6,5,4,3,2,1]
mergesort(list1,0,len(list1)-1)
print(list1)
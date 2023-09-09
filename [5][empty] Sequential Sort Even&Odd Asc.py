def sequential_sort(l): # O(n^2)
  for i in range(len(l)):

    for j in range(i+1, len(l)):

      if l[j] < l[i]: # for descending change here

        temp = l[i]
        l[i] = l[j]
        l[j] = temp
  print(l)

list1=[10,9,8,7,6,5,4,3,2,1]
sequential_sort(list1)
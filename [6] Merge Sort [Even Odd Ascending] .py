def merge_descending(list1, start, end):  # O(n)
    mid = (start + end) // 2

    # The first sublist starts from start -> mid, the second sublist starts from mid+1 -> end
    merged_list = []

    index1 = start  # Keeps track of the elements added from the first sublist
    index2 = mid + 1  # Keeps track of the elements added from the second sublist

    while index1 <= mid and index2 <= end:

        if list1[index1]%2==0 and  list1[index2]%2==0:  # If numbers are even
             #hon lfr2    ^
            if list1[index1]<list1[index2]:
                merged_list.append(list1[index1])  # Copying from the first sublist
                index1 += 1
            else:
                merged_list.append(list1[index2])  # Copying from the second sublist
                index2 += 1

        elif list1[index1] % 2 == 1 and list1[index2] % 2 == 1: # if numbers are odd

            if list1[index1] < list1[index2]:
                merged_list.append(list1[index1])
                index1 += 1
            else:
                merged_list.append(list1[index2])
                index2 += 1
        
        elif list1[index1] % 2 == 0: # if the first is even but the second is odd
            merged_list.append(list1[index1])
            index1 += 1
        else: # if the second is odd but the first is even
            merged_list.append(list1[index2])
            index2 += 1

    while index1 <= mid:
        merged_list.append(list1[index1])  
        index1 += 1

    while index2 <= end:
        merged_list.append(list1[index2])  
        index2 += 1

    
    list1[start:end + 1] = merged_list

def mergesort_descending(list1, start, end):  
    if start == end: 
        return

    mid = (start + end) // 2
    mergesort_descending(list1, start, mid)  
    mergesort_descending(list1, mid + 1, end)

    merge_descending(list1, start, end)  

list1 = [10,9,8,7,6,5,4,3,2,1]
mergesort_descending(list1, 0, len(list1) - 1)
print(list1)
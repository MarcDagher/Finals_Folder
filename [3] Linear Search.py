# - Linear Search / Sequential Search

# search algorithms
# O(n), n being the length of the list <- write it like this, very nice
# O(len(list1)) <- i do not like this

def sequential_search(list1,item):
  for i in list1:
    if i==item:
      return True
  return False


# print the possible combinations of binary numbers of length(k)
def generate_binary(k,str1): # correction of binary exercise
  if len(str1)==k:
    print(str1)
  else:
    generate_binary(k,str1+"0") 
    generate_binary(k,str1+"1") 
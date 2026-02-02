# program to find the  leader of the array

# what is leaders in an array
#! so basically when the right element to the elemeemt is smaller it is called as leader array
#! lets take an example and try to understand
# arr = [1,2,5,3,0]
#! so in above example we basically have 0 as our right most element so basically we need to understand that the given is leader array becasue there is no any other element right to it therefore it is an ladder array

def leader(arr):
  arr1 = []
  maxelemt = arr[len(arr)-1]
  if(len(arr) == 0):
    return arr
  arr1.append(arr[len(arr)-1])
  for i in range(len(arr)-2,-1,-1):
    if( arr[i] >= maxelemt):
      arr1.append(arr[i])
      maxelemt = arr[i]
  
  arr1.reverse()
  return arr1


arr = [2,4,1,2,3,7,3,5,0]
print(leader(arr))
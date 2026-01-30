# problem statment : given an array nums consisting of only 0,1 or 2 , sort the array in non-decreasing order.
# the sorting should be done in place without using ang extra array

def sortaccording(arr):
  count0 = 0
  count1 = 0
  count2 = 0
  index = 0
  for i in range(len(arr)):
   if(arr[i]==0):
    count0 +=1
   elif(arr[i]==1):
    count1 +=1
   else:
    count2 +=1
   
  for i in range(count0):
    arr[index] = 0
    index+=1
  for i in range(count1):
    arr[index] = 1
    index+=1
  for i in range(count2):
    arr[index] = 2
    index+=1

  

arr = [1,1,1,1,1,1,0,2]
sortaccording(arr)
print(arr)

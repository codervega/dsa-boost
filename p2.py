def linearseach(arr,num):
  for i in range(len(arr)):
    if(arr[i] == num):
      return i   
    
  return -1


arr = [2,1,3,1,89,8,1]
linearseach(arr,1)
print (linearseach(arr,34))
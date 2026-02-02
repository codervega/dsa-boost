def longest(arr):
  
  if(len(arr) == 0):
    return 0
  longest_len = 0
  for i in range(len(arr)):
    num = arr[i]
    count = 1
    
    while num+1 in arr:
      count = count + 1
      num = num + 1
    longest_len = max(longest_len,count)
  return longest_len


arr = [1,52,5,2,53,3,6,4,54,55,56,57]
print(longest(arr))
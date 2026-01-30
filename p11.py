def arrmanipulate(arr):
  n = len(arr)
  pos = 0
  neg = 1
  ans = [0] * n
  for i in range(len(arr)):
    if(arr[i]>0 ):
      ans[pos] = arr[i]
      pos += 2
    else:
      ans[neg] = arr[i]
      neg += 2
  return ans

arr = [2,3,1,3,-3,-2,-1,-2]
print(arrmanipulate(arr))
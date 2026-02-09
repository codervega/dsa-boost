# program to do subset using bitwise

def powerset(arr):
  n = len(arr)
  subset = 1 << n
  i = 0
  ans = []
  while i < subset:
    inner_array = []
    j = 0 
    while j < n:
      if i & 1 << j:
  
        inner_array.append(arr[j])
        
      j += 1
    ans.append(inner_array)
    i+=1
  return ans


arr = [1,2,3]
ans = powerset(arr)
print(ans)
  
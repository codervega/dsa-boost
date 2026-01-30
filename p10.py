# kadanes algorithm
def kadanes(arr):
  cur_sum = 0
  index = 0
  start = 0
  end = 0
  temp_start = 0
  max_sum = float('-inf')
  for k in range(len(arr)):

    cur_sum = cur_sum + arr[k]
    if( cur_sum > max_sum):
      max_sum = cur_sum
      start = temp_start
      end = k
    if(cur_sum < 0):
      cur_sum = 0
      temp_start = k+1
  return [start,end]

arr =[10,-14,23,0,-98,98,43,67,-32512,53,12,56,3,1]
ans = kadanes(arr)
print(ans)
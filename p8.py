# problem based on the the two sum equal to target 

# def check(arr,k):
#   hash_mp = {}
#   complete = 0
#   for i in range(len(arr)):
#     complete = k - arr[i]
#     if(complete in hash_mp):
#       return [i,hash_mp[complete]]
#     hash_mp[arr[i]] = i
#   return [-1,-1]

# arr = [1,2,1,5]
# print(check(arr,6))


# this is basically using o(nlogn)
# we can achive this in o(n) and space complexity 0(1)

# well we can do this using simple two pointer approch 


def check(arr,k):
  arr.sort()
  i = 0
  j = len(arr)-1
  while(i<j):
    sum = arr[i] + arr[j]
    if(sum == target):
      return [i,j]
    elif(sum > target):
      j -=1
    else:
      i +=1
  return [-1,-1]

arr = [1,2,1,2,3,1,2,3,8]
target = 10
print(check(arr,target))

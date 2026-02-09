arr = [1,2,1,2,3,5,5]
ans = 0
for i in range(len(arr)):
  ans += arr[i] ^ ans

print(ans)
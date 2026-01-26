#program to find missing number in the series

# we can perform the this problem in three ways that is in using first way brute force second two pointers and the last using sum of n natural number 

# lets write code for this 

#! using brute force

def duplicate(arr,n):
   sum = n*(n+1)/2
   sumarr = 0
   for i in arr:
      sumarr += i
   return sum - sumarr 



arr = [1,2,3,5]

n = 5
ans=duplicate(arr,n)
print(ans)
 #! above is better approch but not the optimal solution we should do optimal solution 
# ! that possible through using xor

def xorapproch(arr,n):
   xor1 = 0
   xor2 = 0
   for i in range(n):
      xor2 ^= arr[i]
      xor1 ^= (i+1)
      xor2 *= n

   return xor1^xor2
    

print("this is basically using xor approch")
ans2 = xorapproch(arr,n)
print(ans2)

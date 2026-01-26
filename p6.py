# program to find single element in an array where every element is present twice except one element

# def singleelement(arr):
#   count = len(arr) 
  
#   hash_map = [0] * count
#   for i in range(len(arr)):
#     hash_map[arr[i]] += 1
    
#   for i in range(len(hash_map)):
#     if(hash_map[i] == 1):
#       return i
  
#   return -1

arr = [1,3,3,2,1,2,4,4,5,5,9]
# print(singleelement(arr))

#! well above code is absically using hashing technique but we can do this optimally using xor operation

def optimalappach(arr):
    xor = 0
    for i in range(len(arr)):
      xor ^= arr[i]
    return xor

print("this is optimal approch using xor operation")
print(optimalappach(arr))



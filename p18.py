# # will be learning about operators here 
# #! bitwise operator here 

# # swapiing two number using xor operator

# a = 50
# b = 20

# a = a ^ b
# b = a  ^ b
# a = a  ^  b 

# print(a)
# print(b)

# # ! program to check if the number is n-th bit is set

# n = 7

# i = 4

# ans = 7 << 1

# final = ans & n

# if (final > 0):
#   print("its a set")
# else:
#   print("not a set")

# print(2 and 2)

# def multiply(a, b):
#     result = 0
    
#     while b > 0:
#         if b & 1:        # check last bit
#             result += a
        
#         a = a << 1       # multiply a by 2
#         b = b >> 1       # divide b by 2
    
#     return result


# print(multiply(13,3))

# # toggle nth bit in the given number
# num1 = 13
# i = 1
# print("----------------------------")
# print((1 << 1) ^ num1)

# #! is the given number a power of two or not
# num2 = 4
# pow = num2 & (num2 - 1)
# if(pow == 0):
#    print("power of two")
# else:
#    print("now power of two")


# #! program to find the set bit in a number
# num4 = 13
# def countset(num4):
#   bin = ""
#   count = 0
#   while (num4 > 0):
#     rem = num4 % 2
#     bin =  str(rem) + bin
#     num4 = num4 // 2
#     if(rem == 1):
#       count += 1
#   return count,bin

# print(countset(num4))

#! well above is using using without bitwise operator now lets do with bitwise operator
def countset(num4):
  count = 0 
  while num4 > 0:
    if num4 & 1:
      count = count + 1
    num4 = num4 >> 1
  return count

num4 = 5
print(countset(num4))


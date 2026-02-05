# will be learning about operators here 
#! bitwise operator here 

# swapiing two number using xor operator

a = 50
b = 20

a = a ^ b
b = a  ^ b
a = a  ^  b 

print(a)
print(b)

# ! program to check if the number is n-th bit is set

n = 7

i = 4

ans = 7 << 1

final = ans & n

if (final > 0):
  print("its a set")
else:
  print("not a set")


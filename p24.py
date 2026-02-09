# program to find the xor of given numbers 
n = 5
l = 2
#! here l means start and n means it is end

# remember this pattern also its the most important thing to remember 

#? if n % 4 = 1 then 1 xor n is gonna be 1
#? if n % 4 = 1 then 1 xor n is gonna be n + 1
#? if n % 4 = 3 then 1 xor n is gonna be 1
#? if n % 4 = 0 then 1 xor n is gonna be n

def pattern(n):
  if n%4 == 1:
    return 1
  elif n%4 == 2:
    return n+1
  elif n%4 == 3:
    return 0
  elif n%4 == 0:
    return n

def acccept(l, n):
  return pattern(l)^pattern(n)

print(acccept(l,n))


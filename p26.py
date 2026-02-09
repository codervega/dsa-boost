# program to find the power of number using bitwise operator

def power(a,b):
  if(b == 0):
    return 1
  result = 1
  negative = False
  if(b < 0):
    b = -b
    negative = True

  while b > 0:
    if(b & 1):
      result *= a
    
    a = a << 1
    b = b >> 1

  if negative:
    return 1/result
  return result

print(power(2,-2))



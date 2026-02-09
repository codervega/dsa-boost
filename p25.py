# program to mulltply two number without using  or multiplicator operator or any recusrion 

def multiply(a,b):
  ans = 0
  while(a > 0):
    if(a & 1):
      ans += b
    
    a = a >> 1
    b = b << 1
  return ans

print(multiply(10,20))
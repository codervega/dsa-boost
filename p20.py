

def division(DIVIDENT, Divisor):
  if( DIVIDENT == Divisor):
    return 1
  sign = "true"
  if(Divisor < 0 and DIVIDENT > 0):
    sign = "False"
  if(Divisor > 0 and DIVIDENT < 0):
     sign = "False"

  D = abs(DIVIDENT)
  d = abs(Divisor)

  ans = 0
  while( D >= d ):
    temp = d
    multi = 1
    while(temp >= temp << 1):
      temp = temp << 1
      multi = multi << 1
    
    D = D - temp
    ans = ans + multi
  if(sign == "False"):
    return -1*ans
  else:
    return ans


ans=division(-3,-3)
print(ans)
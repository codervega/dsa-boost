def palindrome(number):
  ans = number[::-1]
  if number != ans:
    return False
  else:
    return True

def convert(i,n):
  ans = ""
  while (n>1):
    qocent = n%i
    ans = str(qocent) + ans
    n = n // i
  return ans

def stricky_palindrome(n):
  for i in range(2,n-1):
    convertedtobase = convert(i,n)
    if not palindrome(convertedtobase):
      return False
  return True

ans = stricky_palindrome(9)
print(ans)
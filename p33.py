
#! program to check wether number is anagram or not

def anagram(str1,str2):
  if(len(str1) != len(str2)):
    return False
  
  count = {}

  for ch in str1:
    if ch not in count:
      count[ch] = 1
    else:
      count[ch] += 1
    
  for ch in str2:
    if ch not in count:
      return False
    count[ch] -= 1

  return True

ans = anagram("India","India")
if(ans == False):
  print("it's not an anagram")
else:
  print("it's an anagram")
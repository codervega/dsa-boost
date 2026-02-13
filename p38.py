
# You are given two strings str1 and str2.

# Your task is to determine whether any substring of str2 is a shuffled (anagram) version of str1.

def shuffle(str1,str2):
  m = len(str1)
  n = len(str2)
  if m > n:
    return False
  freq = {}
  for ch in str1:
    if ch not in freq:
      freq[ch] = 1
    else:
      freq[ch] += 1
  window = {}
  for i in range(m):
    ch = str2[i]
    if ch not in window:
      window[ch] = 1
    else:
      window[ch] += 1
  
  if window == freq:
    return True
  
  for i in range(m,n):
    new_ch = str2[i]
    old_ch = str2[i-n]

    if new_ch not in window:
      window[new_ch] = 1
    else:
      window[new_ch] = +1
    
    window[old_ch] -= 1
    del window[old_ch]

    if window == freq:
      return True
    
  return False


str2 = "Abgusgejdjhi"
str1 = "Abhi"
ans = shuffle(str1,str2)
if(ans == True):
  print("it is suffle string")
else:
  print("It is not suffle string")
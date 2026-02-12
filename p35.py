
#! remove duplicate character in from the strings

def duplicate(string1):
  ans = set()
  for ch in string1:
    ans.add(ch)
  return ans

print(duplicate("bannana"))
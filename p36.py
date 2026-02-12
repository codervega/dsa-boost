
#! program to remove all ajuacent duplicate from string

string = "aabbaca"

def removepairduplicate(string1):
  stack = []
  for ch in string1:
    if stack and stack[-1] == ch:
      stack.pop()
    else:
      stack.append(ch)
  return stack

print(removepairduplicate("abbaca"))
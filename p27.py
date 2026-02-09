
#! program to reverse a string using stack
def reverse(string1):
  n = len(string1)
  stack = []
  for str in string1:
    stack.append(str)
  
  string2 = ''
  while stack:
    string2 = string2 + stack.pop()
  
  return string2

res = reverse("My Name is Abhishek Shukla")
print(res)

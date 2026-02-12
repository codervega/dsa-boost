
# program to check the rotation of string in the array

def checkrotation(str1,str2):
  if(len(str1) != len(str2)):
    return False
  sum = str1 + str1
  if str2 in sum:
    return True
  else:
    return False
  
ans = checkrotation("Abhishek","kAbhishe")
if(ans == True):
  print("rotation of array")
else:
  print("not a rotation")
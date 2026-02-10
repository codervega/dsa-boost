
#! program to count uppercase and lowercase

def count(string1):
  count_up = 0
  count_down = 0
  for w in string1:
    if(w.isupper()):
      count_up += 1
    elif(w.islower()):
      count_down += 1
    else:
      continue
  return count_down,count_up

print(count("Abhishek Shukla"))

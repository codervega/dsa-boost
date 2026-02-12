
#! program to find first none reapting character in the string

def first_non_repeating(string1):
  for i in range(len(string1)):
    count = 0
    for j in range(len(string1)):
      if(string1[i] == string1[j]):
        count += 1
    if(count == 1):
        return string1[i]
  return None

print(first_non_repeating("aabbcdde"))
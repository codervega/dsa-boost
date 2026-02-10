
#! program to find vowel and consonents count

def voco(string1):
  vowal_count = 0
  consonent_count = 0
  for ch in string1:
    if(ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U"):
      vowal_count += 1
    else:
      consonent_count += 1
  
  # arr = []
  # arr.append(vowal_count)
  # arr.append(consonent_count)
  return vowal_count,consonent_count

print(voco("ABHISHEK"))
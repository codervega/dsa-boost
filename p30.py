
#! program to calculate the frequwncy of a character in a string

def frequency(string1):
  hash_mp = {} 
  for ch in string1:
    if ch in hash_mp:
      hash_mp[ch] += 1
    else:
      hash_mp[ch] = 1
  
  return hash_mp

ans = frequency("Abhishekrrrrrrrrrr")
print(ans)

#! program to remove spaces from the string
string2 = "hello world python"
ans = string2.split(" ")
ans2=''.join(ans)
print(ans2)


#! program to find the largest world in sentence

example = " I Love America, In the History of America we only love Epstine file"
ans = example.split(' ')
length = float('-inf')
string1 = ''
for ch in ans:
  if (len(ch) > length):
    length = len(ch)
    string1 = ch
print(string1)
# writing program to find union of two arrays

a = [1,3,1,3,5,2,4]
b = [2,1,3,3,1,87,54]
set1 = set()
for i in range(len(a)):
  set1.add(a[i])

for i in range(len(b)):
  set1.add(b[i])

temp = []

for i in set1:
  temp.append(i)

print(temp)

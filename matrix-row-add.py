def addrow(matrix):
  final = []
  for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[0])):
      sum = sum + matrix[i][j]
    final.append(sum)
  return final

row = int(input())
col = int(input())

matrix = []
for i in range(row):
  row1 = []
  for j in range(col):
    val = int(input())
    row1.append(val)
  matrix.append(row1)
ans = addrow(matrix)
print(ans)

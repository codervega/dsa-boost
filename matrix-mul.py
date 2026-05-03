

def mul(matrix,matrix1):
  final = []
  sum = 0
  for i in range(len(matrix)):
    row = []
    for j in range (len(matrix1[0])):
      sum = 0
      for k in range(len(matrix[0])):
        sum += matrix[i][k] * matrix1[k][j]
      row.append(sum)
    final.append(row)
  return final


row = int(input())
col = int(input())

matrix = []
for i in range(row):
    row01 = []
    for j in range(col):
        val = int(input())
        row01.append(val)
    matrix.append(row01)


# second matrix
row1 = int(input())
col2 = int(input())

matrix1 = []
for i in range(row1):
    row02 = []
    for j in range(col2):
        val = int(input())
        row02.append(val)
    matrix1.append(row02)


# check condition
if col != row1:
    print("Multiplication not possible")
else:
    print(mul(matrix, matrix1))
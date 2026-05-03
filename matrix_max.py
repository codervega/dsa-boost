

def check(matrix):
  max_len = matrix[0][0]
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      if(max_len < matrix[row][col]):
        max_len = matrix[row][col]
  return max_len



print("enter no of rows")
rows = int(input())
print("enter no of colums")
col = int(input())
matrix = []
for row in range(rows):
  rows1 = []
  for col1 in range(col):
    val = int(input())
    rows1.append(val)
  matrix.append(rows1)

print("the max value in the matrix is")
ans = check(matrix)
print(ans)

# 

rows = int(input())
cols = int(input())

matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print(matrix)
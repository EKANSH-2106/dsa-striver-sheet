m=len(matrix)
n=len(matrix[0])

rows=[0]*m
cols=[0]*n

for i in range(m):
    for j in range(n):
        if matrix[i][j]==0:
            rows[i]=1
            cols[j]=1

for i in range(m):
    for j in range(n):
        if rows[i] or cols[j]:
            matrix[i][j]=0

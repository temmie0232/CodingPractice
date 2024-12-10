
r,c = map(int,input().split())

matrix = []
row = []
total_row = []

# 表の作成(一行ずつ追加)
for i in range(r):
    row = list(map(int,input().split()))
    matrix.append(row)
    
for i in range(r):
    row = sum(matrix[i])
    matrix[i].append(row)

for i in range(c+1):
    total = 0
    for j in range(r):
        total += matrix[j][i]
    total_row.append(total)

matrix.append(total_row)

for i in range(r+1):
    for j in range(c+1):
        print(f"{matrix[i][j]}",end="")
        if j != c:
            print(" ",end="")
    print()
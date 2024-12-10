
n, m = map(int,input().split())

matrix = []

c = []
ans = [0 for i in range(n)]

for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

for i in range(m):
    y = int(input())
    c.append(y)

for i in range(n):
    for j in range(m):
        ans[i] += matrix[i][j] * c[j]

for i in ans:
    print(i)
n,m,l = map(int,input().split())

row = []
matrix_A = []
matrix_B = []
matrix_C = [[0] * l for _ in range(n)]

for i in range(n):
    row = list(map(int,input().split()))
    matrix_A.append(row)

for i in range(m):
    row = list(map(int,input().split()))
    matrix_B.append(row)


for i in range(n):
    for k in range(m):
        for j in range(l):
            matrix_C[i][j] += matrix_A[i][k]*matrix_B[k][j]

for i in range(n):
    for j in range(l):
        print(f"{matrix_C[i][j]}",end="")
        if j != l-1:
            print(" ",end="")
    print()
        
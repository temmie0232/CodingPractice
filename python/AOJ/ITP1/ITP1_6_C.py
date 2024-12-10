
# 初期化
room = [[[0 for i in range(10)] for j in range(3)] for i in range(4)]

# 情報数
n = int(input())

# b棟f階r番v人
for i in range(n):
    b,f,r,v = map(int,input().split())
    room[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        for k in range(10):
            print(f" {room[i][j][k]}",end="")
        print()
    if i!=3:
        print("#"*20)
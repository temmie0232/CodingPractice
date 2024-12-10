
n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

for p in range(1,4):
    dxy = 0
    d = []
    for i in range(n):
        d.append(abs(x[i]-y[i])**p)
        
    dxy = sum(d)**(1/p)
    print(dxy)

dxy = 0
d = []

for i in range(n):
    d.append(abs(x[i]-y[i]))

print(max(d))
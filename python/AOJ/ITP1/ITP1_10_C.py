
import math


while True:
    
    n = int(input())

    if n==0:
        break

    s = list(map(float,input().split()))

    avg = sum(s)/len(s) 

    x = []
    
    for i in range(n):
        x.append((s[i]-avg)**2)

    h = math.sqrt(sum(x)/len(s))

    print(h)
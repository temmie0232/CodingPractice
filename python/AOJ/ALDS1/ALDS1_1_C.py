
import math

def isPrime(i):
    flag = True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            flag = False
            break
    return(flag)
    
    
n = int(input())
a = []
count = 0

for i in range(n):
    a.append(int(input()))
    
for i in a:
    if isPrime(i):
        count+=1

print(count)
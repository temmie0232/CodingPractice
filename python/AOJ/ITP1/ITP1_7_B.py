
def func(n,x):
    ans = 0
    n_ = n+1
    for i in range(1,n_):
        for j in range(i+1,n_):
            for k in range(j+1,n_):
                if i+j+k == x:
                    ans += 1
    return ans
            

while True:
    n, x = map(int,input().split())
    if (n,x) == (0,0):
        break
    
    print(func(n,x)) 
    
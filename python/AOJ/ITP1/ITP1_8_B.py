
while True:
    ans = 0
    n = input()
    
    if n=="0":
        break
    
    for i in n:
        ans += int(i)
    print(ans)
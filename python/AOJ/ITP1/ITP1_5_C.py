while True:

    h,w = map(int,input().split())

    if (h,w)==(0,0):
        break
    
    for i in range(h):
        for j in range(w):
            if ((i+1)+(j+1))%2==0:
                print("#",end="")
            else:
                print(".",end="")
        print("")
    print("")
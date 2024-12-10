
def checkCircleInSquare(w,h,x,y,r):
    if x-r<0 or y-r<0 or x+r>w or y+r>h:
        return False
    else:
        return True

w,h,x,y,r = map(int,input().split())

if checkCircleInSquare(w,h,x,y,r) == False:
    print("No")
else:
    print("Yes")
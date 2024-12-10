
def sortTwoValue(x,y):
    if x>y:
        x,y = y,x
    return x,y

x,y = 1,1

while True:
    x,y = map(int,input().split())
    
    if x == 0 and y == 0:
        break
    
    x,y = sortTwoValue(x,y)
    print(x,y)

def shuffle(s):
    h = int(input())
    for i in range(h):
        temp = s.pop(0)
        s.append(temp)
    return s

while True:
    
    s = input()
    
    if s=="-":
        break
    
    s = list(s)
    
    n = int(input())

    for i in range(n):
        shuffle(s)

    print("".join(s))




def grading(m,f,r):
    point = m+f
    if m == -1 or f == -1:
        return "F"
    if point < 30:
        return "F"
    if point >= 80:
        return "A"
    elif 80 > point >= 65:
        return "B"
    elif 65 > point >= 50:
        return "C"
    elif 50 > point >= 30:
        if r >= 50:
            return "C"
        else:
            return "D"


while True:
    m,f,r = map(int,input().split())
    if (m,f,r) == (-1,-1,-1):
        break
    print(grading(m,f,r))



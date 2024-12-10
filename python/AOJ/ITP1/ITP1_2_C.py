
def sort_(a,b):
    if a > b:
        a,b = b,a
    return a,b

a,b,c = map(int,input().split())

a,b = sort_(a,b)
b,c = sort_(b,c)
a,b = sort_(a,c)

print(a,b,c)
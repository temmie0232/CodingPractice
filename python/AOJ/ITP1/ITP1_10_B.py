
import math

a, b, c = map(float,input().split())

c = math.radians(c)

s = 1/2*(a*b*math.sin(c))

# もう1辺の長さ
c_ = math.sqrt(((a**2)+(b**2))-(2*a*b*math.cos(c)))

l = a + b + c_
h = (2*s)/a

print(s)
print(l)
print(h)

import math

n = int(input())

h = math.floor(n / 3600)
m = math.floor((n % 3600) / 60)
s = ((n % 3600) % 60)%60

print(f"{h}:{m}:{s}")
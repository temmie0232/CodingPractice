
p_taro = 0
p_hanako = 0

t_cards = []
h_cards = []

n = int(input())

for i in range(n):
    taro, hanako = input().split()

    if taro == hanako:
        p_taro += 1
        p_hanako += 1
    elif taro < hanako:
        p_hanako += 3
    else:
        p_taro += 3
    
print(p_taro,p_hanako) 
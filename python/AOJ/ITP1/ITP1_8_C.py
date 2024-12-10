array = []
while True:
    try:
        s = input().lower()
        array.append(s)
    except:
        break
    
n = [0 for i in range(26)]

for string in array:
    for c in string:
        if c.isalpha():
            index = ord(c)-97
            n[index] += 1

for i in range(26):
    print(f"{chr(i+97)} : {n[i]}")
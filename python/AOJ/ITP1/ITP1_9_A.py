
t = []
count = 0

w = input()

while True:
    temp = input()
    if temp == "END_OF_TEXT":
        break
    t.append(temp.lower().split())

for words in t:
    for word in words:
        if word == w:
            count += 1

print(count)
        
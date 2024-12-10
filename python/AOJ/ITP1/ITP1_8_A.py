
string = input()
string_update = []
n = len(string)

for i in range(n):
    if string[i].isalpha():
        if string[i].islower():
            string_update.append(string[i].upper())
        if string[i].isupper():
            string_update.append(string[i].lower())
    else:
        string_update.append(string[i])

print("".join(map(str,string_update)))
        
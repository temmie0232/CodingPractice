
s = input()
n = int(input())

for i in range(n):
    command, a, b, *rest = input().split()
    rp = rest[0] if rest else None
    a = int(a)
    b = int(b)

    if command == "print":
        print(s[a:b+1])
    elif command == "replace":
        if rp:
            s = s[:a] + rp + s[b+1:] 
    elif command == "reverse":
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    
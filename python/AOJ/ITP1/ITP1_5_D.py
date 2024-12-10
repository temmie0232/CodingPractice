def call(n):
    i = 1
    while i <= n:
        x = i
        if x % 3 == 0:
            print(f" {i}", end="")
        else:
            while x > 0:
                if x % 10 == 3:
                    print(f" {i}", end="")
                    break
                x //= 10
        i += 1
    print()

n = int(input())

call(n)
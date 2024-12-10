

while True:

    inputs = input().split()

    a = int(inputs[0])
    op = inputs[1]
    b = int(inputs[2])

    
    if op == "?":
        break
    elif op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a//b)
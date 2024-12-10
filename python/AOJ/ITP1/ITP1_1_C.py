
def main() -> None:
    a: int
    b: int
    a,b = map(int,input().split())
    print(getSquareArea(a,b),getSquarePerimeter(a,b))

def getSquareArea(x: int, y: int) -> int:
    z: int = x * y
    return z

def getSquarePerimeter(x: int, y:int) -> int:
    z: int = x*2 + y*2
    return z


if __name__ == "__main__":
    main()
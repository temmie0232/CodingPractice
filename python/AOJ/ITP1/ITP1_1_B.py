
def main() -> None:
    x: int = int(input())
    print(XCubic(x))

def XCubic(x: int) -> int:
    y: int = x**3
    return y
    
if __name__ == "__main__":
    main()
inf = float('inf')
def solution():
    for _ in range(int(input())):
        n = int(input())
        if n % 3 == 0:
            print(n//3)
        elif n == 1:
            print(2)
        elif n % 3 == 1:
            print(n//3 + 1)
        else:
            print(n//3 + 1)


if __name__ == "__main__":
    solution()
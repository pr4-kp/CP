inf = float('inf')
def solution():
    for _ in range(int(input())):
        n, s = map(int, input().split())
        if n <= s:
            to = s
        else:
            to = (-(-n//s)) * s
        print(-(-to//n))
            


if __name__ == "__main__":
    solution()
def solution():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    c = 0
    t = 0
    while t <= x and c<n:
        t += A[c]
        c += 1
    if c == n:
        print(n)
    else:
        print(c-1)

if __name__ == "__main__":
    solution()
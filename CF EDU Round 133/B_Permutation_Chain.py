inf = float('inf')
def solution():
    for _ in range(int(input())):
        n = int(input())

        p = list(range(1, n+1))
        print(n)
        print(*p)

        for ii in range(n-1): 
            p[ii], p[ii+1] = p[ii+1], p[ii]
            print(*p)


if __name__ == "__main__":
    solution()
def solution():
    N = int(input())
    mm = 0
    xx = list(map(int, input().split()))
    yy = list(map(int, input().split()))

    for a in range(N):
        for b in range(N):
            if mm < (xx[a]-xx[b])**2 + (yy[a]-yy[b])**2:
                mm = (xx[a]-xx[b])**2 + (yy[a]-yy[b])**2
    print(mm)


if __name__ == "__main__":
    solution()
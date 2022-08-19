inf = float('inf')
def solution():
    Wormholes = []
    n, m = map(int, input().split())
    P = list(map(int, input().split()))
    for jj in range(m):
        Wormholes.append(list(map(int, input().split())))

    if P == list(range(1,n+1)):
        print(-1)
    else:
        



if __name__ == "__main__":
    solution()
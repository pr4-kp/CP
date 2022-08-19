import sys
input = sys.stdin.readline
inf = float('inf')

def solution():
    n, m = map(int, input().split())
    A = [[] for ii in range(n)]
    for ii in range(n): 
        A[ii] = list(map(int, input().split()))
    temp = 0
    print(*A, sep='\n')
    # print(sorted(A, key=lambda x: x[0]))
    for ii in range(n):
        for jj in range(n):
            new = []
            for v1, v2 in zip(A[ii], A[jj]):
                new.append(max(v1, v2))
            if min(new) > temp:
                best = [ii, jj]
                temp = min(new)
    print(best[0] + 1, best[1] + 1)

if __name__ == "__main__":
    solution()
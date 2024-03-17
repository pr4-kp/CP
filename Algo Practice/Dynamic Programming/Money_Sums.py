import sys
# # (optional) very fast input
#import io
#import os

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
inf = float('inf')
def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

"""
--- Notes ---

"""

def solution():
    n = int(input())
    a = arr_in()
    MAX = sum(a)
    possible = [0] * (MAX + 1)
    possible[0] = 1
    temppossible = [0] * (MAX + 1)
    for ii in range(n):
        for jj in range(MAX):
            if possible[jj] and jj + a[ii] <= MAX:
                temppossible[jj + a[ii]] = 1
            
        possible = [possible[ii] | temppossible[ii] for ii in range(MAX + 1)]
        temppossible = [0] * (MAX + 1)
    
    # print(possible)
    ans = []
    for ii in range(MAX + 1):
        if possible[ii] and ii != 0:
            ans.append(ii)
    print(len(ans))
    print(*ans)
if __name__ == "__main__":
    solution()
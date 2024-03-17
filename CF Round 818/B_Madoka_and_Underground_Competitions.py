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
    for _ in range(int(input())):
        n, k, r, c = tup_in()
        arr = [(["."] * n) for i in range(n)]
        
        arr[r-1][c-1] = 'X'

        if k == 1:
            arr = [(["X"] * n) for i in range(n)]
        else:
            target = (r + c - 2) % k
            for ii in range(n):
                for jj in range(n):
                    if (ii + jj) % k == target:
                        arr[ii][jj] = 'X'

        [print(''.join(map(str, a))) for a in arr]



if __name__ == "__main__":
    solution()
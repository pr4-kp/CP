import sys
# # (optional) very fast input
#import io
#import os

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
MAX = 10 ** 9 + 7
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
    to = ((n * (n + 1)) // 2)
    if to % 2 == 0:
        to //= 2
        possible = [0] * (to + 1)
        possible[0] = 1
        temppossible = [0] * (to + 1)

        for ii in range(1, n + 1):
            for jj in range(to + 1):
                if possible[jj] and jj + ii <= to:
                    temppossible[jj + ii] += possible[jj] % MAX

            possible = [(possible[ii] + temppossible[ii]) % MAX for ii in range(to + 1)]
            temppossible = [0] * (to + 1)
        # print(possible)
        print((possible[to] * 500_000_004) % MAX)
    else:
        print(0)

if __name__ == "__main__":
    solution()
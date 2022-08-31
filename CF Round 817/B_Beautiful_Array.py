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
b - sum of beauty
s - sum or original array
n - number of elements in array
k - number to divide by
"""

def solution():
    for _ in range(int(input())):
        n, k, b, s = tup_in()
        if s // k < b:
            print(-1)
        elif s // k == b:
            arr = [0] * n
            arr[-1] = s
            print(*arr)
        elif s > (b * k + (n) * (k - 1)):
            print(-1)
        else:
            ct = n - 2
            arr = [0] * n
            arr[-1] = s
            while arr[-1] // k > b and ct >= 0:
                arr[-1] -= (k - 1)
                arr[ct] = k - 1
                ct -= 1
            print(*arr)
            

if __name__ == "__main__":
    solution()
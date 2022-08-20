import sys
#import io
#import os

# # very fast input
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
        n, k, b, s = tup_in()

        if n == 1:
            if s // k == b:
                print(s)
            else:
                print(-1)
        else:
            A = [0] * n
            A[0] = s
            if s // k < b:
                print(-1)
            else:
                for ii in range(1, n):
                    if A[0] // k > b:
                        A[0] -= k - 1
                        A[ii] = k - 1
                    else:
                        break
                if A[0] // k > b:
                    print(-1)
                else:
                    print(*A)

if __name__ == "__main__":
    solution()
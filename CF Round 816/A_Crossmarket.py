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
        n, m = tup_in()
        A = sorted([n, m])
        if A[0] == 1:
            if A[1] == 1:
                print(0)
            else:
                print(A[1])
        else:
            print(A[0] * 2 + A[1] - 2)

if __name__ == "__main__":
    solution()
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
        n = int(input())
        S = arr_in()
        v = input()

        fails = set()

        sc = 0

        for ch in v:
            if ch == '0':
                fails.add(S[sc])
            sc += 1

        print(min(fails))



if __name__ == "__main__":
    solution()
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
    maxa = 0
    a = arr_in()
    stack = []

    for i, v in enumerate(a):
        start = i 
        while stack and v < stack[-1][1]:
            cur = stack[-1]
            stack.pop()
            start = cur[0]
            maxa = max(maxa, (i - cur[0]) * cur[1])
        stack.append([start, v])

    while stack:
        cur = stack[-1]
        stack.pop()
        maxa = max(maxa, (n - cur[0]) * cur[1])
        print(stack)

if __name__ == "__main__":
    solution()
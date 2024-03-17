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
    ans = [0] * n 
    stack = [[0, 0]]
    for ind, val in enumerate(a):
        while stack and stack[-1][1] >= a[ind]:
            stack.pop()
        print(stack[-1][0], end=' ')
        stack.append([ind + 1, val])
            
        

if __name__ == "__main__":
    solution()
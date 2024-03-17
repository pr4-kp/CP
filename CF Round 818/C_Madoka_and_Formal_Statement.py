import sys
# (optional) very fast input
import io
import os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline
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
    b = arr_in()
    if a == b: 
        return 1

    ignore = [False] * n

    for ii in range(n - 1):
        if a[ii] != b[ii] and b[ii + 1] + 1 < b[ii]:
            return 0
        elif a[ii] > b[ii]:
            return 0
    
    if a[n - 1] != b[n - 1] and b[0] + 1 < b[n - 1]:
        return 0
    elif a[n - 1] > b[n - 1]:
        return 0
    else:
        return 1

if __name__ == "__main__":
    for _ in range(int(input())):
        if solution():
            print("YES")
        else:
            print("NO")
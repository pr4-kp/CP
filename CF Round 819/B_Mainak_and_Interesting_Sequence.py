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
    n, m = tup_in()
    if m < n:
        return 0
    if n == 1:
        return [m]
    a = [1] * n 
    m -= n
    if m > n - 1 and n % 2 == 1:
        a[0] += m 
        return a
    elif m % 2 == 0 and n % 2 == 0:
        if m % 2 == 1:
            a[0] += m 
        else:
            a[0] += m // 2
            a[1] += m // 2
        return a
    elif n % 2 == 0 and m % 2 == 0:
        a[0] += m // 2


if __name__ == "__main__":
    for _ in range(int(input())):
        a = solution()
        if a:
            print("YES")
            print(*a)
        else:
            print("NO")
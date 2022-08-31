import sys
# # (optional) very fast input
#import io
#import os

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
inf = float('inf')
"""
--- Notes ---

"""

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def solution():
    n = int(input())
    mult = list(map(lambda x: sum_digits(x * n), range(1,10)))
    print(mult)

if __name__ == "__main__":
    solution()
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
if n divides anything above it, we can remove it.
It is always worse to take a gcd of something that isn't the above case:
proof: gcd(a,b) >= 2b > a + b or gcd(a, b) = b < a + b. 

"""

def solution():
    for _ in range(int(input())):
        n = int(input())
        A = reversed(list(set(arr_in())))

        print(sum(A))




if __name__ == "__main__":
    solution()
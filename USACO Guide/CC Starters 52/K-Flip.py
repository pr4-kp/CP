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
If ii == 1, then start flipping everything, return 0000000...000

k = 5
10111011101
01111011101

Greedy, just flip the first 1 and everything after. O(nk) gives TLE
01111011101 XOR
01111100000
"""

def solution():
    for _ in range(int(input())):
        n, k = tup_in()
        S = int(input(), 2)

        n = S.bit_length()
        while n >= 1 << k - 1:
            S ^= (1 << k - 1) << (n - k)
            n = S.bit_length()

        print(bin(S)[2:])



if __name__ == "__main__":
    solution()
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

# --- BEGIN PREFIX SUM ---
"""
- O(n) preprocessing time
- O(1) range sum query
"""
def psum(l, n):
    p = [0]
    for i in range(n):
        p.append(p[-1])
        p[-1] ^= l[i]
    return p
# --- END PREFIX SUM ---

def solution():
    n, q = tup_in()
    X = arr_in()
    pref_sum_x = psum(X, n)
    for _ in range(q):
        l, r = tup_in()
        print(pref_sum_x[r] ^ pref_sum_x[l - 1])
    

if __name__ == "__main__":
    solution()
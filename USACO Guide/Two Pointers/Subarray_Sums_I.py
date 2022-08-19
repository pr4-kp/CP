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


# --- BEGIN PREFIX SUM ---
"""
- O(n) preprocessing time
- O(1) range sum query
"""
def psum(l, n):
    p = [0]
    for i in range(n):
        p.append(p[-1])
        p[-1] += l[i]
    return p
# --- END PREFIX SUM ---
"""
--- Notes ---

"""

def solution():
    n, x = tup_in()
    A = arr_in()
    PSA = psum(A, n)
    ans = 0

    left = 0
    right = 0

    while left != n + 1 and right != n + 1:
        if PSA[right] - PSA[left] < x:
            right += 1
        elif PSA[right] - PSA[left] > x:
            left += 1
        else:
            left += 1
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    solution()
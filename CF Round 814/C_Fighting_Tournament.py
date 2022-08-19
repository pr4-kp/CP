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
For the query for person i, first check if anyone higher is before them.
Then just check for the next highest person

If the person is the most powerful fighter, then the answer depends on k
Also, if they are in position 1, then we just have to subtract 1 from the answer.

Moral: Don't get over-confused. There were two edge cases I had to consider. 
I was able to think of the first one on first submission. 
However, the second one made me write over-complicated code.
"""

# --- BEGIN SPARSE TABLE ---
"""
- O(nlog(n)) preprocessing time
- O(1) range min/max/gcd/lcmetc. query
- Use when the value of two intersecting intervals is the same as the the value of the union of those intervals
"""
N_MAX = 2 * 10 ** 5 + 1

def precalc_log(m = N_MAX):
    global LOG
    LOG = [0] * m
    for ii in range(2, m):
        LOG[ii] = LOG[ii // 2] + 1
def precalc_sparse_table(A):
    global ST
    n = len(A)
    size = LOG[n]
    ST = [[0 for jj in range(n + 1 - (1 << ii))] for ii in range(size + 1)]
    ST[0] = A
    for ii in range(1, size + 1):
        for jj in range(0, n + 1 - (1 << ii)):
            ST[ii][jj] = max(ST[ii - 1][jj], ST[ii - 1][jj + (1 << (ii - 1))])
def query(l, r):
    log_range = LOG[r - l + 1]
    return max(ST[log_range][l], ST[log_range][r - (1 << log_range) + 1])
# --- END SPARSE TABLE ---

def solution():
    precalc_log()
    for _ in range(int(input())):
        n, q = tup_in()
        A = arr_in()
        precalc_sparse_table(A)

        def bin_search_max():
            left, right = i - 1, n - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if query(i - 1, mid) > A[i - 1]:
                    right = mid
                else:
                    left = mid
            return right

        for qq in range(q):
            i, k = tup_in()
            if A[i - 1] == n:
                if i == 1:
                    print(k)
                else:
                    print(max(k - (i - 2), 0))
            else:
                if query(0, i - 1) > A[i - 1]:
                    print(0)
                else:
                    if A[i - 1] < A[not i - 1]:
                        print(0)
                    else:
                        right = bin_search_max()
                        if k <= i - 2:
                            print(0)
                        else:
                            a = min(k - (i - 2), right - (i - 1))
                            if i == 1:
                                print(a - 1)
                            else:
                                print(a)

if __name__ == "__main__":
    solution()
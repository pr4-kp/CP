import sys
input = sys.stdin.readline
inf = float('inf')
def arr_in():
	return list(map(int, input().split()))

def tup_in():
	return map(int, input().split())

"""
--- Notes ---

"""
# --- BEGIN SPARSE TABLE ---
"""
- O(nlog(n)) preprocessing time
- O(1) range min/max/etc. query
- Use when the value of two non-disjoint intervals is the same as the the value of the union of those intervals
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
    ST = [[0 for jj in rang e(n + 1 - (1 << ii))] for ii in range(size + 1)]
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
    n, q = tup_in()
    X = arr_in()
    precalc_sparse_table(X)

    for ii in range(q): 
       l, r = tup_in()
       print(query(l + 1, r + 1))

if __name__ == "__main__":
	solution()
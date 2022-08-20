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
- O(1) range min/max/gcd/lcm etc. query
- Use when the value of two intersecting intervals is the same as the the value of the union of those intervals
- Use when array is static
"""
class SparseTable:
    def __init__(self, A, n) -> None:
        size = n.bit_length() - 1
        self.table = [[0 for jj in range(n + 1 - (1 << ii))] for ii in range(size + 1)]
        self.table[0] = A
        for ii in range(1, size + 1):
            for jj in range(0, n + 1 - (1 << ii)):
                self.table[ii][jj] = min(
                    self.table[ii - 1][jj], self.table[ii - 1][jj + (1 << (ii - 1))])

    def query(self, l, r) -> int:
        log_range = (r - l + 1).bit_length() - 1
        return min(self.table[log_range][l], self.table[log_range][r - (1 << log_range) + 1])
# --- END SPARSE TABLE ---

def solution():
    n, q = tup_in()
    X = arr_in()
    SX = SparseTable(X, n)

    for ii in range(q): 
        l, r = tup_in()
        print(SX.query(l - 1, r - 1))

if __name__ == "__main__":
	solution()
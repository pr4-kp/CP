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

"""--- Notes ---
Big fail here, I needed to change the value of X[a], not even in the segment tree, just X itself
after the user decided to change it.
"""
# --- BEGIN FENWICK TREE ---
"""
- O(n) preprocessing time
- O(log(n)) range sum query
- O(log(n)) update value
- Use when range sum queries are being made and array is dynamic
"""
class FenwickTree:
    def __init__(self, arr, n) -> None:
        self.tree = [0] * (n + 1)
        self.size = n
        for ii in range(n):
            self.add_val(ii, arr[ii])
    
    def add_val(self, i, v):
        i += 1
        while i <= self.size:
            self.tree[i] += v
            i += i & (-i)
    
    def prefix_sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    
    def get_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
# --- END FENWICK TREE ---

def solution():
    n, q = tup_in()
    X = arr_in()
    FTX = FenwickTree(X, n)

    for _ in range(q):
        q_type, k, u = tup_in()
        if q_type == 1:
            FTX.add_val(k - 1, u - X[k - 1])
            X[k - 1] = u
        elif q_type == 2:
            print(FTX.get_sum(min(k,u)-1, max(k,u)-1))
            

if __name__ == "__main__":
    solution()
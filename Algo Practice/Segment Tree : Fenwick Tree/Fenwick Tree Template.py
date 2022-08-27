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
    A = [1,3,4,8,6,1,4,2]
    n = 8
    FTA = FenwickTree(A, n)
    


if __name__ == "__main__":
    solution()
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

# --- BEGIN SEGMENT TREE---
class SegmentTree:
    def __init__(self, arr, n) -> None:
        self.arr = arr
        self.tree = [0] * (4 * n)
        self.n = n

        for ii in range(n):
            self.tree[n + ii] = arr[ii]

        for ii in range(n - 1, 0, -1):
            self.tree[ii] = self.tree[ii << 1] + self.tree[ii << 1 | 1]
    
    def update(self, i, v):
        self.tree[i + self.n - 1] = v
        i += self.n - 1
        jj = i
        while jj > 1:
            self.tree[jj >> 1] = self.tree[jj] + self.tree[jj ^ 1]
            jj >>= 1
        
    def query(self, l, r):
        res = 0
        l += self.n - 1
        r += self.n

        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            
            l >>= 1
            r >>= 1
        return res


# --- END SEGMENT TREE ---


def solution():
    n, q = tup_in()
    X = arr_in()
    STX = SegmentTree(X, n)
    for _ in range(q):
        t, k, u = tup_in()
        if t == 1:
            STX.update(k, u)
        else:
            STX.query(k, u)



if __name__ == "__main__":
    solution()
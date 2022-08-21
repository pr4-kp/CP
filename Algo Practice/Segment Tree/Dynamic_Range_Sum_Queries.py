import sys
# # (optional) very fast input
#import io
#import os

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
def arr_in(): return list(map(int, input().split()))
def tup_in(): return map(int, input().split())

# --- BEGIN SEGMENT TREE---
class SegmentTree:
    def __init__(self, arr, n) -> None:
        self.arr = arr
        self.n = n
        self.tree = [0] * (2 * n)

        for ii in range(n):
            self.tree[n + ii] = arr[ii]
        for ii in reversed(range(n)):
            self.tree[ii] = self.tree[ii << 1] + self.tree[(ii << 1) | 1]

    def update(self, i, v) -> None:
        i += self.n
        self.tree[i] = v

        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def query(self, l, r) -> int:
        l += self.n
        r += self.n
        sum = 0
        while l < r:
            if l & 1:
                sum += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                sum += self.tree[r]  
            l >>= 1
            r >>= 1
        return sum
# --- END SEGMENT TREE ---

def solution():
    n, q = tup_in()
    X = arr_in()
    STX = SegmentTree(X, n)
    for _ in range(q):
        t, k, u = tup_in()
        if t == 1:
            STX.update(k - 1, u)
        else:
            print(STX.query(k - 1, u))


if __name__ == "__main__":
    solution()

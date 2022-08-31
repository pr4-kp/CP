import sys
from random import randint
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

class DSU:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]

    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return self.parent[node]
    
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if randint(0, 2) % 2:
            self.parent[rootB] = rootA
            if rootA != rootB:
                self.size[rootA] += self.size[rootB]
        else:
            self.parent[rootA] = rootB 
            if rootA != rootB:
                self.size[rootB] += self.size[rootA]

def solution():
    n, m = tup_in()
    d = DSU(n)
    ans = n
    last = 0
    for _ in range(m): 
        u, v = tup_in()
        if d.find(u) != d.find(v):
            ans -= 1
        d.union(u,v)
        last = max(last, d.size[d.find(u)], d.size[d.find(v)])

        print(ans, last)

if __name__ == "__main__":
    solution()
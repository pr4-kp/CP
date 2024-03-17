import heapq
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


# --- BEGIN MAX HEAP ---
"""
- Make sure to import heapq!
- Allows for the creation of max heaps using heapq
- Initializing is O(n) with heapify
- Push is O(log(n))
- Pop is O(log(n))
"""
class MaxHeapObj(object):
    def __init__(self, val): self.val = val
    def __lt__(self, other): return self.val > other.val
    def __eq__(self, other): return self.val == other.val
    def __str__(self): return str(self.val)

class MinHeap(object):
    def __init__(self, l):
        heapq.heapify(l)
        self.h = l
    def heappush(self, x): heapq.heappush(self.h, x)
    def heappop(self): return heapq.heappop(self.h)
    def __getitem__(self, i): return self.h[i]
    def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
    def __init__(self, l):
        l = list(map(lambda x: MaxHeapObj(x), l))
        heapq.heapify(l)
        self.h = l
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
    def heappop(self): return heapq.heappop(self.h).val
    def __getitem__(self, i): return self.h[i].val

# --- END MAX HEAP ---


def solution():
    for _ in range(int(input())):
        n = int(input())
        a = arr_in()
        b = arr_in()
        # print(a, b)
        ha = MaxHeap(a)
        hb = MaxHeap(b)

        ans = 0

        while ha and hb:
            biga = ha[0]
            bigb = hb[0]
            if biga == bigb:
                ha.heappop()
                hb.heappop()
            elif biga > bigb:
                ans += 1
                add = len(str(ha.heappop()))
                ha.heappush(add)
            else:
                ans += 1
                add = len(str(hb.heappop()))
                hb.heappush(add)
        
        print(ans)


        

if __name__ == "__main__":
    solution()
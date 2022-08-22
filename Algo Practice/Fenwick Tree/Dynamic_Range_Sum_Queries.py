import sys
input = sys.stdin.readline
inf = float('inf')

# --- BEGIN FENWICK TREE ---
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
    n, q = map(int, input().split())
    array = list(map(int, input().split()))
    array_fenwick_tree = FenwickTree(array, n)

    for _ in range(q):
        q_type, k, u = map(int, input().split())
        if q_type == 1:
            array_fenwick_tree.add_val(k - 1, u - array[k - 1])
            array[k - 1] = u  # Make sure to update value after changing!
        elif q_type == 2:
            print(array_fenwick_tree.get_sum(min(k, u)-1, max(k, u)-1))
            

if __name__ == "__main__":
    solution()
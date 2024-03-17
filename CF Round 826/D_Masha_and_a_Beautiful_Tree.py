import sys
from io import BytesIO, IOBase
import os


# sys.setrecursionlimit(10 ** 6)
# Fast IO Region
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")
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
# class SparseTable:
#     def __init__(self, A, n) -> None:
#         size = n.bit_length() - 1
#         self.table = [[0 for jj in range(n + 1 - (1 << ii))] for ii in range(size + 1)]
#         self.table[0] = A
#         for ii in range(1, size + 1):
#             for jj in range(0, n + 1 - (1 << ii)):
#                 self.table[ii][jj] = min(
#                     self.table[ii - 1][jj], self.table[ii - 1][jj + (1 << (ii - 1))])

#     def query(self, l, r) -> int:
#         log_range = (r - l + 1).bit_length() - 1
#         return min(self.table[log_range][l], self.table[log_range][r - (1 << log_range) + 1])
# --- END SPARSE TABLE ---

def solution():
    n = int(input())
    tree = arr_in()
    if n == 1:
        return 0
    tree = [a - 1 for a in tree]
    tree = [tree[i] ^ i for i in range(n)]
    tot = 0
    # for ii in reversed(range(n)):
    #     ans += sum(list(map(lambda x: x & (1 << ii), tree))) // (1 << ii) // (1 << ii)

    n = n.bit_length() - 1

    for i in range(1,n):
        for j in range(1 << i):
            for k in range(1 << (n-i)):
                if tree[j * (1 << (n-i))] & (1 << i) != tree[j * (1 << (n-i)) + k] & (1 << i):
                    return -1

    # for i in range(1,n):
    #     for j in range(1 << i):
    #         ans = False
    #         for k in range(1 << (n-i)):
    #             if tree[j * (1 << (n-i)) + k] & (1 << i):
    #                 ans = True
    #         if ans:
    #             tot += 1
    for ii in range(1 << n):
        print(bin(tree[ii]).count("1"))
    return tot

if __name__ == "__main__":
    for _ in range(int(input())):
        print(solution())
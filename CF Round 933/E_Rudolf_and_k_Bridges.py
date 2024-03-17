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
use dp:
if d = 2, |4 - 1| - 1 = 2 is allowed
so d is space between i and j
[ - - - - - - (-) ]
"""

def solution():
    n, m, k, d = tup_in()

    min_cost = [0] * n

    for i in range(n):
        a = arr_in()
        dp = [1] * m 

        for j in range(1, m):
            best = int(2e6)
            for l in range(1, d + 2):
                if j - l >= 0:
                    best = min(best, dp[j-l])
            dp[j] = best + a[j] + 1

        min_cost[i] = dp[-1]

    sol: int = sum(min_cost[:k])
    v: int = sum(min_cost[:k])
    for j in range(n - k):
        v = v - min_cost[j] + min_cost[j + k]
        sol = min(sol, v)

    print(sol)

if __name__ == "__main__":
    for _ in range(int(input())):
        solution()
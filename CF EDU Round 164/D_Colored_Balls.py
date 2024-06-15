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


MOD = 998244353

"""
--- Notes ---
v(–) is ceil(S/2), unless there is a color with more than S/2 balls, then it is the value of that color
"""

def solution():
    n = int(input())
    a = arr_in()
    s = sum(a)
    out = 0
    over = 0

    dp = [[0] * (s+1) for _ in range(n)]

    dp[0][0] = 1 
    dp[0][a[0]] = 1
    
    for i in range(1, n):
        for j in range(s+1):
            # either you don't add the ith color and nothing is added 
            dp[i][j] = dp[i-1][j]
            # or you add the ith color
            if (j-a[i] >= 0): dp[i][j] += dp[i-1][j-a[i]] % MOD
    
    for j in range(1,s+1):
        out += dp[-1][j] * -(-j//2) % MOD

    # handling undercounting: if a[i] is bigger than half the sum – this is the same as checking all subsets 
    # of size j such that j < a[i] and then adding a[i]
    # rather nice way to do this; not sure I could figure out this step even if I figured out the knapsack part
    for i in range(n):
        for j in range(a[i]):
            over -= dp[-1][j] * -((-(a[i] + j)) // 2) % MOD 
            over += dp[-1][j] * a[i] % MOD

    print((out + over) % MOD)

if __name__ == "__main__":
    solution()
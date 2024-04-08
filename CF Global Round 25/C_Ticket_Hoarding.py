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

def solution():
    for _ in range(int(input())):
        n, m, k = tup_in()
        ogk = k
        a = arr_in()
        out = 0

        a.sort()
        # print(a)

        for j in range(n):
            if k == 0:
                break
            elif k >= m:
                out += (a[j] + (ogk - k)) * m 
                k -= m
            else:
                out += (a[j] + (ogk - k)) * k
                k -= k

        print(out)

        # dp = [[inf] * (k + 1) for __ in range(2)]

        # for j in range(min(m + 1, k)):
        #     dp[0][j] = a[0] * j

        # for j in range(1, n):
        #     for l in range(0, k + 1):
        #         for i in range(max(0, l - min(m,n)), l + 1): # assume ive already bought i tickets
        #             dp[1][l] = min(dp[1][l], dp[0][i] + (l - i) * (i + a[j]))

        #     for j in range(k+1):
        #         dp[0][j] = dp[1][j]
        #         dp[1][j] = inf

        #     print(dp)

        # print(dp[0][-1])

if __name__ == "__main__":
    solution()
import sys
from io import BytesIO, IOBase
import os
from itertools import accumulate


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
    n,m = tup_in()
    a=arr_in()
    b=arr_in()
    c=arr_in()
    exp=0
    dp = [-1] * 1000001

    diffs = [(a[i], a[i]-b[i]) for i in range(n)]
    diffs.sort(key=lambda a: a[0])
    print(diffs)
    d2 = list(accumulate(diffs, lambda a,b: (b[0],min(a[1], b[1]))))
    print(d2)

    mindiff = min(diffs, key=lambda a: a[1])

    for i in range(m):
        if (c[i] > 1000000):
            v = ((c[i] - 1000000 + mindiff - 1) // mindiff)
            c[i] -= v * mindiff
            exp += v * 2

    print(c, exp)

if __name__ == "__main__":
    solution()
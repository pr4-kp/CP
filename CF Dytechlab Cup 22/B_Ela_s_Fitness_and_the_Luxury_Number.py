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
100000000000000000
1000000000000000000
between 
i^2, i \in Z
i^2 + 2i + 1 

(2i + 1) // i = 2 16 -> 20 -> 24
"""

def to_n(n):
    if n == 0:
        return 0
    res = 3 * int(n ** 0.5)
    m = int(n ** 0.5)
    if n < m * m + 2 * m:
        res -= 1
    if n < m * m + m:
        res -= 1
    return res


def solution():
    for _ in range(int(input())):
        l, r = tup_in()
        # n = int(r ** 0.5)
        # cn = n * 3 
        # m = int(l ** 0.5)
        # cm = m * 3 

        # if l == m ** 2 + 2 * m:
        #     cm += 2
        # elif l >= m ** 2 + m:
        #     cm += 1

        # if l == m ** 2 or l == m ** 2 + m or l == m ** 2 + 2 * m:
        #     cm -= 1
        print(to_n(r) - to_n(l - 1))

        # if r == n ** 2 + 2 * n:
        #     cn += 2
        # elif r >= n ** 2 + n:
        #     cn += 1
    
        # print(cn - cm)
            

if __name__ == "__main__":
    solution()
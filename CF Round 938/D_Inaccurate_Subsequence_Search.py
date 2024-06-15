import sys
from io import BytesIO, IOBase
import os
from collections import Counter


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
    
    n, m, k = tup_in()
    a = arr_in()
    b = arr_in()
    out = 0

    if m == 1:
        return a.count(b[0])

    c = (Counter(a[:m]))
    bb = Counter(b)

    tot = sum((c & bb).values())

    if tot >= k:
        out += 1
    
    for j in range(1, n - m + 1):

    #     # remove a[j-1], add a[j + m - 1]
        if a[j-1] in c:
            if a[j-1] in bb:
                if bb[a[j-1]] >= c[a[j-1]]:
                    tot -= 1

            c[a[j-1]] -= 1
            if c[a[j-1]] == 0:
                c.pop(a[j-1])

        if a[j+m-1] in c:
            if a[j+m-1] in bb:
                if bb[a[j+m-1]] > c[a[j+m-1]]:
                    tot += 1
            c[a[j+m-1]] += 1
        else:
            if a[j+m-1] in bb:
                if bb[a[j+m-1]] > c[a[j+m-1]]:
                    tot += 1
            c[a[j+m-1]] = 1
        # print(c)
        # print("\t", tot)

    #     # print(c & Counter(b))
    #     # print(sum((c & Counter(b)).values()))
        
        if tot >= k:
            out += 1
    #     # pass
    return out



if __name__ == "__main__":
    for _ in range(int(input())):
        print(solution())
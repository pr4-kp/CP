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
    n,m=tup_in()
    a=[]
    b=[]
    for __ in range(n):
        a.append(arr_in())
    for __ in range(n):
        b.append(arr_in())

    loc1a = 0
    loc1b = 0
    for j in range(n):
        if 1 in a[j]: loc1a=j
        if 1 in b[j]: loc1b=j

    # move the 1 to the top 
    tmp = a[0]
    a[0] = a[loc1a]
    a[loc1a] = tmp 

    tmp = b[0]
    b[0] = b[loc1b]
    b[loc1b] = tmp

    if set(a[0]) != set(b[0]):
        return "NO"

    # permute the top row 
    d1=dict()
    d2=dict()
    perm=dict()
    for i, e in enumerate(a[0]):
        d1[e]=i
    for i, e in enumerate(b[0]):
        d2[e]=i

    for e in a[0]:
        perm[d1[e]] = d2[e]

    # print(perm)

    aa = [] 
    for r in a:
        ar = [0] * m
        for j in range(m):
            ar[perm[j]] = r[j]
        aa.append(ar)

    # print(aa)

    for i in range(n):
        aa[i] = tuple(aa[i])
        b[i] = tuple(b[i])

    # print(aa, b)
    if set(aa) == set(b):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    for _ in range(int(input())):
        print(solution())
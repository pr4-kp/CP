import sys
from io import BytesIO, IOBase
import os
from math import gcd


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
O(n) to check for any entry
try to find O(1) many things to test removing 
"""

def test_remove(a, j):
    aa = a.copy()
    n = len(aa)
    aa.pop(j)
    b=[]

    for i in range(n-2):
        b.append(gcd(aa[i], aa[i+1]))
    
    for i in range(n-3):
        if b[i] > b[i + 1]:
            return False
    return True

def solution():
    
    n=int(input())
    a=arr_in()
    bb=[]

    if n == 3:
        return "YES"

    for i in range(n-1):
        bb.append(gcd(a[i], a[i+1]))
    # for j in range(n):
    #     print(j, test_remove(a, j))

    bad = 0
    for j in range(n-2):
        if bb[j + 1] < bb[j]:
            bad = j

    if (test_remove(a,bad)):
        return "YES"
    elif bad+1<=n-1 and test_remove(a,bad+1):
        return "YES"
    elif bad+2 <= n-1 and test_remove(a, bad+2):
        return "YES"
    else:
        return "NO"

    

        

if __name__ == "__main__":
    for _ in range(int(input())):
        print(solution())
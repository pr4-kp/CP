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
        n = int(input())
        r = [input(), input()]

        possible = [[False] * n for _j in range(2)]
        
        possible[0][0] = True

        for j in range(n // 2):
            # on top row: check if up move gets you there from bottom or right move from previous top
            if (2 * j - 1) >= 0 and possible[1][2 * j - 1] and r[0][2 * j - 1] == ">":
                possible[0][2 * j] = True
            if (2 * j - 2) >= 0 and possible[0][2 * j - 2] and r[0][2 * j - 1] == ">":
                possible[0][2 * j] = True

            # on bottom row: check if down move gets you there from previous top or right move from previous bottom
            if possible[0][2 * j] and r[1][2 * j] == ">":
                possible[1][2 * j + 1] = True 
            if (2 * j - 1) >= 0 and possible[1][2 * j - 1] and r[1][2 * j] == ">":
                possible[1][2 * j + 1] = True


        # [print(r) for r in possible] 
        if possible[1][n-1]:
            print("YES")
        else:
            print("NO")



if __name__ == "__main__":
    solution()
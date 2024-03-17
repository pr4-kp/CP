import sys
from io import BytesIO, IOBase
import os
from collections import Counter
from string import ascii_lowercase


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
        n, k = tup_in()
        c = Counter(list(input()))
        lex = ""
        # print(c)

        size_per_set = n // k
        amt_left = n // k

        for i in range(k):
            amt_left = n // k
            for ch in ascii_lowercase:
                if amt_left == 0:
                    lex += ch
                    break
                if c[ch] > 0:
                    c[ch] -= 1
                    amt_left -= 1
                else:
                    lex += ch
                    break
            if amt_left > 0:
                for ch in ascii_lowercase:
                    if amt_left == 0:
                        break
                    while c[ch] > k - i - 1:
                        if amt_left == 0:
                            break
                        c[ch] -= 1
                        amt_left -= 1
                for ch in reversed(ascii_lowercase):
                    if amt_left == 0:
                        break 
                    while c[ch]:
                        if amt_left == 0:
                            break
                        c[ch] -= 1
                        amt_left -= 1
                
        print(lex)

if __name__ == "__main__":
    solution()
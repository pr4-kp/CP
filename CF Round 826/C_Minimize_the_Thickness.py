import sys
from io import BytesIO, IOBase
import os
MAX = 4000


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
    def psum(l, n):
        p = [0]
        for i in range(n):
            p.append(p[-1])
            p[-1] += l[i]
        return p

    for _ in range(int(input())):
        n = int(input())
        a = arr_in()

        def possible(k):
            desired_sum = 0
            lens = []
            curl = 0
            for ele in a:
                desired_sum += ele 
                if desired_sum < k:
                    curl += 1
                elif desired_sum == k:
                    desired_sum = 0
                    curl += 1
                    lens.append(curl)
                    curl = 0
                else: #desired_sum > k
                    return MAX
            if desired_sum != 0:
                return MAX
            else:
                return max(lens)

        pa = psum(a, n)
        ans = []
        # print(pa)
        for sums in pa[1:]:
            ans.append(possible(sums))
        
        print(min(ans))

if __name__ == "__main__":
    solution()
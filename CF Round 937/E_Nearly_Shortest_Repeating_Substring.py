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
    n = int(input())
    s = input()

    for j in range(1, n // 2 + 1):
        if n % j == 0:
            differences = 0
            # numsets = n // j
            # rangesets = [set() for __ in range(j)]

            # for k in range(n):
            #     rangesets[k % j].add(s[k])
            # print(rangesets)

            # tot = 0
            # for t in rangesets:
            #     tot += len(t)
            # if tot <= j + 1:
            #     return j

            cuts = dict()

            for k in range(0, n // j):
                if s[k * j : (k+1) * j] not in cuts:
                    cuts[s[k * j: (k+1) * j]] = 1
                else:
                    cuts[s[k * j: (k+1) * j]] += 1
                # cuts.add(s[k * j : (k+1) * j])
                # for l in range(j):
                #     if (s[l] != s[k * j + l]):
                #         differences += 1
                        # print("\t", l, k * j + l, "different!")
            # print(cuts)
            # print(cuts)
            if len(cuts) == 2 and 1 in cuts.values():
                differences = 0
                cuts = list(cuts)
                s1 = cuts[0]
                s2 = cuts[1]

                for l in range(j):
                    if s1[l] != s2[l]:
                        # print("\t", s1[l], s2[l])
                        differences += 1

                if differences <= 1:
                    return j
            elif len(cuts) == 1:
                return j


            # if differences <= 1:
            #     return j
            
    return n


if __name__ == "__main__":
    for _ in range(int(input())):
        print(solution())
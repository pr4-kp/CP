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


class DisjointSets:
	def __init__(self, size: int) -> None:
		self.parents = [i for i in range(size)]
		self.sizes = [1 for _ in range(size)]

	def find(self, x: int) -> int:
		""":return: the "representative" node in x's component"""
		if self.parents[x] == x:
			return x
		self.parents[x] = self.find(self.parents[x])
		return self.parents[x]

	def unite(self, x: int, y: int) -> bool:
		""":return: whether the merge changed connectivity"""
		x_root = self.find(x)
		y_root = self.find(y)
		if x_root == y_root:
			return False

		if self.sizes[x_root] < self.sizes[y_root]:
			x_root, y_root = y_root, x_root

		self.parents[y_root] = x_root
		self.sizes[x_root] += self.sizes[y_root]
		return True

	def connected(self, x: int, y: int) -> bool:
		""":return: whether x and y are in the same connected component"""
		return self.find(x) == self.find(y)


def sieve(n):
    prime_factors = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        if not prime_factors[i]: # i.e. if i is prime
            k = 1
            while (i * k < n + 1):
                prime_factors[i * k].append(i)
                k += 1
    return prime_factors

pf = sieve(int(1e6) + 5)

def solution():
    n,k = tup_in()
    a = arr_in()

    s = [0] * (2 * n - 1)

    for i in range(n-1):
        s[i] = a[i+1]
    for i in range(n):
        s[i + n - 1] = a[i]

    dsu = DisjointSets(2 * n - 1)

    lp = dict()

    for i in range(2 * n - 1):
        for f in pf[s[i]]:
            if f in lp and (i-lp[f]) <= k: 
                dsu.unite(lp[f], i)
            lp[f] = i

    ans = len(set(dsu.parents))
    for i in range(n):
         if a[i] == 1:
            if i == 0:
                ans += n - 1
            else:
                ans += n - 2

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solution()
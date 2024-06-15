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
MOD = 10 ** 9 + 7
MAXN = 3*10**3
fac = [0] * (MAXN + 1)
inv = [0] * (MAXN + 1)
def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

"""
--- Notes ---

"""

def factorial(p: int):
    """Precomputes n! from 0 to MAXN."""
    global fac
    fac[0] = 1
    for i in range(1, MAXN + 1):
        fac[i] = (fac[i - 1] * i) % p


def inverses(p: int):
	"""
	Precomputes all modular inverse factorials from 0 to MAXN in O(n + log p) time
	"""
	global inv
	inv[MAXN] = pow(fac[MAXN], p - 2, p)
	for i in range(MAXN, 0, -1):
		inv[i - 1] = (inv[i] * i) % p


def binom(n: int, r: int):
    """Computes nCr mod p"""
    if r > n or r < 0:
        return 0
    return fac[n] * inv[r] % MOD * inv[n - r] % MOD


def solution():
    n,c,k=tup_in()
    out = 0
    fp=[-1]*n

    factorial(MOD)
    inverses(MOD)

    def fixedpt(g):
        if fp[g%n] != -1:
            return fp[g%n]

        if c >= g:
            if c + k == n:
                fp[g%n]=1
                return 1
            else:
                fp[g%n]=0
                return 0
        
        Xg = 0
        max_ones_representative = int((c + k) * g / n)
        a=0
        for j in range(max_ones_representative + 1):
            a += binom(g, j)

        dp = [[0] * g for _ in range(g)]
        dp[0][0] = 1

        for z in range(1,g):
            for l in range(g):
                dp[z][l+i+1]
        
        fp[g%n]=Xg
        return Xg

    for i in range(n):
        out += fixedpt(gcd(n,i)) % MOD
    
    print(out % MOD)


if __name__ == "__main__":
    solution()
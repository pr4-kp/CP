import sys
from io import BytesIO, IOBase
import os
from itertools import accumulate

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

# factorial precomputation 

MAXN = 10**6
MOD = 998244353

fac = [0] * (MAXN + 1)
inv = [0] * (MAXN + 1)


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
    ans = []

    n, q = tup_in()
    gps = list(accumulate(arr_in(), initial = 0))
    sps = list(accumulate(arr_in(), initial=0))

    tg = gps[n] 
    ts = sps[n] 

    factorial(MOD)
    inverses(MOD)

    # precompute the sum 
    binoms = []
    for j in range(0, ts + 1):
        binoms.append(binom(ts, j) % MOD)
    
    binomspsum = list(accumulate(binoms, lambda x, y: x + y % MOD, initial=0))

    for _ in range(q):
        l, r = tup_in()
        
        g = gps[r] - gps[l-1]
        s = sps[r] - sps[l-1]

        if (ts - s + tg - 2 * g >= 0 and ts - s + tg - 2 * g < ts + 1):
            out = binomspsum[ts + 1] - binomspsum[ts - s + tg - 2 * g + 1] % MOD
        elif (ts - s + tg - 2 * g < 0):
            out = pow(2, ts, MOD)    # probability 1
        else:
            out = 0                  # probability 0
                
        out = out * pow(inv[2], ts, MOD) % MOD

        ans.append(out)

    print(*ans)


if __name__ == "__main__":
    solution()
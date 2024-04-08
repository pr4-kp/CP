import sys
from io import BytesIO, IOBase
import os


# sys.setrecursionlimit(10 ** 6)
# Fast IO Region
BUFSIZE = 8192

MAXN = int(2e5)
MOD = 998244353

fac = [0] * (MAXN + 1)
inv = [0] * (MAXN + 1)

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


"""
--- Notes ---
if p[-1] == s[0], then the value at p[-1] should be n
if p[-1] < s[0], then between these indices must be the values 
    min(p[-1] + 1, s[0] + 1) ... n
    pf: if not there, then outside, which makes p[-1], s[0] not a prefix/suffix max

"""

def solution():
    n, pm, sm = tup_in()
    p = arr_in()
    s = arr_in()

    if p[-1] != s[0] or p[0] != 1 or s[-1] != n:
        return 0
    
    factorial(MOD)
    inverses(MOD)

    ans = binom(n - 1, s[0] - 1)

    for i in range(pm - 1, 0, -1):
        gap = p[i] - p[i - 1] - 1
        ans *= binom(p[i] - 2, gap) * fac[gap] % MOD
        ans %= MOD

    for j in range(1, sm):
        gap = s[j] - s[j - 1] - 1
        ans *= binom(s[j] - 2, gap) * fac[gap] % MOD
        ans %= MOD

    return ans % MOD

    
    

if __name__ == "__main__":
    for _ in range(int(input())):
        print(solution())
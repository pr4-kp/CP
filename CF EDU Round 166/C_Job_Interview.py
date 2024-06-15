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
for each entry there is an ideal choice 

e.g. last one it is [1 1 1 1 1]

the sum of the choice array should equal m (after removing the one at i)
if the sum is: 
    1. greater than m: then flip 1 to 0 (right to left) until the sum is only 1 greater than m
    2. less than m: swap the arrays and swap m and n and then we are in case (1)
    3. equal to m: find the last 0 and swap it. It is now in case 1
store that last thing we didn't flip. we can freely flip that bit 

so we've handled all cases except not choosing that "swap" bit 
we can do that case manually lol
"""

def solution():
    for _ in range(int(input())):
        n, m = tup_in()
        a = arr_in()
        b = arr_in()

        out = [0] * (n + m + 1)

        if sum([0 if a[i] > b[i] else 1 for i in range(n + m + 1)]) < m:
            tmp = n
            n = m
            m = tmp 

            tmp = a.copy()
            a = b.copy()
            b = tmp

        choice = [0 if a[i] > b[i] else 1 for i in range(n + m + 1)]
        # print(choice)

        # case for sum choice > m
        swap = 0
        s = sum(choice)
        for i in range((n + m + 1)-1, -1, -1):
            if s == m + 1 and choice[i] == 1:
                swap = i
                break 
            if s == m and choice[i] == 0:
                choice[i] = 1 
                swap = i
                break 
            if s > m + 1 and choice[i] == 1:
                choice[i] = 0
                s -= 1
        # print(choice, m, swap, sep='\n')

        # chooses based on the choice array 
        tot = sum([a[i] if choice[i] == 0 else b[i] for i in range(n + m + 1)])
        for i in range(n + m + 1):
            if i > 0:
                if choice[i - 1] == 0:
                    tot += a[i - 1]
                else:
                    tot += b[i - 1]

            if choice[i] == 0:
                tot -= a[i]
            else:
                tot -= b[i]

            if i != swap:
                # take the swap as 1 
                if choice[i] == 1:
                    out[i] = tot
                # take the swap as 0 
                elif choice[i] == 0:
                    out[i] = tot - b[swap] + a[swap]
            else:
                tn = n 
                tm = m
                for j in range(n + m + 1):
                    if j != i:
                        if a[j] > b[j] and tn > 0:
                            tn -= 1
                            out[i] += a[j]
                        elif b[j] > a[j] and tm > 0:
                            tm -= 1
                            out[i] += b[j]
                        elif tn <= 0:
                            out[i] += b[j]
                        elif tm <= 0:
                            out[i] += a[j]

        print(*out)
        



if __name__ == "__main__":
    solution()
import sys
from io import BytesIO, IOBase
import os
import heapq
from queue import PriorityQueue


# class pq(PriorityQueue):
#     def _put(self, item):
#         return super()._put((self._get_priority(item), item))

#     def _get(self):
#         return super()._get()[1]

#     def _get_priority(self, item):
#         return item[0]


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
    n, k = tup_in()
    a = arr_in()

    if n == 1:
        return a[0]
    
    if k < n - 1:
        for j in range(n):
            print([s - a[j] for s in a])
        # diff = PriorityQueue()
        
        # for i in range(n - 1):
        #     diff.put((-abs(a[i + 1] - a[i]), i, a[i], a[i + 1]))
        
        # while (k > 0):
        #     best = diff.get()
        #     ind = best[1]

        #     if (best[2] != a[ind] or best[3] != a[ind + 1]):
        #         continue

        #     # change the array 
        #     if (best[2] > best[3]):
        #         a[ind] = best[3]
        #     else:
        #         a[ind + 1] = best[2]

        #     print("\t", best, a)

        #     if (ind > 0): 
        #         diff.put((-abs(a[ind] - a[ind - 1]),
        #                  ind - 1, a[ind - 1], a[ind]))
        #     if (ind < n - 2):
        #         diff.put((-abs(a[ind + 2] - a[ind + 1]),
        #                  ind + 1, a[ind + 1], a[ind + 2]))
                
        #     k -= 1
                
        return sum(a)
    else:
        return min(a) * n
        

if __name__ == "__main__":
    for _ in range(int(input())):
        print(solution())

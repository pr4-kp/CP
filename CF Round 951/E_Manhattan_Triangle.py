import sys
from io import BytesIO, IOBase
import os
from collections import namedtuple


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

Point = namedtuple('Point', ['x', 'y'])


def isBetween(a, b, c):
    crossproduct = (c.y - a.y) * (b.x - a.x) - (c.x - a.x) * (b.y - a.y)

    if abs(crossproduct) != 0:
        return False

    dotproduct = (c.x - a.x) * (b.x - a.x) + (c.y - a.y)*(b.y - a.y)
    if dotproduct < 0:
        return False

    squaredlengthba = (b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y)
    if dotproduct > squaredlengthba:
        return False

    return True


def lb(arr, x):
    start = 0
    end = len(arr)-1

    while start != end:
        mid = (start+end)//2
        if arr[mid][0] < x:
            start = mid + 1
        else:
            end = mid

    return arr[end]

def solution():
    n,d=tup_in()
    pts = dict()
    xpy = dict()
    xmy = dict()
    for i in range(n):
        x, y = tup_in()
        pts[Point(x,y)]=i+1
        if (x-y not in xmy): 
            xmy[x-y] = []
        xmy[x-y].append((x+y, Point(x,y)))

        if (x+y not in xpy): 
            xpy[x+y] = []
        xpy[x+y].append((x-y, Point(x, y)))

    for e in xpy: 
        xpy[e].sort(key=lambda x: x[0])
    for e in xmy:
        xmy[e].sort(key=lambda x: x[0])

    for p in pts:

        if (Point(p.x + d//2, p.y + d//2) in pts):
            if (p.x - p.y - d in xmy):
                p3 = lb(xmy[p.x - p.y - d], p.x + p.y)
                # if (p3[0] <= p.x + p.y + d and p3[0] >= p.x + p.y):
                if isBetween(Point(p.x - d//2, p.y + d//2), Point(p.x, p.y + d), p3[1]):
                    print(pts[p], pts[Point(p.x + d//2, p.y + d//2)], pts[p3[1]])
                    return
            if (p.x - p.y + d in xmy):
                p3 = lb(xmy[p.x - p.y + d], p.x + p.y)
                # if (p3[0] <= p.x + p.y + d and p3[0] >= p.x + p.y):
                if isBetween(Point(p.x + d//2, p.y - d//2), Point(p.x + d, p.y), p3[1]):
                    print(pts[p], pts[Point(p.x + d//2, p.y + d//2)], pts[p3[1]])
                    return
        
            # for p3 in pts:
            #     if isBetween(Point(p.x - d//2, p.y + d//2), Point(p.x, p.y + d), p3):
            #         print(pts[p], pts[Point(p.x + d//2, p.y + d//2)], pts[p3])
            #         return 
            #     if isBetween(Point(p.x + d//2, p.y - d//2), Point(p.x + d, p.y), p3):
            #         print(pts[p], pts[Point(p.x + d//2, p.y + d//2)], pts[p3])
            #         return
                
        if (Point(p.x - d//2, p.y + d//2) in pts):
            if (p.x + p.y + d in xpy): 
                p3 = lb(xpy[p.x + p.y + d], p.x - p.y - d)
                # if (p3[0] <= p.x - p.y and p3[0] >= p.x + p.y - d):x
                if isBetween(Point(p.x, p.y + d), Point(p.x + d//2, p.y + d//2), p3[1]):
                    print(pts[p], pts[Point(p.x - d//2, p.y + d//2)], pts[p3[1]])
                    return
            if (p.x + p.y - d in xpy):
                p3 = lb(xpy[p.x + p.y - d], p.x - p.y - d)
                # if (p3[0] <= p.x - p.y and p3[0] >= p.x + p.y - d):
                if isBetween(Point(p.x - d, p.y), Point(p.x - d//2, p.y - d//2), p3[1]):
                    print(pts[p], pts[Point(p.x - d//2, p.y + d//2)], pts[p3[1]])
                    return


        #     for p3 in pts:
        #         if isBetween(Point(p.x - d, p.y), Point(p.x - d//2, p.y - d//2), p3):
        #             print(pts[p], pts[Point(p.x - d//2, p.y + d//2)], pts[p3])
        #             return
        #         if isBetween(Point(p.x, p.y + d), Point(p.x + d//2, p.y + d//2), p3):
        #             print(pts[p], pts[Point(p.x - d//2, p.y + d//2)], pts[p3])
        #             return

    print(0,0,0)
    return
    

if __name__ == "__main__":
    for _ in range(int(input())):
        solution()
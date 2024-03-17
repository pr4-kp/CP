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
    # def calc(a):
    #     res = 0
    #     for ii in range(n):
    #         res += abs(pos[ii] - a) + dress[ii]
    #     return res

    # for _ in range(int(input())):
    #     n = int(input())
    #     pos = arr_in()
    #     dress = arr_in()

    #     left = 0
    #     right = int(1e8)
    #     tester = min(calc(left), calc(right))

    #     while left + 1 < right:
    #         mid = (left + right) / 2
    #         t = calc(mid)
    #         if t < tester and:

    # 1 August 2022
    # https://codeforces.com/contest/782/problem/B

    # sys.stdin = open('input.txt', 'r')
    for _ in range(int(input())):

        n = int(input())
        cor = arr_in()
        dress = arr_in()

        def all_friends_converge(minutes) -> bool:

            overlap_lower, overlap_upper = 0, 10 ** 9
            for i in range(n):
                lower_bound = cor[i] - (minutes - dress[i])
                upper_bound = cor[i] + (minutes - dress[i])
                if lower_bound > overlap_upper or upper_bound < overlap_lower:
                    return False
                if lower_bound > overlap_lower:
                    overlap_lower = lower_bound
                if upper_bound < overlap_upper:
                    overlap_upper = upper_bound
            return True

        def all_friends_converge2(minutes):
            overlap_lower, overlap_upper = 0, 10 ** 9
            for i in range(n):
                lower_bound = cor[i] - (minutes - dress[i])
                upper_bound = cor[i] + (minutes - dress[i])
                # if lower_bound > overlap_upper or upper_bound < overlap_lower:
                #     return False
                if lower_bound > overlap_lower:
                    overlap_lower = lower_bound
                if upper_bound < overlap_upper:
                    overlap_upper = upper_bound
            return (overlap_upper + overlap_lower) / 2
            
        left, right = 0, 10 ** 9
        diff = 10 ** (-6)

        while all_friends_converge2(left) + diff < all_friends_converge2(right):
            mid = (left + right) / 2
            if last_comparison := all_friends_converge(mid):
                right = mid
            else:
                left = mid + diff

        # make it more accurate
        print(all_friends_converge2((left + mid) / 2)
            if last_comparison else all_friends_converge2((mid + right) / 2))


if __name__ == "__main__":
    solution()

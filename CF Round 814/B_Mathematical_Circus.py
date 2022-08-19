import sys
#import io
#import os

# # very fast input
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
inf = float('inf')
def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

"""
--- Notes ---
1. a + k | 4 => a % 4 = -k % 4
2. a + k | 2 => a % 2 = -k % 2 (parity match) and b | 2
3. b | 4
"""

def solution():
    for _ in range(int(input())):
        n, k = tup_in()
        A = list(range(1 + (k % 4), n + 1 + (k % 4)))

        if k % 4 == 0:
            print("NO")
        if k % 2 == 1:
            print("YES")
            for ii in range(n // 2):
                print(2 * ii + 1, 2 * ii + 2)
        else:
            aSet, bSet = set(), set()
            tot = set(range(1, n+1))
            for ii in range(1, n + 1):
                if ii % 4 == 0:
                    bSet.add(ii)
                    tot.remove(ii)
                elif A[ii - 1] % 4 == 0:
                    aSet.add(ii)
                    tot.remove(ii)
            tot = list(tot)
            print("YES")
            for aa in aSet:
                print(aa, tot.pop())
            for bb in bSet:
                print(tot.pop(), bb)
                


if __name__ == "__main__":
    solution()
import sys
# # (optional) very fast input
#import io
#import os

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
inf = float('inf')
def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

"""
--- Notes ---

"""

def solution():
    for _ in range(int(input())):
        n = int(input())
        line = input().split()[0]
        vals = 0
        ans = []
        for ind, char in enumerate(line):
            if char == 'L':
                vals += ind
            else:
                vals += n - 1 - ind

        for ii in range(n // 2):
            if line[ii] == 'L':
                vals += n - 2 * ii - 1
                ans.append(vals)
            if line[-1 - ii] == 'R':
                vals += n - 2 * ii - 1
                ans.append(vals)

        while len(ans) != n:
            ans.append(vals)
        
        print(*ans)

if __name__ == "__main__":
    solution()
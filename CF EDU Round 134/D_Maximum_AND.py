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
        max = 0
        n = int(input())
        a = arr_in()
        b = arr_in()

        for i in reversed(range(31)):
            ans = 0
            max += 1 << i 
            for ae, be in zip(a, b):
                if (ae & max) == max:
                    ans += 1
                if (be & max) == max:
                    ans += 1
            if ans != n:
                max -= 1 << i
        
        print(max)

if __name__ == "__main__":
    solution()
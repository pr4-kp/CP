import sys
from collections import defaultdict
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
        a = input().split()
        b = input().split()
        c = input().split()
        ascore = bscore = cscore = 0


        d = defaultdict(lambda: 0)

        for aword, bword, cword in zip(a, b, c):
            d[aword] += 1
            d[bword] += 1
            d[cword] += 1
        
        for aword, bword, cword in zip(a, b, c):
            if d[aword] == 1:
                ascore += 3
            elif d[aword] == 2:
                ascore += 1
                
            if d[bword] == 1:
                bscore += 3
            elif d[bword] == 2:
                bscore += 1

            if d[cword] == 1:
                cscore += 3
            elif d[cword] == 2:
                cscore += 1
        
        print(ascore, bscore, cscore)

if __name__ == "__main__":
    solution()
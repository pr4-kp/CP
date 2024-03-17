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
        s = list(input().strip())
        while s and s[0] == s[-1]:
            s.pop(0)
            s.pop()
        
        for ii in range(0, len(s), 2):
            if s[ii] != s[ii+1]:
                print("Alice")
                break 
        else:
            print("Draw")

if __name__ == "__main__":
    solution()
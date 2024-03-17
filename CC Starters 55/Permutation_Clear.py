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
        a = arr_in()
        k = int(input())
        b = set(arr_in())
        for ele in a:
            if ele not in b:
                print(ele, end=' ')
        print()
                
            

if __name__ == "__main__":
    solution()
import sys
from collections import defaultdict
import sys
sys.stdin = open("second_hands_input.txt", "r")
sys.stdout = open("second_hands_output.txt", "w")
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
    for t in range(1, int(input()) + 1):
        n, k = tup_in()
        S = arr_in()
        if n == 1: 
            print("Case #" + str(t) + ":", "YES")
        elif k * 2 < n:
            print("Case #" + str(t) + ":", "NO")
        else:
            d = defaultdict(lambda: 0)
            for ii in range(n):
                d[S[ii]] += 1
            for ii in range(n):
                if d[ii] > 2:
                    print("Case #" + str(t) + ":", "NO")
                    break
            else:
                print("Case #" + str(t) + ":", "YES")



if __name__ == "__main__":
    solution()
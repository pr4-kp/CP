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
First player wins on 1 x even
Second player wins on 1 x odd


"""

def solution():
    for _ in range(int(input())):
        n, m = tup_in()
        if n % 2 != m % 2:
            print("Burenka")
        else:
            print("Tonya")

if __name__ == "__main__":
    solution()
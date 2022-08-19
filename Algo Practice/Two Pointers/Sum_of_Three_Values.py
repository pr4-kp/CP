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

"""

def solution():
    n, x = tup_in()
    A = arr_in()
    A_sort = sorted(A)
    A_vals = sorted(range(len(A)), key=A.__getitem__)
    ans = False

    for ii in range(n):
        left = 0
        right = n - 1
        findx = x - A_sort[ii]

        while left < right:
            if left == ii:
                left += 1
            elif right == ii:
                right -= 1
            elif A_sort[left] + A_sort[right] == findx:
                break
            elif A_sort[left] + A_sort[right] > findx:
                right -= 1
            else:
                left += 1
        if left == right:
            pass
        else:
            ans = True
            break
    if ans:
        print(A_vals[left] + 1, A_vals[right] + 1, A_vals[ii] + 1)
    else:
        print("IMPOSSIBLE")
            


if __name__ == "__main__":
    solution()
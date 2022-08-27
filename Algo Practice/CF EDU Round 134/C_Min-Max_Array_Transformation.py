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
10 20 30 40
22 33 33 55

12 2 3 
"""

def solution():
    for _ in range(int(input())):
        n = int(input())
        a = arr_in()
        b = arr_in()
        if a[-1] <= b[0]:
            sm = b[0]
            bg = b[-1]
            d_min = [abs(sm - ele) for ele in a]
            print(*d_min)
            d_max = [abs(bg - ele) for ele in a]
            print(*d_max)
        else:
            d_min = [-1] * n
            d_max = [0] * n

            top = n - 1
            bottom = n - 1
            avail = [n] * n
            while top > -1 and bottom > -1:
                if a[top] <= b[bottom]:
                    bottom -= 1
                else:
                    avail[top] = n - bottom - 1
                    top -= 1

            top_choice = n - 1
            for ii in reversed(range(n)):
                if avail[ii] == n - ii and ii != 0:
                    d_min[ii] = d_max[ii] = b[ii] - a[ii]
                    d_max[ii] = max(d_max[ii], b[top_choice] - a[ii])

                    top_choice = ii - 1
                else:
                    # print(top_choice, n - avail[ii])
                    d_max[ii] = b[top_choice] - a[ii]
                    if top_choice > n - avail[ii]:
                        d_max[ii] = max(d_max[ii], b[n - avail[ii]] - a[ii])
                        
            top = 0 
            bottom = 0
            while top < n and bottom < n:
                if a[top] > b[bottom]:
                    bottom += 1
                else:
                    d_min[top] = b[bottom] - a[top]
                    top += 1

            print(*d_min)
            print(*d_max)
                    




if __name__ == "__main__":
    solution()
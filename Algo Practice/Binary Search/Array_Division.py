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
I did a similar CF problem: Magazine Ad, this is just that but without the extra words.
Binary search over all possible maxs
- Upper bound: sum(X)
- Lower bound: max(X)

All my time was spent debugging make_subarray lol
"""

def solution():
    n, k = tup_in()
    X = arr_in()

    # check if possible to make subarray with this max size
    def make_subarray(size):
        subarray_ct = 0
        curr_size = 0

        for x in X:
            curr_size += x
            if curr_size == size:
                curr_size = 0
                subarray_ct += 1
            elif curr_size > size:
                curr_size = x
                subarray_ct += 1
            
        if curr_size > 0:
            subarray_ct += 1
        # print(subarray_ct, size)    

        return subarray_ct <= k

    left = max(X) - 1
    right = sum(X)

    while left + 1 < right:
        mid = left + (right - left) // 2
        # print(left, mid, right)

        if make_subarray(mid): 
            right = mid 
        else:
            left = mid
    
    print(right)

if __name__ == "__main__":
    solution()
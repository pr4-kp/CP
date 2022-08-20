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
Lower bound - 0
Upper bound - n ^ 2

Count the number of numbers less than mid, if total is == n ** 2 // 2,
then we are good. We can do this without 
calculating the whole table by going row by row.
1 2 3 4 5 ... n <- find max k s.t k * row < mid, so k = min(mid // row, n)

2 4 6 8 10 12 : mid = 12 => mid // row = 6 => k = 6
              : mid = 11 => mid // row = 5 => k = 5

PYTHON TOO SLOW @_@ do it in cpp instead I guess...
"""

def solution_bf():
    mult_table = []
    n = int(input())

    for ii in range(1, n + 1):
        for jj in range(1, n + 1):
            mult_table.append(ii * jj)

    mult_table.sort()
    print(mult_table[(n ** 2) // 2])

def solution():
    n = int(input())

    left = 0
    right = n ** 2

    def calc_less_than(mid):
        ans = 0
        for row in range(1, n + 1):
            ans += min(mid // row, n)
        return ans
    
    def calc_less_than_print(mid):
        ans = 0
        for row in range(1, n + 1):
            ans += min(mid // row, n)
            print(min(mid // row, n))
        return ans

    if n == 1:
        print(1)
    else:
        while left + 1 < right:
            mid = left + (right - left) // 2
            # print(mid, calc_less_than(mid))
            if calc_less_than(mid) == (n ** 2) // 2 + 1:
                break
            elif calc_less_than(mid) < (n ** 2) // 2 + 1:
                left = mid 
            else:
                right = mid
            
        print(mid)
        calc_less_than_print(mid)
        


if __name__ == "__main__":
    solution()


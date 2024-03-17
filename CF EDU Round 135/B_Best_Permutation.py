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
        a = [0] * n 
        a[n-1] = n
        a[n-2] = n - 1
        a[n-3] = 1
        
        if n % 2 == 1:
            if n % 3 == 0:
                a[n-2] = ((n-1) // 2) + 1
                a[n-3] = ((n-1) // 2) - 1
                a[n-4] = 1
                used = set(range(1,n+1))
                used.remove(n)
                used.remove(1)
                used.remove(((n-1) // 2) + 1)
                used.remove(((n-1) // 2) - 1)

                c = n - 5
                for ele in used:
                    a[c] = ele
                    c -= 1
                pass
            else:
                c = 0
                for ii in range(2, n - 1):
                    a[c] = ii
                    c += 1
        else:
            c = n - 4
            for ii in range(2, n - 1):
                a[c] = ii
                c -= 1
        print(*a)
        #tester
        # x = 0
        # for ele in a:
        #     if x>=ele:
        #         x = 0
        #     else:
        #         x += ele
        # print(x)

if __name__ == "__main__":
    solution()
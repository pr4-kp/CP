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
1 2 3 4 5
1 1 3 4 5 [1,1], [1,1,3], [1,1,3,4], [1,1,3,4,5]
1 2 2 4 5 [2,2], [1,2,2], [2,2,4], [1,2,2,4], [2,2,4,5], [1,2,2,4,5]
"""

def solution():
    n, m = tup_in()
    a = arr_in()
    ans = n*(n+1)//2


    for i in range(1, n):
        if a[i] != a[i-1]:
            ans += i*(n-i)


    for _ in range(m):
        i, x = tup_in()
        i -= 1
        if i > 0:
            if a[i-1] != a[i] and a[i-1] == x:
                ans -= i*(n-i)
            elif a[i-1] == a[i] and a[i-1] != x:
                ans += i*(n-i)
        if i < n-1:
            if a[i+1] != a[i] and a[i+1] == x:
                ans -= (i+1)*(n-i-1)
            elif a[i+1] == a[i] and a[i+1] != x:
                ans += (i+1)*(n-i-1)
        a[i] = x
        print(ans)


    

if __name__ == "__main__":
    solution()
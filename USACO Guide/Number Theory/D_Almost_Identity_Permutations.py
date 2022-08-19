import sys
input = sys.stdin.readline
inf = float('inf')
def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

"""
--- Notes ---
- k >= 1:
+1
- k >= 2:
transpositions:
n choose 2
- k >= 3:
1 2 3

3 1 2
2 3 1
n choose 3 * 2?
- k >= 4:
1 2 3 4

2 3 4 1
3 4 1 2
4 1 2 3
2 1 4 3
4 3 2 1
"""

def solution():
    n, k = tup_in()
    ans = 0
    if k >= 1:
        ans += 1
    if k >= 2:
        ans += (n * (n - 1)) // 2
    if k >= 3:
        ans += (2 * n * (n - 1) * (n - 2)) // 6
    if k >= 4:
        ans += (9 * n * (n - 1) * (n - 2) * (n - 3)) // 24
    print(ans)


if __name__ == "__main__":
    solution()
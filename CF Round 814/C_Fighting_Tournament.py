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
For the query for person i, first check if anyone higher is before them.
Then just check for the next highest person

If the person is the most powerful fighter, then the answer depends on k
Also, if they are in position 1, then we just have to subtract 1 from the answer.
"""

def solution():
    for _ in range(int(input())):
        n, q = tup_in()
        a = arr_in()
        nearest = []
        stack = [0, 0]
        for ind, val in enumerate(a):
            while stack and stack[-1][1] <= a[ind]:
                stack.pop()
            nearest.append(stack[-1][0])
            stack.append([ind + 1, val])
        print(nearest)

        for qq in range(q):
            i, k = tup_in()
            if a[i - 1] == n:
                if i == 1:
                    print(k)
                else:
                    print(max(k - (i - 2), 0))
            else:
                pass
                
if __name__ == "__main__":
    solution()
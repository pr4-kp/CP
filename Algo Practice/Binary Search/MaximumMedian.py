from bisect import bisect_left, bisect_right
from typing import Callable

def binary_search(arr, x, n):
    # Find index in sorted array of an element x. Returns -1 if not found.
    i = bisect_left(arr, x)
    if i != n and arr[i] == x:
        return i 
    else:
        return -1


a = [1, 2, 4, 4, 8]
x = int(4)
res = binary_search(a, x, 5)
if res == -1:
    print(x, "is absent")
else:
    print("First occurrence of", x, "is present at", res)

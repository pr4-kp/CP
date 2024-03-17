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


def kth_bit(n, k) -> bool:
    return (n >> k) & 1

def solution():
    for _ in range(int(input())):
        p, q, r = tup_in()
        ans = 0
        print(bin(p), bin(q), bin(r))
        for bit in range(22):
            if kth_bit(p, bit) and kth_bit(q, bit) and kth_bit(r, bit):
                print(bit, "+=2")
                ans += 2
            elif (kth_bit(p, bit) and kth_bit(q, bit)) or (kth_bit(p, bit) and kth_bit(r, bit)) or (kth_bit(q, bit) and kth_bit(r, bit)):
                print(bit, "+=1")
                ans += 1
        print(ans)
if __name__ == "__main__":
    solution()
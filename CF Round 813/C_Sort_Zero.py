import sys
input = sys.stdin.readline
inf = float('inf')

def solution():
    for _ in range(int(input())):
        n = int(input())
        A = list(map(int, input().split()))
        A.reverse()
        if n == 1:
            print(0)
        else:
            first_increase = -1
            for ii in range(n - 1):
                # find first increase
                if A[ii] < A[ii + 1]:
                    first_increase = ii + 1
                    break
            if first_increase == -1:
                print(0)
            else:
                removed = set(A[first_increase:])
                for ii in reversed(range(first_increase - 1)):
                    if A[ii] in removed:
                        removed = set(A[ii:])
                
                print(len(removed))

if __name__ == "__main__":
    solution()
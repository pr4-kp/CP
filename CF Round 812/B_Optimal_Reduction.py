import sys
input = sys.stdin.readline
inf = float('inf')

def solution():
    for _ in range(int(input())):
        n = int(input())
        A = list(map(int, input().split()))

        # measure changes in d dx
        if n == 1 or n == 2:
            print("YES")
        else:
            change = 0
            if A[0] > A[-1]:
                A.reverse()
            # print(A)
            ans = "YES"
            changed = False

            for ii in range(n-1):
                if not changed:
                    if A[ii+1] - A[ii] < 0:
                        changed = True
                else:
                    if A[ii+1] - A[ii] > 0:
                        ans = "NO"
                        break
            print(ans)

if __name__ == "__main__":
    solution()
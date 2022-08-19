import sys
input = sys.stdin.readline
inf = float('inf')

def solution():
    for _ in range(int(input())):
        n = int(input())
        A = [[] for ii in range(n)]
        for ii in range(n): 
            A[ii] = list(input().strip())
        # print(*A, sep='\n')
        if n == 1:
            print(0)
        elif n == 2:
            c = A[0].count('0') + A[1].count('0')
            c = min(4-c, c)
            print(c)
        else:
            ans = 0
            for ii in range(n // 2):
                for jj in range(n // 2):
                    # print(ii, jj)
                    diff = [A[ii][jj], A[n - jj - 1][ii],
                            A[jj][n - ii - 1], A[n - ii - 1][n - jj - 1]]
                    ans += min(diff.count('0'), 4 - diff.count('0'))
            
            if n % 2 == 1:
                for ii in range(n // 2):
                    diff = [A[ii][n // 2], A[n - ii - 1][n // 2], 
                            A[n // 2][n - ii - 1], A[n // 2][ii]]
                    ans += min(diff.count('0'), 4 - diff.count('0'))
            print(ans)
                



if __name__ == "__main__":
    solution()
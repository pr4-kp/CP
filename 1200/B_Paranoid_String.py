import sys
input = sys.stdin.readline
inf = float('inf')

def solution():
    for _ in range(int(input())):
        n = int(input())
        T = input().strip()
        # print(T)
        ans = n
        if n == 1:
            print(1)
        else:
            for ii in range(n-1):
                if T[ii + 1] != T[ii]:
                    ans += ii + 1
                # else:
                    # ans += 1
            print(ans)
        
        

if __name__ == "__main__":
    solution()
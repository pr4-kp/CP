import sys
input = sys.stdin.readline
inf = float('inf')

def solution():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        P = list(map(int, input().split()))
        ans = 0

        # print(P[:k-1])

        for ii in range(k):
            if ii + 1 not in P[:k]:
                ans += 1
        
        print(ans)

if __name__ == "__main__":
    solution()
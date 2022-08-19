import sys
input = sys.stdin.readline
inf = float('inf')

def solution():
    for _ in range(int(input())):
        n = int(input())
        P = []

        if n == 1:
            print(1)
        else:
            P = list(range(1, n+1))
            swap = n-2
            while swap >= 0:
                P[swap], P[swap + 1] = P[swap + 1], P[swap]
                swap -= 2
            print(*P)

            

if __name__ == "__main__":
    solution()
import sys
input = sys.stdin.readline
inf = float('inf')

def solution():
    for _ in range(int(input())):
        n = int(input())
        ans = 0
        maxX = 0
        maxY = 0
        minX = 0
        minY = 0
        boxes = []
        for ii in range(n): 
            x, y = map(int, input().split())
            maxX = max(maxX, x)
            minX = min(minX, x)
            maxY = max(maxY, y)
            minY = min(minY, y)

        print((abs(maxX) + abs(maxY) + abs(minX) + abs(minY)) * 2)
if __name__ == "__main__":
    solution()
# import numpy as np

import sys
sys.stdin = open("balancing.in","r")
sys.stdout = open("balancing.out","w")

def solution():
    n, b = map(int, input().split())
    sol = []
    v_fence = set()
    h_fence = set()
    cowlist = []
    for cow in range(n):
        xpos, ypos = map(int, input().split())
        v_fence.add(xpos+1)  # x-coords of relevant vertical fences
        h_fence.add(ypos+1)
        cowlist.append([xpos, ypos])
    for checkX in v_fence:
        for checkY in h_fence:
            cX = checkX
            cY = checkY
            c0 = 0
            c1=0
            c2=0
            c3=0
            
            for cowz in cowlist:
                if cowz[0] < checkX and cowz[1] > checkY:
                    c0 += 1
                elif cowz[0] > checkX and cowz[1] > checkY:
                    c1 += 1
                elif cowz[0] > checkX and cowz[1] < checkY:
                    c2 += 1
                elif cowz[0] < checkX and cowz[1] < checkY:
                    c3 += 1
            sol.append(max(c1,c2,c3,c0))
    print(min(sol))


if __name__ == "__main__":
    solution()
import sys
sys.stdin = open("race.in","r")
sys.stdout = open("race.out","w")

def optTime(k, endSpeed):
    ans = 0
    dist = k
    s = 1
    while dist > 0 and s < endSpeed:
        ans += 1
        dist -= s
        s += 1
    first = True
    while dist > 0:
        ans += 1
        dist -= s
        if first:
            first = False
        else:
            s += 1
            first = True
    return(ans)


def solution():
    k, n = map(int, input().split())
    x = []
    for _ in range(n):
        print(optTime(k, int(input())))


if __name__ == "__main__":
    solution()
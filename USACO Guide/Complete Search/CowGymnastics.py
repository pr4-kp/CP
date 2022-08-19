import sys
sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")

def checkrank(rank, n, comp1, comp2):
    for rr in rank:
        ind = 0
        while(ind < n and rr[ind] != comp1):
            if rr[ind] == comp2:
                return False
            ind += 1
    return True

def solution():
    rank = []
    beats = True
    ans = 0
    k, n = map(int, input().split())
    for _ in range(k):
        rank.append(list(map(int, input().split())))
    for comp1 in range(1, n+1):
        for comp2 in range(1, n+1):
            if comp1 != comp2:
                if checkrank(rank, n, comp1, comp2):
                    ans += 1
    print(ans)

if __name__ == "__main__":
    solution()

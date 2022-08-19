import sys
sys.stdin = open("outofplace.in","r")
sys.stdout = open("outofplace.out","w")

def solution():
    n = int(input())
    cow = []
    ans = 0

    for ii in range(n):
        cow.append(int(input()))
    cowS = sorted(cow)
    for i in range(n):
        if cow[i] != cowS[i]:
            ans += 1

    print(ans - 1)


if __name__ == "__main__":
    solution()
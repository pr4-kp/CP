import sys
sys.stdin = open("breedflip.in","r")
sys.stdout = open("breedflip.out","w")

def solution():
    n = int(input())
    a = input()
    b = input()
    ans = 0
    start = False

    for ii in range(n):
        if a[ii] != b[ii]:
            start = True
        if start:
            if a[ii] == b[ii]:
                ans += 1
                start = False
    print(ans)


if __name__ == "__main__":
    solution()
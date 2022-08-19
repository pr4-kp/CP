import sys
sys.stdin = open("div7.in","r")
sys.stdout = open("div7.out","w")

def solution():
    n = int(input())
    ids = [0]
    a = [0]
    for i in range(n):
        ids.append(ids[-1])
        ids[-1] += int(input())
        ids[-1] = ids[-1] % 7
    for j in range(7):
        if j in ids:
            a.append(n - ids[::-1].index(j) - ids.index(j))
    print(max(a))


if __name__ == "__main__":
    solution()
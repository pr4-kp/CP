def solution():
    for _ in range(int(input())):
        l = int(input())
        s = input()
        s = sorted(s)
        ans = 2
        for ii in range(1, l):
            if s[ii] == s[ii-1]:
                ans += 1
            else:
                ans += 2
        print(ans)


if __name__ == "__main__":
    solution()
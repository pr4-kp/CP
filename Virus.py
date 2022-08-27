inf = float('inf')
def solution():
    s = []
    for _ in range(int(input())):
        n, m = map(int, input().split())
        diff = []
        ans = 0
        A = sorted(list(map(int, input().split())))

        for ii in range(m-1):
            diff.append(A[ii+1]-A[ii]-1)
        diff.append(n+A[0]-A[-1]-1)
        diff.sort(reverse=True)

        ii = 0
        # print(diff)
        while diff:
            trysave = diff.pop(0) - 1 - (2 * ii)
            saved = max(trysave, 0)
            # print(saved)
            ans += saved
            if trysave == 0:
                ans += 1
                ii += 1 # but i think it ends
            if saved == 0:
                break
            else:
                ii += 2
        # s.append(n - ans)
        print(n-ans)
    # print(s)


if __name__ == "__main__":
    solution()
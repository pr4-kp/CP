inf = float('inf')
def solution():
    # tryremove = list(reversed(range(1, 10)))
    for _ in range(int(input())):
        s = int(input())
        if s <= 9:
            print(s)
        else:
            tryremove = 9
            ans = []
            while s > 0:
                if s - tryremove < 0:
                    ans.append(s)
                else:
                    ans.append(tryremove)
                s -= tryremove
                tryremove -= 1

            for ii in range(len(ans)-1, -1, -1):
                print(ans[ii], end='')
            print()
            

if __name__ == "__main__":
    solution()
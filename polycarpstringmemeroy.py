def solution():
    for _ in range(int(input())):
        ans = 0
        polyword = input()
        trackedwords = []
        if len(polyword) <= 3:
            print(1)
        else:
            for char in polyword:
                if char not in trackedwords:
                    trackedwords.append(char)
                else:
                    pass 
                if len(trackedwords) > 3:
                    ans += 1
                    trackedwords.clear()
                    trackedwords.append(char)

            if len(trackedwords) != 0:
                ans += 1
            print(ans)


if __name__ == "__main__":
    solution()
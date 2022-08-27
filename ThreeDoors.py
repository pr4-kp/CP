def solution():
    for _ in range(int(input())):
        
        key = int(input())
        got = {key}
        behind = list(map(int, input().split()))
        while len(got) != 3:
            if behind[key - 1] == 0:
                print("NO")
                break
            else:
                key = behind[key - 1]
                got.add(key)
        if len(got) == 3:
            print("YES")



if __name__ == "__main__":
    solution()
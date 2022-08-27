from os import cpu_count


def solution():
    for _ in range(int(input())):
        if input().lower() == "yes":
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solution()
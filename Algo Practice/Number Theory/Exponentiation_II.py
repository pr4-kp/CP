MOD = 10 ** 9 + 7

def solution():
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        print(pow(a, pow(b, c, MOD - 1), MOD))

if __name__ == "__main__":
    solution()
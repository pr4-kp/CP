def solution():
    ans = []
    for _ in range(int(input())):
        n = int(input())
        wheelNums = list(map(int, input().split()))
        for ii in range(n):
            move = input().split()
            for jj in range(int(move[0])):
                if move[1][jj] == 'D':
                    wheelNums[ii] += 1
                else:
                    wheelNums[ii] -= 1
        [print(a % 10, end = ' ') for a in wheelNums]


if __name__ == "__main__":
    solution()
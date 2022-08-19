inf = float('inf')
def solution():
    for _ in range(int(input())):
        n = int(input())
        A = list(reversed(list(map(int, input().split()))))

        Seen = set()
        ii = 0
        while ii < n:
            if A[ii] in Seen:
                break
            Seen.add(A[ii])
            ii += 1
        print(n-ii)


if __name__ == "__main__":
    solution()
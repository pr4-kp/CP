from bisect import bisect, bisect_left


def psum(l, n):
    p = [0]
    for i in range(n):
        p.append(p[-1])
        p[-1] += l[i]
    return p

inf = float('inf')
def solution():
    for _ in range(int(input())):
        n, q = map(int, input().split())
        A = sorted(list(map(int, input().split())), reverse=True)
        pA = psum(A, n)
        # print(pA)
        sol = []
        for ii in range(q):
            desired_sum = int(input())
            ans = bisect_left(pA, desired_sum)
            if ans > n:
                print(-1)
            else:
                print(ans)


if __name__ == "__main__":
    solution()
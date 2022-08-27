# def av(a,b):
#     return (a // 2) + (b // 2) + ((a % 2 + b % 2) // 2)

inf = float('inf')
def solution():
    ans = []
    for _ in range(int(input())):
        s = 0
        n, x = map(int, input().split())
        A = list(map(int, input().split()))
        runningmin = inf
        runningmax = -inf
        for ii in range(n-1):
            if abs(A[ii] - A[ii+1]) > 2*x:
                s += 1
                runningmin = inf
                runningmax = -inf
            elif runningmin != inf and runningmax != -inf:
                if abs(runningmax - A[ii+1]) > 2*x or abs(runningmin - A[ii+1]) > 2*x or abs(runningmax - runningmin) > 2*x:
                    s += 1
                    runningmin = inf
                    runningmax = -inf
                else:
                    runningmin = min(runningmin, A[ii])
                    runningmax = max(runningmax, A[ii])
            else:
                runningmin = min(runningmin, A[ii])
                runningmax = max(runningmax, A[ii])
        print(s)
        # ans.append(s)
    # print(ans)

if __name__ == "__main__":
    solution()
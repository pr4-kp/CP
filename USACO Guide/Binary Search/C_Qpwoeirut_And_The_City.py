def coolify(h, ii):
    if h[ii] > max(h[ii-1], h[ii+1]):
        return 0
    else:
        return max(h[ii-1], h[ii+1]) - h[ii] + 1


# def maxcool(coollist, ct, n):
#     if ct ==
inf = float('inf')

def solution():
    for _ in range(int(input())):
        n = int(input())
        h = list(map(int, input().split()))
        coollist = []
        ans = inf
        for ii in range(1, n-1):
            coollist.append(coolify(h, ii))
        # print(coollist)
        # print(coollist)

        if len(coollist) % 2 == 1:
            ans = 0
            for ii in range(len(coollist)): 
                if ii % 2 == 0:
                    ans += coollist[ii]
            print(ans)
        else:
            ans = []
            # go through 0 1 0 0 1 0 1 0
            #            0 1 0 1 0 0 1 0
            #            0 1 0 1 0 1 0 0
            m = len(coollist) // 2
            # print(coollist)
            for ii in range(m + 1):
                cur_cost = 0 
                start_left = 0
                start_right = len(coollist) - 1
                done = []
                

                for jj in range(ii): 
                    cur_cost += coollist[start_left]
                    start_left += 2

                for jj in range(m - ii):
                    cur_cost += coollist[start_right]
                    start_right -= 2

                ans.append(cur_cost)
            print(min(ans))
            pass


if __name__ == "__main__":
    solution()

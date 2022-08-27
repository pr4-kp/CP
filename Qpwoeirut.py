def coolify(h, ii):
    if h[ii] > max(h[ii-1], h[ii+1]):
        return 0
    else:
        return max(h[ii-1], h[ii+1]) - h[ii] + 1

def maxcool(coollist, ct, n):
    if ct == 

def solution():
    for _ in range(int(input())):
        n = int(input())
        h = list(map(int, input().split()))
        coollist = [0]
        for ii in range(1, n-1):
            coollist.append(coolify(h, ii))
        # print(coollist)
        print(coollist)

if __name__ == "__main__":
    solution()
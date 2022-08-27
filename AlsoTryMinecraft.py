def psum(l, n):
    p = [0]
    for i in range(n - 1):
        p.append(p[-1])
        if l[i] > l[i+1]:
            p[-1] += l[i] - l[i+1] 
    # p.append(p[-1])
    return p

def solution():
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))
    ps = psum(heights, n)
    heights.reverse()
    psr = psum(heights, n)
    psr.reverse()
    # print(ps, psr)
    quests = []
    for _ in range(m):
        quest = list(map(int, input().split()))
        if quest[0]<quest[1]:
            print(ps[quest[1]-1] - ps[quest[0]-1])
        else:
            print(psr[quest[1]-1] - psr[quest[0]-1])
    
    

    


if __name__ == "__main__":
    solution()
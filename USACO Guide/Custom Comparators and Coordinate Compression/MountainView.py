def solution():
    pos = []
    n = int(input())
    for _ in range(n):
        b, e = map(int, input().split())
        pos.append((b-e, b+e))
    pos.sort(key = lambda x: (x[0], -x[1]))
    cur = pos[0][1]

    ans = 1
    for i in range(1, n):
        end = pos[i][1]
        if end > cur:
            cur = end
            ans += 1
    print(ans)
        
        

if __name__ == "__main__":
    solution()
def solution():
    fin = []
    for _ in range(int(input())):
        
        n = int(input())
        c = list(map(int, input().split()))
        ans = [0] * n
        prev = [-1] * n
        colors = {i for i in range(n)}

        for block in range(n):
            if prev[c[block] - 1] != -1 and (prev[c[block] - 1] - block) % 2 == 0:
                pass
            else: 
                ans[c[block] - 1] += 1
            prev[c[block] - 1] = block
        fin.append(ans)
    for f in fin:
        print(' '.join(str(x) for x in f))


if __name__ == "__main__":
    solution()
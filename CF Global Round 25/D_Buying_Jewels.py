def solve(): 
    n, k = map(int, input().split())
    if k > n:
        print("NO")
        return
    elif k == n:
        print("YES")
        print(1)
        print(1)
    elif k > -(-n//2):
        print("NO")
    else:
        print("YES")
        print(2)
        print(n - k + 1, 1)

for t in range(int(input())):
    solve()
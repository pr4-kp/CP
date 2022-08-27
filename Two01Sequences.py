inf = float('inf')
def solution():
    # ans = []
    for _ in range(int(input())):
        
        n, m = map(int, input().split())
        a = list(map(int, list(input())))
        b = list(map(int, list(input())))
        
        s = "NO"
        if m == 1 and b[0] in a:
            s = "YES"
        elif a[-(m-1):] == b[1:] and b[0] in a[:-(m-1)]:
            s = "YES"
        
        print(s)
        
        


        
    


if __name__ == "__main__":
    solution()
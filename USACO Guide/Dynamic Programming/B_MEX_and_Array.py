inf = float('inf')
def solution():
    for _ in range(int(input())):
        n = int(input())
        A = list(map(int, input().split()))
        vals = {}

        def dp(subset, rem, l):
            if subset == [0]:
                vals[subset] = 2
                return
            elif l == 1:
                vals[subset] = 1
                return                
        
        print(dp(A, n))



if __name__ == "__main__":
    solution()
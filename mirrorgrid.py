def solution():
    for _ in range(int(input())):
        grid = [] 
        changes = 0
        c0 = 0
        n = int(input())
        if n == 1:
            input()
            changes = 0
        else:
            for kk in range(n): 
                grid.append(list(input()))
            if n % 2 == 1:
                for ii in range(n//2):
                    s = int(grid[ii][n//2]) + int(grid[n//2][ii]) + \
                        int(grid[n-1-ii][n//2]) + int(grid[n//2][n-1-ii])
                    changes += min(4-s, s)
            for ii in range(n//2): 
                for jj in range(n//2): 
                    s = int(grid[ii][jj]) + int(grid[n-ii-1][jj]) + \
                        int(grid[ii][n-jj-1]) + int(grid[n-ii-1][n-jj-1])
                    changes += min(4-s, s)
            # print(changes)
        print(changes)
        


if __name__ == "__main__":
    solution()
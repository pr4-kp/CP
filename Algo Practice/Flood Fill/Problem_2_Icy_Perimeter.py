# import sys
# sys.stdin = open("perimeter.in","r")
# sys.stdout = open("perimeter.out","w")

inf = float('inf')
def solution():
    cols = rows = int(input())
    grid = [input() for _ in range(rows)]
    visited = [[False for i in range(cols)] for j in range(rows)]
    area = 0 
    perimeter = 0

    def floodfill(r, c):
        global visited
        global area 
        global perimeter 

        frontier = [(r,c)]
        while frontier:
            if ((r < 0 or r >= rows or c < 0 or c >= cols) or grid[r][c] != '#'):
                perimeter += 1
                continue
            elif visited[r][c]:
                continue
            else:
                area += 1
            visited[r][c] = True
            frontier.append((r-1, c))
            frontier.append((r, c-1))
            frontier.append((r+1, c))
            frontier.append((r, c+1))
    
    for row in range(rows):
        for col in range(cols):
            if not visited[row][col] and grid[row][col] == '#':
                floodfill(row, col)
                print(area, perimeter)
                area = 0
                perimeter = 0

            




if __name__ == "__main__":
    solution()
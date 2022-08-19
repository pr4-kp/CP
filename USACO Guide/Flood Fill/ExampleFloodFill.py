row_num, col_num = [int(i) for i in input().split()]
grid = [input() for _ in range(row_num)]
visited = [[False for _ in range(col_num)] for _ in range(row_num)]


def floodfill(r: int, c: int):
	global visited

	"""
	Note: you can also use queue and pop from the
	front (as opposed to popping from the back) for a BFS-based approach
	"""
	frontier = [(r, c)]
	while frontier:
		r, c = frontier.pop()
		if (r < 0 or r >= row_num or c < 0 or c >= col_num
                        or visited[r][c] or grid[r][c] == '#'):
			continue

		visited[r][c] = True
		frontier.append((r - 1, c))
		frontier.append((r, c - 1))
		frontier.append((r + 1, c))
		frontier.append((r, c + 1))


room_num = 0
for row in range(row_num):
	for col in range(col_num):
		if not visited[row][col] and grid[row][col] == '.':
			floodfill(row, col)
			room_num += 1
print(room_num)

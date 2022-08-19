# n = int(input())
# p = list(map(int, input().split()))

# def solve(i, s1, s2):
# 	if i == n:
# 		return abs(s2 - s1)
# 	return min(solve(i + 1, s1 + p[i], s2),
# 			   solve(i + 1, s1, s2 + p[i]))

# print(solve(0, 0, 0))

n = int(input())
p = list(map(int, input().split()))

ans = float('inf')
for mask in range(1 << n):
	s1, s2 = 0, 0
	for i in range(n):
		if mask & (1 << i):
			s1 += p[i]
		else:
			s2 += p[i]
	ans = min(ans, abs(s1 - s2))

print(ans)

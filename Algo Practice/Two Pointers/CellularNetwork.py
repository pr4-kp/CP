def two_pointers(cities, towers, n, m):
    i = 0
    ans = 0
    for city in cities:
        while i < m and towers[i] < city:
            i += 1
        # if not last tower
        cur = abs(towers[min(m-1, i)] - city)
        # if not first tower
        if i:
            cur = min(cur, abs(towers[i-1]-city))
        ans = max(ans, cur)
    print(ans)

def solution():
    n, m = map(int ,input().split())
    cities = list(map(int, input().split()))
    towers = list(map(int, input().split()))
    
    two_pointers(cities, towers, n, m)


if __name__ == "__main__":
    solution()
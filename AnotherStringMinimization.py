def solution():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = map(int, input().split())
        s = ['B'] * m
        for change in a:
            c = change-1
            if s[min(c, m-1-c)] == 'A':
                s[max(c, m-1-c)] = 'A'
            else:
                s[min(c, m-1-c)] = 'A'
        print(''.join(s))

if __name__ == "__main__":
    solution()
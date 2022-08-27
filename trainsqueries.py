from re import I


def solution():
    for _ in range(int(input())):
        input()
        numstations, queries = map(int, input().split())
        stops = input().split()
        first = {}
        last = {}
        for i in range(numstations):
            if stops[i] not in first:
                first[stops[i]] = i
            last[stops[i]] = i
        for tests in range(queries):
            a, b = map(str, input().split())
            if a not in first or b not in first:
                print("NO")
                continue
            if first[a] < last[b]:
                print("YES")
            else:
                print("NO")



if __name__ == "__main__":
    solution()
from bisect import bisect

# import sys
# sys.stdin = open("haybales.in","r")
# sys.stdout = open("haybales.out","w")

def solution():
    bale_num, query_num = map(int, input().split())
    bales = sorted(list(map(int, input().split())))
    for _ in range(query_num):
        start, end = map(int, input().split())
        print(bisect(bales, end) - bisect(bales, start-1))



if __name__ == "__main__":
    solution()
import collections

import sys
input = sys.stdin.readline
inf = float('inf')
def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

"""
--- Notes ---

"""

def solution():
    n,m=tup_in()
    graph = [[] for i in range(n)]
    for _ in range(m): 
        u,v=tup_in()
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
        
        
    d = collections.deque()
    d.appendleft()

if __name__ == "__main__":
    solution()
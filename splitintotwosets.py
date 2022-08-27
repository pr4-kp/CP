
def bfs_color(graph, visited, node, coloring):
    if visited[node]:
        return 1
    else:
        visited[node] = True
        coloring[node] = True
        queue = []
        queue.append(node)
        
        while queue:
            m=queue.pop(0)
            visited[m] = True
            for neighbor in graph[m]:
                if visited[neighbor] == False:
                    queue.append(neighbor)
                if coloring[neighbor] == coloring[m]:
                    return 0
                else:
                    coloring[neighbor] = not coloring[m]
        return 1


# print("Following is the Breadth-First Search")
# bfs_color(graph, visited, '5', True)    # function calling
def solution():
    fin = []
    for _ in range(int(input())):
        domCt = int(input())
        dominos = [0]*domCt
        ans = 1
        for dom in range(domCt):
            dominos[dom] = list(map(int, input().split()))
            if dominos[dom][1] == dominos[dom][0]: ans = 0

        adjList = [[] for i in range(domCt)]
        for ii in range(domCt):
            for jj in range(domCt):
                if (dominos[jj][0] in dominos[ii] or dominos[jj][1] in dominos[ii]) and jj != ii:
                    adjList[ii].append(jj)
        visited = [0]*domCt
        
        coloring = [-1]*domCt
        coloring[0] = True
        
        for curNode in range(domCt):
            if bfs_color(adjList, visited, curNode, coloring):
                pass
            else:
                ans = 0
                break
        if ans:
            fin.append("YES")
            # print("YES")
        else:
            fin.append("NO")
            # print("NO")

    [print(f) for f in fin]

if __name__=="__main__":
    solution()
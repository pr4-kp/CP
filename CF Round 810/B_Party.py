inf = float('inf')
def solution():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        A = list(map(int, input().split()))
        Degrees = [0] * n
        Friends = []

        for ii in range(m): 
            u, v = map(int, input().split())
            Degrees[u-1] += 1
            Degrees[v-1] += 1
            Friends.append([u-1, v-1])
        
        if m % 2 == 0:
            print(0)
        else:
            ans = []
            # remove one friend with an odd degree
            # remove two friends with an even degree
            for ii in range(n): 
                if Degrees[ii] % 2 == 1:
                    ans.append(A[ii])
            for ii in range(m): 
                if Degrees[Friends[ii][0]] % 2 == 0 and Degrees[Friends[ii][1]] % 2 == 0:
                    ans.append(A[Friends[ii][0]] + A[Friends[ii][1]])
            print(min(ans))
            


if __name__ == "__main__":
    solution()
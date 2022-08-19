def between(A, B):
    return ((B + A) * (B - A + 1)) // 2


inf = float('inf')
def solution():
    for _ in range(int(input())):
        m = int(input())
        A1 = list(map(int, input().split()))
        A2 = list(map(int, input().split()))
        # print([A1, A2])
        A = [A1, A2]
        if max(max(A1), max(A2)) < 2 * m:
            print(2 * m - 1)
        else: # more complex algorithms are needed...
            if max(A1) > max(A2):
                A1.reverse()
                # finding the index of element
                index = A1.index(max(A1))
                # printing the final index
                print(m - index - 1)
            elif max(A1) < max(A2):
                A2.reverse()
                # finding the index of element
                index = A2.index(max(A2))
                # printing the final index
                print(m - index - 1)
            else:
                A1.reverse()
                # finding the index of element
                index1 = A1.index(max(A1))
                # printing the final index
                # print(m - index - 1)
                A2.reverse()
                # finding the index of element
                index2 = A2.index(max(A2))
                # printing the final index
                print(max(m - index1 - 1, m - index2 - 1))
        
        # t = 0 


if __name__ == "__main__":
    solution()
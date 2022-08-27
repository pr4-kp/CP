def solution():
    for _ in range(int(input())):
        s = []
        n = int(input())
        sol = []
        for nn in range(n): 
            s.append(input())
        ss = set(s)
        for word in s:
            c = 0
            for ind in range(1, len(word)): 
                if word[:ind] in ss and word[ind:] in ss:
                    c = 1
                    break
            sol.append(c)
        print(''.join(str(a) for a in sol))



if __name__ == "__main__":
    solution()
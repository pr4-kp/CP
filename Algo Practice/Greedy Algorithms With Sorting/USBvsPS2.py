def solution():
    a, b, c = map(int, input().split())
    MM = []
    t = 0
    m = int(input())
    for ii in range(m): 
        add = input().split()
        MM.append([int(add[0]), add[1]])

    aCt = bCt = cCt = 0

    MM.sort(key=lambda x:x[0])

    for ii in range(m): 
        if aCt < a and MM[ii][1] == 'USB':
            t += MM[ii][0]
            aCt += 1
        elif bCt < b and MM[ii][1] == 'PS/2':
            t += MM[ii][0]
            bCt += 1
        elif cCt < c:
            t += MM[ii][0]
            cCt += 1
        else:
            pass 
    
    print(aCt + bCt + cCt, t)




if __name__ == "__main__":
    solution()
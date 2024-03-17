
def psum(a):

    psum = [0]

    for i in a:

        psum.append(psum[-1] + i)  # psum[-1] is the last element in the list

    return psum
for __ in range(int(input())):
    n = int(input())
    c = sorted(list(map(int, input().split())))
    p = psum(c)

    if n == 1 and c == [1]:
        print('YES')
        continue
    elif n == 1 and c != [1]:
        print('NO')
        continue
    elif c[0] != 1:
        print('NO')
    
    sol = 'YES'
    for j in range(1, n):
        if c[j] > p[j]:
            sol = 'NO'
            break 
    
    print(sol)


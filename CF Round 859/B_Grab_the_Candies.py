for _ in range(int(input())):
    m = b = 0
    n = int(input())
    a = list(map(int, input().split()))
    for ele in a:
        if ele % 2 == 0:
            m += ele 
        else:
            b += ele
    if m <= b:
        print('NO')
    else:
        print('YES')
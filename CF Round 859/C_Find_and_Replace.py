for __ in range(int(input())):
    set1 = set()
    set2 = set()
    n = int(input())
    s = input()
    for j in range(n):
        if j % 2 == 0:
            set1.add(s[j])
        else:
            set2.add(s[j])
    # print(set1, set2)
    if set1.intersection(set2):
        print('NO')
    else:
        print('YES')
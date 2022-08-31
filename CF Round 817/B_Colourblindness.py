for _ in range(int(input())):
    n = int(input())
    s1 = list(input())
    s2 = list(input())

    for index, char in enumerate(s1):
        if char == 'G' or char == "B":
            s1[index] = 'S'
    for index, char in enumerate(s2):
        if char == 'G' or char == "B":
            s2[index] = 'S'


    if s1 == s2:
        print("YES")
    else:
        print("NO")
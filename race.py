for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    s = input()

    liked = []
    disliked = []

    for j in range(n):
        if s[j] == '0':
            disliked.append(p[j])
        else:
            liked.append(p[j])

    # print(liked, disliked)
    disliked.sort(reverse=True)
    d = len(disliked)
    liked.sort()
    l = len(liked)

    # the disliked songs should be in [0,1,...,len(disliked)-1]
    # replace the largest disliked song with len(disliked) - 1
    # etc.
    for j in range(d):
        m = disliked[j]
        p[p.index(m)] = d - j - 1

    # the liked songs are in [len(disliked),...n-1]
    # replace the smallest liked song with len(disliked)
    # etc.
    for j in range(l):
        m = liked[j]
        p[p.index(m)] = d + j

    [print(str(ele + 1) + " ", end="") for ele in p]
    print()

def psum(a):

    psum = [0]

    for i in a:

        psum.append((psum[-1] + i) & 1)  # psum[-1] is the last element in the list

    return psum


for __ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    p = psum(a)
    for __ in range(q):
        # print(p)
        l, r, k = map(int, input().split())
        test = 0
        if l != 1:
            test += p[l-1]
        if r != n:
            test += p[n] - p[r]
        test += k * (r-l + 1) 
        if test & 1:
            print('YES')
        else:
            print('NO')



# for i in range(Q):

# 	l, r = map(int, input().split())

# 	print(p[r] - p[l])
from sys import stdout
def psum(a):

    psum = [0]

    for i in a:

        psum.append(psum[-1] + i)  # psum[-1] is the last element in the list

    return psum

def format_out(l, r):
    print('? ', end='')
    for j in range(l, r+1):
        print(j, end=' ')
    print()
    stdout.flush()
    # input()
        

for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    p = psum(a)

    l = 1
    r = n

    while l != r - 1 and l != r:
        mid = (l + r - 1) // 2
        format_out(l, mid)
        if int(input()) == p[mid]:
            l = (mid) + 1
        else:
            r = (mid)
    print('! ' + str(r))
    stdout.flush()


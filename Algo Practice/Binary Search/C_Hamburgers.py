inf = float('inf')
def solution():
    hamburger = input()
    cb, cs, cc = hamburger.count('B'), hamburger.count(
        'S'), hamburger.count('C')
    nb, ns, nc = map(int, input().split())
    pb, ps, pc = map(int, input().split())
    r = int(input())
    # print(cb, cs, cc)

    def can_buy(n):
        # print("it takes", (pb * max(cb * n - nb, 0) + ps * max(cs * n - ns, 0)
            #    + pc * max(cc * n - nc, 0)), "to buy", n)
        return r >= (pb * max(cb * n - nb, 0) + ps * max(cs * n - ns, 0) 
                    + pc * max(cc * n - nc, 0))

    left = 0
    init = 0
    if cb != 0:
        init += nb // cb + 1
    if cs != 0:
        init += ns // cs + 1
    if cc != 0:
        init += nc // cc + 1

    right = (pb * cb * r + ps * cs * r + pc * cc * r) + init
    
    # print(right)

    while left < right:
        mid = left + (right - left) // 2
        if can_buy(mid):
            left = mid + 1
            # print('can buy', mid)
        else:
            right = mid
            # print('cant buy', mid)
    print(left - 1)


if __name__ == "__main__":
    solution()
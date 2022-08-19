def psum(l, n, record):
    p = [0]
    for i in range(n):
        p.append(p[-1])
        p[-1] += l[i]

        v = p[-1] - i - 1 

        if v not in record:
            record[v] = 0
        record[v] += 1

    return record

def solution():
    for _ in range(int(input())):
        ans = 0
        n = int(input())
        aa = list(map(int, list(input())))
        r = psum(aa, n, {0:1})
        # print(paa)
        c2 = lambda x: (x*(x-1))//2
        # print(r)
        
        for vv in r.values():
            ans += c2(vv)
        print(ans)


if __name__ == "__main__":
    solution()
def psum(l, n):
    p = [0]
    for i in range(n):
        p.append(p[-1])
        if l[i] == '(':
            p[-1] += 1
        if l[i] == ')':
            p[-1] -= 1
        else:
            pass
    return p

def solution():
    for _ in range(int(input())):
        brac = list(input())

        optot = brac.count('(')
        cltot = brac.count(')')
        qtot = brac.count('?')

        fin = brac.copy()
        # print(psum(brac, len(brac)))
        if qtot == 1 or qtot == 0:
            print("YES")
        elif len(brac) == 2:
            print("YES")
        else:
            print("NO")
        
        # for c, i in enumerate(brac):
        #     if c == '?':
        #         if i == 0:
        #             optot -= 1
        #         elif cltot == 0:
        #             cl += 1
        #         qtot -= 1
        #     elif c == '(':
        #         optot -= 1
        #     elif c == ')':
        #         cltot -= 1

if __name__ == "__main__":
    solution()
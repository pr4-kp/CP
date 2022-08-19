import sys
sys.stdin = open("evolution.in","r")
sys.stdout = open("evolution.out","w")

def checkTree(allTraits, prop, n):
    for t1 in allTraits:
        for t2 in allTraits:
            if t1 != t2:
                c1 = False
                c2 = False
                c3 = False
                for ii in range(n):
                    if (t1 in prop[ii]) and (t2 not in prop[ii]):
                        c1 = True
                    elif (t2 in prop[ii]) and (t1 not in prop[ii]):
                        c2 = True
                    elif (t1 in prop[ii]) and (t2 in prop[ii]):
                        c3 = True
                if c1 and c2 and c3:
                    return False
    return True

def solution():
    n = int(input())
    prop = [set() for i in range(n)]
    allTraits = set()
    for ii in range(n):
        t = input().split()
        prop[ii].update(t[1:])
        allTraits.update(t[1:])
    if (checkTree(allTraits, prop, n)):
        print("yes")
    else:
        print("no")
    
                    

if __name__ == "__main__":
    solution()
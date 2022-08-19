import sys
sys.stdin = open("notlast.in","r")
sys.stdout = open("notlast.out","w")

def solution():
    n = int(input())
    milk = {'Bessie':0, 'Elsie': 0, 'Daisy':0, 'Gertie':0, 'Annabelle':0, 'Maggie':0, 'Henrietta':0}
    for _ in range(n):
        cow = input().split()
        milk[cow[0]] += int(cow[1])
    s = [(amt, name) for name, amt in milk.items()]
    s.sort()
    m = s[0][0]
    for k in range(1, 7):
        if s[k][0] != m:
            if k != 6:
                if s[k][0] != s[k+1][0]:
                    print(s[k][1])
                else:
                    print("Tie")
            else:
                print(s[k][1])
            break 
    else: 
        print("Tie")

if __name__ == "__main__":
    solution()
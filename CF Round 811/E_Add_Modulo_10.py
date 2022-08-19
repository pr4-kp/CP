inf = float('inf')
def solution():
    for _ in range(int(input())):
        n = int(input())
        A = list(map(int, input().split()))
        working = set()

        for num in A:
            
            useful = (num // 10) % 2
            rem = num % 10
            if rem in [3, 6, 7, 9]:
                useful -= 1
                useful %= 2
                working.add(useful)
            elif rem in [1, 2, 4, 8]:
                working.add(useful)
            else:
                working.add(5)
        
        if len(working) == 1:
            for onlything in working:
                if onlything == 5:
                    working2 = set()
                    for num in A:
                        if num % 10 == 5:
                            working2.add(num // 10 + 1)
                        elif num % 10 == 0:
                            working2.add(num // 10)
                        else:
                            working2.add(-1)
                    if len(working2) == 1:
                        print("Yes")
                    else:
                        print("No")
                    

                else:
                    print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solution()
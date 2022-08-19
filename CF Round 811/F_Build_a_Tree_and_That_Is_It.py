inf = float('inf')

def solution():
    for _ in range(int(input())):
        n, d12, d23, d31 = map(int, input().split())
        c = (d31 - d12 + d23) / 2
        b = d23 - c
        a = d31 - c
        # print(a, b, c)

        avail_nodes = list(range(4, n+1))
        # print(avail_nodes)
        
        # ans = "NO"
        if a.is_integer() and b.is_integer() and c.is_integer() and a >= 0 and b >= 0 and c >= 0:
            # print("YES")
            a, b, c = int(a), int(b), int(c)
            # a is dist from 1 to center, etc.
            # print(a, b, c)
            if [a,b,c].count(0) == 2 or [a,b,c].count(0) == 3:
                print("NO")
            elif n == 3:
                print("HELL")
            else:
                print("YES")
                root = 4

                for ind, join in enumerate([a,b,c]):
                    if join == 0:
                        root = ind + 1
                        break
                else:
                    avail_nodes.pop(0)
                # print(a, b, c)
                for ind, join in enumerate([a, b, c]): # take the distances
                    if join == 0:
                        pass
                    else:
                        temp = root
                        # print('trying', ind+1)
                        for ii in range(join - 1):
                            if not avail_nodes:
                                pass
                            else:
                                connect = avail_nodes.pop(0)
                                print(temp, connect)
                                temp = connect
                        print(temp, ind+1)
                while avail_nodes:
                    print(avail_nodes.pop(0), root)
                                            

            
        else:
            print("NO")






        

if __name__ == "__main__":
    solution()
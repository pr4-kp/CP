import sys
sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")

def solution():
    ans = 0
    road = input()
    for ii in range(26):
        for jj in range(26):
            if ii != jj:
                visited = 0
                visited2 = 0
                for cow in road:
                    if cow == chr(ii+65):
                        visited += 1
                        if visited == 1:
                            visited2 = 0
                    elif cow == chr(jj+65):
                        visited2 += 1
                    
                    if visited == 2:
                        if visited2 == 1:
                            # print(chr(ii+65), chr(jj+65))
                            ans += 1
                        break
    print(ans//2)


    
if __name__ == "__main__":
    solution()
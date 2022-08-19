import sys
input = sys.stdin.readline
inf = float('inf')

def solution():
    for _ in range(int(input())):
        n, s = map(int, input().split())
        A = list(map(int, input().split()))
        one_positions = []

        for ii in range(n):
            if A[ii] == 1:
                one_positions.append(ii)
        
        if s > len(one_positions):
            print(-1)
        elif s == len(one_positions):
            print(0)
        else:
            temp_right = n
            temp_left = -1
            ans = 0 
            # print(one_positions)
            current_ones = len(one_positions)
            while s != current_ones:
                if one_positions[0] - temp_left <= temp_right - one_positions[-1]:
                    rem = one_positions.pop(0)
                    # print("removed", rem)
                    if rem == temp_left + 1:
                        ans += 1
                    else:
                        ans += rem - temp_left
                    temp_left = rem
                    current_ones -= 1
                else:
                    
                    rem = one_positions.pop(-1)
                    # print("removed", rem)
                    if rem == temp_right - 1:
                        ans += 1
                    else:
                        ans += temp_right - rem
                    temp_right = rem
                    current_ones -= 1
                # print("ans", ans) # ans
            print(ans)



if __name__ == "__main__":
    solution()
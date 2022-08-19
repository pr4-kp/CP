inf = float('inf')
def solution():
    for _ in range(int(input())):
        h, c, t = map(int, input().split())
        if t == h:
            print(1)
        elif t <= (h + c) / 2:
            print(2)
        else:
            left = 0
            right = 10 ** 9
            # diff = inf


            # i + 1 cups hot water, i cups mcold water
            find = lambda i: ((i + 1) * h + i * c) / (2 * i + 1)

            while left < right:
                mid = left + (right - left) // 2
                if find(mid) == t:
                    break
                elif find(mid) > t:
                    left = mid
                else:
                    right = mid - 1
                # print(mid, find(mid))
            
            print(2 * mid + 1)
                



if __name__ == "__main__":
    solution()
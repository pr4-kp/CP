inf = float('inf')

def two_pointers(pkList, n):
    left = 0
    right = 0
    ans = inf
    # desired amount of pokemon to get
    des = len(set(pkList)) 
    seen = {pkList[0]}

    while left < n and right < n:
        while right < n and right >= left:
            
            if pkList[right] not in seen:
                seen.add(pkList[right])
            
            if len(seen) == des:
                ans = min(ans, right-left + 1)
                # print("stopped pointers at", left, right)
                break
            right += 1
            # print("pointers at", left, right)
        if pkList[left] not in pkList[min(left+1, n-1):right]:
            try: seen.remove(pkList[left]) 
            except: pass
        left += 1
    return ans

def solution():
    n = int(input())
    pkList = input()

    print(two_pointers(pkList, n))


if __name__ == "__main__":
    solution()
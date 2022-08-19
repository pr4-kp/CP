def two_pointers(n, t, books):
    left = 0
    right = 0
    ans = 0
    c = 0
    while left < n and right < n:
        while right < n:
            c += books[right]
            right += 1

            if c > t:
                right -= 1
                c -= books[right]
                break

        ans = max(ans, right-left)
        c -= books[left]
        left += 1
    print(ans)

def solution():
    
    n, t = map(int, input().split())
    books = list(map(int, input().split()))

    two_pointers(n, t, books)
    



if __name__ == "__main__":
    solution()
def solution():
    n = int(input())
    if (len(str(n)) == 1):
        print(n - 1)
        return
    
    x = len(str(n-1))

    if n < 2 * 10 ** (x-1): # even number of digits
        n -= 10 ** (x-2)
        ans = list(str(n)) + list(reversed(str(n)))
    else: 
        n -= 10 ** (x-1)
        ans = list(str(n)) + list(reversed(str(n)[:-1]))


    print(*ans, sep="")


if __name__ == "__main__":
    solution()
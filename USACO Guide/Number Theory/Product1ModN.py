import sys
input = sys.stdin.readline
inf = float('inf')

"""
--- Notes --- 
(n - 1)! % n == n - 1
start at the beginning, we can always include 1
if gcd(n, ii) != 1 that means that the product will never be 1
proof: ii * k, for k \in \ZZ will be a multiple of ii, which cannot be 1
so we can discard anything that is not relatively prime to n
can we just stop when the product is 1?
suppose that we could continue, then the sum, 1 % n gets multiplied by some number
therefore the number == k % n


"""

def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)

def solution():
    n = int(input())
    if n == 2:
        print(1)
        print(1)
    else:
        t = 1
        ans = [1]
        for ii in range(2, n):
            if gcd(n, ii) == 1:
                ans.append(ii)
                t *= ii
                t %= n
        if t != 1:
            ans.remove(t)
        print(len(ans))
        print(*ans)



if __name__ == "__main__":
    solution()
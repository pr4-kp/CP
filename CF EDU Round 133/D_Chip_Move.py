import sys
input = sys.stdin.readline

mod = 998244353

n, k = map(int, input().split())

ANS = [0]*(n+1)
DP = [0]*(n+1)
DP[0] = 1

f = 0

for i in range(k, n+1):
    f += i
    if f > n:
        break
    S = [0]*(n+1)
    for j in range(i, n+1):
        S[j] = (DP[j-i]+S[j-i]) % mod
        ANS[j] += S[j]
        ANS[j] %= mod
    DP = S

# print(*S)
# print(*DP)

print(*ANS[1:])

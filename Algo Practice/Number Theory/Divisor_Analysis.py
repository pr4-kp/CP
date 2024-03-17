MOD = 10 ** 9 + 7

def ext_euclid(a, b):
    x_arr = [1, 0, a]
    y_arr = [0, 1, b]
    q = -1

    while y_arr[2] > 0:
        q = x_arr[2] // y_arr[2]
        for i in range(3):
            x_arr[i] -= y_arr[i] * q
        x_arr, y_arr = y_arr, x_arr

    return x_arr

def mod_inverse(a: int, b: int) -> int:
    """@return the modular inverse of a modulo b."""
    arr = ext_euclid(a, b)
    assert arr[2] == 1 # GCD must be 1
    return arr[0] + (arr[0] < 0) * b

div_cnt = 1
div_sum = 1
div_prod = 1
div_cnt2 = 1   # number of divisors mod MOD - 1 for c

for _ in range(int(input())):
    p, x = map(int, input().split())
    div_cnt = div_cnt * (x + 1) % MOD
    div_sum = div_sum * (pow(p, x + 1, MOD) - 1) * mod_inverse(p - 1, MOD) % MOD
    div_prod = pow(div_prod, x + 1, MOD) * \
        pow(pow(p, x * (x + 1) // 2, MOD), div_cnt2, MOD) % MOD
    div_cnt2 = div_cnt2 * (x + 1) % (MOD - 1)

print(div_cnt, div_sum, div_prod)
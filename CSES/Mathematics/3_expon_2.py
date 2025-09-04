MOD = 10**9 + 7

def modpow(a, b, mod=MOD):
    """Binary exponentiation: compute a^b % mod efficiently."""
    result = 1
    a %= mod
    while b > 0:
        if b & 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b >>= 1
    return result

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())

    # Edge cases for a = 0
    if a == 0:
        if b == 0:
            if c == 0:
                print(0)
            else:
                print(1)
        else:
            print(0)  # 0^(b^c) = 0 if b^c > 0
    else:
        # Step 1: compute exponent modulo MOD-1
        exp = modpow(b, c, MOD - 1)

        # Step 2: if exponent is 0 but b^c > 0, set exp = MOD-1
        if exp == 0 and (b != 0 or c != 0):
            exp = MOD - 1

        # Step 3: compute final answer a^exp % MOD
        print(modpow(a, exp, MOD))

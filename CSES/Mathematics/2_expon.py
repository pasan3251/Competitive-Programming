MOD = 10**9 + 7

def modpow(a, b, mod=MOD):
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
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        print(1)  # by problem statement
    else:
        print(modpow(a, b))

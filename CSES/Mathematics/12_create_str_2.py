MOD = 10**9 + 7

def modpow(a, b, mod):
    res = 1
    while b:
        if b & 1:                # if the lowest bit of b is 1 (i.e., b is odd)
            res = res * a % mod  # multiply res by current base a
        a = a * a % mod          # square the base
        b >>= 1                  # shift b right (divide by 2)
    return res

s = input().strip()
n = len(s)

# frequency count
from collections import Counter
freq = Counter(s)

# precompute factorials
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % MOD

# precompute inverse factorials
invfact = [1] * (n + 1)
invfact[n] = modpow(fact[n], MOD - 2, MOD)
for i in range(n, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

# compute answer
ans = fact[n]
for c in freq.values():
    ans = ans * invfact[c] % MOD

print(ans)

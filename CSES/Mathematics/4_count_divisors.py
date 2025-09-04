n = int(input())

def num_divisors(x):
    ret = 1
    p = 2
    while p * p <= x:
        exp = 0
        while x % p == 0:
            x //= p
            exp += 1
        ret *= (exp + 1)
        p += 1
    if x > 1:
        ret *= 2
    return ret

for _ in range(n):
    x = int(input())
    print(num_divisors(x))
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

def sum_divisors(n):
    sum = 1
    p = 2
    
    while p <= n // 2:
        if n % p == 0:
            sum += p
        p += 1
    if n > 1:   
        sum += n
    
    return sum

def mul_divisors(n):
    mul = 1
    p = 2
    
    while p <= n // 2:
        if n % p == 0:
            mul *= p
        p += 1
    if n > 1:   
        mul *= n
    
    return mul


num = 1

for _ in range(n):
    x, k = map(int, input().split())
    
    num *= x**k
    
print(num_divisors(num) % (10**9 + 7), sum_divisors(num) % (10**9 + 7), mul_divisors(num) % (10**9 + 7))
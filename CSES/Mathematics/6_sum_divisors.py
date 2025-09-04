n = int(input())

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


get_sum = 0

for i in range(1, n+1):
    get_sum += sum_divisors(i)
    
print(get_sum % (10**9 + 7))
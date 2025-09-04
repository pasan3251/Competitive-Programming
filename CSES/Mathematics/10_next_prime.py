import math

n = int(input())

is_prime = [False, False, True]  # 0 and 1 are not prime 2 is a prime


primes = [2]


def get_primes(limit):
    """Generate list of primes up to 'limit' using Sieve of Eratosthenes."""
    len_is_prime = len(is_prime)
    if limit < len_is_prime:
        return primes
    
    # extend boolean array
    is_prime.extend([True] * (limit + 1 - len_is_prime))
    
    # seive from where we left off
    for num in range(len_is_prime, limit + 1):
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime[num - 1] = False
                break
            
        if is_prime[num]:
            primes.append(num)

                
    return primes


for _ in range(n):
    t = int(input())
    
    
    while 1:
        
        t+=1
        
        get_primes(t)
        
        if is_prime[t - 1]:
            break
        
    print(t)
    
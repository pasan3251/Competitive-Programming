n, k = map(int, input().split())

primes = list(map(int, input().split()))


        
num_list = [0] * (n + 1)        

for prime in primes:
    for i in range(prime, n + 1, prime):
        num_list[i] = 1
        
print(sum(num_list))


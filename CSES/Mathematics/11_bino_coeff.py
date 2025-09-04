import math

n = int(input())

for _ in range(n):
    
    a, b = map(int, input().split())
    
    a_fac = math.factorial(a)
    b_fac = math.factorial(b)
    a_sub_b_fac = math.factorial(a-b)
    
    result = int((a_fac / (b_fac * a_sub_b_fac)) % (10**9 + 7))
    
    print(result)
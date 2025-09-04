n = int(input())

def GCD(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a

a = list(map(int, input().split()))

gcd = 1

for i in range(n - 1):
    
    for j in range(i + 1, n):
        gcd_temp = GCD(a[i], a[j])
        if gcd_temp > gcd:
            gcd = gcd_temp

print(gcd)
n = int(input())

numbers = list(map(int, input().split()))

def GCD(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a

coprimes = 0

for num1 in range(n - 1):
    for num2 in range(num1 + 1, n):
        if GCD(numbers[num1], numbers[num2]) == 1:
            coprimes += 1
            
            
print(coprimes)
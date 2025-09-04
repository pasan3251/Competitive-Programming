from decimal import Decimal, getcontext

getcontext().prec = 30  # increase precision

n = int(input())
r = list(map(int, input().split()))

ans = Decimal(0)

for a in range(n):
    for b in range(a + 1, n):
        r_a, r_b = Decimal(r[a]), Decimal(r[b])

        if r_a <= r_b:
            ans += (r_a - 1) / (2 * r_b)
        else:
            ans += 1 - (r_b + 1) / (2 * r_a)

print(f"{ans:.6f}")

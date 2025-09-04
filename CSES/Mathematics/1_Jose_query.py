def josephus(n, k):
    if n == 1:
        return 1
    if k <= (n + 1) // 2:
        if 2 * k > n:
            return (2 * k) % n
        return 2 * k
    find =  josephus(n // 2, k - (n + 1) // 2)
    
    if (n & 1) > 0:
        # odd
        return 2 * find + 1
    return 2 * find - 1


q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    print(josephus(n, k))

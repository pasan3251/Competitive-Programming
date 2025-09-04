# construct adjacency matrix (A)    n x n
# get number of paths with length k :   A**k [0][n-1] (mod (10**9 + 7))

MOD = 10**9 + 7

def matmul(A, B, n):
    """Multiply two n x n matrices modulo MOD."""
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] == 0: 
                continue
            for j in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def matpow(A, k, n):
    """Fast exponentiation of matrix A to power k."""
    # Identity matrix
    res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while k > 0:
        if k & 1:
            res = matmul(res, A, n)
        A = matmul(A, A, n)
        k >>= 1
    return res


# --------------------------------------------------------------

n, m, k = map(int, input().split())

# adjacency matrix
A = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    A[a-1][b-1] += 1

Ak = matpow(A, k, n)

print(Ak[0][n-1] % MOD)


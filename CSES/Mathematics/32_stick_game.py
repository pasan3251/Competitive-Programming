num_sticks, num_moves = map(int, input().split())

posible_moves = list(map(int, input().split()))

dp = [False] * (num_sticks + 1)
dp[0] = False  # losing position


for stick in range(1, num_sticks + 1):
    for move in posible_moves:
        if stick - move >= 0 and not dp[stick - move]:
            dp[stick] = True
            break
    

result = ''.join('W' if dp[i] else 'L' for i in range(1, num_sticks + 1))

print(result)

t = int(input())

for _ in range(t):
    n = int(input())
    
    heaps = list(map(int, input().split()))
    
    
    nim_sum = 0
    
    for h in heaps:
        nim_sum ^= h    # xor all heaps
    
    print("first" if nim_sum else "second")
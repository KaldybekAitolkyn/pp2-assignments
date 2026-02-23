def powers_of_two(n):
    p = 1        
    for _ in range(n + 1):
        yield p
        p *= 2    
n = int(input())
print(*powers_of_two(n))
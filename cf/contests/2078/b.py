t = int(input()) 

for _ in range(t): 
    n, k = map(int, input().split())

    if k % 2 == 0: 
        nums = [n-1 for i in range(n)] 
        nums[-2] = n  
    else: 
        nums = [n for i in range(n)] 
        nums[-1] = n-1  
    
    print(*nums) 

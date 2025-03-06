t = int(input()) 

for _ in range(t): 
    n = int(input()) 
    arr = input().split() 
    mn = float("inf")
    idx = -1 

    for i in range(n): 
        num = int(arr[i])
        if num < mn: 
            mn = num 
            idx = i 
    
    time_needed = max(n-1-idx, idx) * 2 
    if time_needed >= mn: 
        print("NO") 
    else: 
        print("YES") 
    

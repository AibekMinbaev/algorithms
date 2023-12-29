for _ in range(int(input())): 
    n = int(input()) 
    arr = list(map(int, input().split())) 

    d = {0:1} 
    sm = 0 
    res = "NO"

    for i in range(n): 
        if i % 2 == 0: 
            sm += arr[i] 
        else: 
            sm -= arr[i] 
        
        if sm in d: 
            res = "YES" 
            break 
        d[sm] = 1 

    print(res)
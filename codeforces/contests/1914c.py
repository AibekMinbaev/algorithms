for _ in range(int(input())): 
    n, k = list(map(int, input().split())) 

    a = list(map(int, input().split())) 
    b = list(map(int, input().split())) 

    res = a[0] 
    mx = b[0] 

    k -= 1 

    for i in range(1, n): 
        if k > 0: 
            if mx * k <= a[i] + mx * (k-1): 
                res += a[i]
                mx = max(mx, b[i]) 
                k -= 1 
            else: 
                res += k * mx 
                k = 0 
                break  
        else: 
            break 
    
    if k: 
        res += mx * k 
    print(res) 
    


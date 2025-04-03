t = int(input()) 

for _ in range(t): 
    n, k, x = map(int, input().split()) 
    arr = list(map(int, input().split())) 
    sm = sum(arr) * k 
    
    if sm < x: 
        print(0) 
    else: 
        arr = arr[::-1]
        a = x // sum(arr)
        b = x % sum(arr) 
        
        if b == 0: 
            a = max(0, a - 1) 
            b = x - sum(arr) * a 

        res = (n * k) - (n * a) 
        
        cnt = 0 
        for i in range(n): 
            if cnt + arr[i] >= b: 
                print(res - i ) 
                break 
            cnt += arr[i]   
        
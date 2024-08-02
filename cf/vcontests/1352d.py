for _ in range(int(input())): 
    n = int(input()) 
    arr = list(map(int, input().split())) 

    l = 0
    r = len(arr) - 1 

    cnt = 1 
    cur = arr[l] 
    l = 1 
    a, b = 0, 0 
    a += cur 

    while l <= r: 
        
        if cur >= 0 and l <= r : 
            cnt += 1 
            temp = 0 
            
            while cur >= 0 and l <= r: 
                cur -= arr[r]
                temp += arr[r] 
                b += arr[r] 
                r -= 1 
            
            cur = temp 
        
        if cur >= 0 and l <= r : 
            cnt += 1 
            temp = 0 
            while cur >= 0 and l <= r: 
                cur -= arr[l] 
                temp += arr[l] 
                a += arr[l]
                l += 1 
            
            cur = temp  
    print(cnt, a, b) 


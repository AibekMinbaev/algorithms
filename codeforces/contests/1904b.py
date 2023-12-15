for _ in range(int(input())): 
    n = int(input())  
    input_arr = list(map(int, input().split())) 
    arr = sorted(input_arr) 
    
    pref_sum = [] 
    sm = 0 
    for num in arr: 
        sm += num 
        pref_sum.append(sm) 
    
    d = {} 
    ans = n - 1
    for i in range(n-1, -1, -1): 
        if arr[i] not in d:
            d[arr[i]] = ans
            if i > 0 and pref_sum[i-1] < arr[i]: 
                ans = i - 1
            
    for elem in input_arr: 
        print(d[elem]) 
    

    
     


      # d = {}
    # for i in range(len(arr)-1, -1, -1): 
    #     target = pref_sum[i] 
    
    #     l, r = 0, len(arr) - 1 

    #     while l <= r: 
    #         m = (l + r) // 2 

    #         if arr[m] <= target: 
    #             d[arr[i]] = m 
    #             l = m + 1
    #         else: 
    #             r = m - 1 
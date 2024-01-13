for _ in range(int(input())): 
    n, k, x = map(int, input().split()) 
    arr = list(map(int, input().split())) 

    arr.sort(reverse=True) 
    bob = sum(arr[:x]) * -1
    temp_arr = [bob]

    l, r = 1, x 
    while l <= n and r <= n: 
        if r != n: 
            bob += arr[l-1] 
            bob += -arr[r] 
            temp_arr.append(bob)
            l += 1 
            r += 1 
        else: 
            # print("HI")
            bob += arr[l-1]
            temp_arr.append(bob) 
            l += 1 

    
    # print(temp_arr)
    sm = sum(arr) 
    cnt = 0 
    res = float('-inf') 
    for i in range(min(len(temp_arr), k+1)): 
        res = max(res, sm - cnt + temp_arr[i] * 2) 
        if i < len(arr): 
            cnt += arr[i] 
    
    print(res) 

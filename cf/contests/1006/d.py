t = int(input()) 


for _ in range(t): 
    n = int(input()) 
    arr = list(map(int, input().split())) 

    mx_cnt = 0 

    l, r = 0, 0 
    for i in range(n): 
        cnt = 0 
        
        for j in range(i+1, n): 
            if arr[i] > arr[j]: 
                cnt += 1 
            elif arr[i] < arr[j]: 
                cnt -= 1 

            if cnt > mx_cnt: 
                mx_cnt = cnt 
                l, r = i, j 
    print(l+1, r+1) 


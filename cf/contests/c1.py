t = int(input()) 

for _ in range(t): 
    n = int(input()) 
    nums = list(map(int, input().split())) 


    one_arr = [0] * n 
    three_arr = [0] * n 

    one = 0 
    for i in range(n): 
        if nums[i] == 2: 
            one_arr[i] = one 
        elif nums[i] == 1: 
            one += 1 
    
    three = 0 
    for i in range(n-1, -1, -1): 
        if nums[i] == 2: 
            three_arr[i] = three 
        elif nums[i] == 3: 
            three += 1 
    
    tmp = [] 
    for i in range(n): 
        if nums[i] == 2: 
            ones = one_arr[i] 
            threes = three_arr[i] 
            if ones > 0 and threes > 0: 
                tmp.append((ones, threes)) 
    
    cnt = 0 
    for i in range(len(tmp)): 
        for j in range(i, len(tmp)): 
            cnt += tmp[i][0] * tmp[j][1]
            print(cnt)  
    
    print(tmp) 
    print(cnt) 


2 2 2 2 2 
  
0,0 
1,1 > 0,1  
2,2 > 0,2; 1,2; 0,2
s = input() 

if len(s) == 1: 
    print(1) 
else: 
    res = 1 
    cnt = 1 
    for i in range(1, len(s)): 
        if s[i-1] == s[i]: 
            cnt += 1 
        else: 
            cnt = 1 
        
        if cnt > res: 
            res = cnt 
        
    print(res) 
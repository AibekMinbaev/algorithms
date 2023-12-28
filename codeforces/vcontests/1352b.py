for _ in range(int(input())): 
    n, k = map(int, input().split())  

    ans = False
    res = [] 

    temp1 = (n - (k - 1))
    temp = (n - 2 * (k - 1))

    if  temp1 > 0 and temp1 % 2 != 0: 
        ans = True 
        for i in range(k - 1): 
            res.append(1) 
        res.append(temp1) 

    if not ans: 
        if  temp > 0 and temp % 2 == 0: 
            ans = True 
            for i in range(k - 1): 
                res.append(2) 
            res.append(temp)
    
    if not ans: 
        print("NO")  
    else: 
        print("YES") 
        for elem in res: 
            print(elem) 
        
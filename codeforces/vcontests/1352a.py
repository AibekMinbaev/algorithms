for _ in range(int(input())): 
    n = input()
    res = []  
    cnt = 1 
    for  i in range(len(n) - 1, -1, -1): 
        if n[i] != "0": 
            res.append(int(n[i]) * cnt)  
        cnt *= 10 

    print(len(res)) 
    for elem in res: 
        print(elem) 
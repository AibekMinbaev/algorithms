for _ in range(int(input())): 
    cor = [] 
    cur = None 
    for i in range(4): 
        x, y = map(int, input().split()) 
        cor.append((x,y)) 
    
    for elem in cor: 
        if cur == None: 
            cur = elem
        else: 
            if elem[0] == cur[0]: 
                print(abs(cur[1] - elem[1]) ** 2) 
    


    
    

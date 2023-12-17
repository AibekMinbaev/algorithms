for _ in range(int(input())): 
    ab = input() 
    a = "" 
    b = "" 

    for i in range(len(ab)): 
        a += ab[i] 
        if i < len(ab) - 1: 
            if ab[i+1] != "0": 
                b = ab[i+1:]
                break 
    
    if len(a) > 0 and len(b) > 0: 
        a = int(a) 
        b = int(b)

        if a >= b or a == 0 or b == 0: 
            print(-1) 
        else: 
            print(a, b) 
    else: 
        print(-1) 

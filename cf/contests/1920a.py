for _ in range(int(input())): 
    n = int(input()) 

    one = 1 
    two = float("inf") 
    arr = [] 

    for i in range(n): 
        a, x = map(int, input().split()) 

        if a == 1: 
            one = max(one, x) 
        elif a == 2: 
            two = min(two, x) 
        else: 
            arr.append(x) 
    
    cnt = 0 
    for elem in arr: 
        if elem >= one and elem <= two: 
            cnt += 1 
    
    print(max(0, two - one - cnt + 1))


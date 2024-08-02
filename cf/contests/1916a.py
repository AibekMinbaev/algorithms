for _ in range(int(input())): 
    n, k = map(int, input().split()) 

    barr = list(map(int, input().split())) 

    sm = 1 
    for elem in barr:
        sm *= elem 
    
    if (2023 / sm) % 1 == float(0): 
        print("YES") 
        print(2023 // sm) 
        for i in range(k-1): 
            print(1) 
    else: 
        print("NO")  
        
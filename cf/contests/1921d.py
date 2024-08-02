for _ in range(int(input())): 
    n, m = map(int, input().split()) 
    a = list(map(int, input().split())) 
    b = list(map(int, input().split()))  

    a.sort() 
    b.sort(reverse=True) 
    mid = n // 2  
    dif = m - n 

    r1 = 0 
    for i in range(mid): 
        r1 += abs(a[i] - b[i])  
    
    for i in range(mid + dif, m): 
        r1 += abs(a[i - dif] - b[i]) 

    mid2 = n // 2 + 1 
    r2 = 0 
    for i in range(mid2): 
        r2 += abs(a[i] - b[i])  
    
    for i in range(mid2 + dif, m): 
        r2 += abs(a[i - dif] - b[i]) 

    print(max(r1, r2)) 

    
    



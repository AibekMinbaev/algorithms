for _ in range(int(input())): 
    n = int(input()) 

    a1 = list(map(int, input().split())) 
    a2 = list(map(int, input().split())) 
    a3 = list(map(int, input().split())) 

    arr1 = [] 
    arr2 = [] 
    arr3 = [] 
    for i in range(n): 
        arr1.append((a1[i], i)) 
        arr2.append((a2[i], i)) 
        arr3.append((a3[i], i)) 
    
    arr1 = sorted(arr1, key=lambda x: x[0], reverse= True ) 
    arr2 = sorted(arr2, key=lambda x: x[0], reverse= True) 
    arr3 = sorted(arr3, key=lambda x: x[0], reverse= True) 
    
    cnt = 0 
    for i in range(3): 
        for j in range(3): 
            for k in range(3): 
                t1 = arr1[i][1] 
                t2 = arr2[j][1] 
                t3 = arr3[k][1] 

                if t1 != t2 and t1 != t3 and t2 != t3: 
                    cnt = max((arr1[i][0] + arr2[j][0] + arr3[k][0]), cnt )
    print(cnt) 
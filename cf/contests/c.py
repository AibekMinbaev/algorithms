t = int(input()) 

for _ in range(t): 
    n = int(input()) 
    arr = [int(i) for i in input().split()] 
    res = sum(arr) 

    while len(arr) > 1: 
        arr1 = []
        sm1 = 0 
        arr2 = [] 
        sm2 = 0 

        for i in range(1, len(arr)): 

            f, s = arr[i-1], arr[i] 
            arr1.append(s-f) 
            sm1 += s-f
            arr2.append(f-s) 
            sm2 += f-s 

        if sm1 > sm2: 
            arr = arr1 
        else: 
            arr = arr2 
        res = max(res, sm1, sm2) 
    print(res) 
             

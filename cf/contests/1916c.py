for _ in range(int(input())): 
    n = int(input()) 
    arr = list(map(int, input().split())) 

    sm1 = arr[0]
    sm2 = arr[0]
    print(arr[0])
    for i in range(1, len(arr)): 
        sm1 += arr[i] 
        sm2 += arr[i] 

        if sm1 % 2 != 0: 
            sm1 -= 1 

        res = (sm1 + sm2) // 2 
        print(res) 
        if res % 2 != 0: 
            print(res - 1) 
        else: 
            print(res) 
        
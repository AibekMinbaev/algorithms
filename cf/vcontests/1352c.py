for _ in range(int(input())): 
    n, k = map(int, input().split())  

    l = 1
    r = 10 ** 18

    while l <= r:  
        m = (l + r) // 2 

        temp = m // n 
        left = m % n 
        t = m 

        if left == 0: 
            m += 1 
        if m - temp == k: 
            print(m) 
            break 
        elif m - temp < k:
            l = t + 1 
        else: 
            r = t - 1 
        



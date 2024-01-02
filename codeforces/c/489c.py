m, s = map(int, input().split()) 

a = s // 9 
b = s % 9  

mx = "" 
temp = a + (1 if b else 0) 
if temp > m or (s == 0 and m != 1): 
    print(-1, -1)  
else: 
    dif = m - temp 
    h = a * 9 + b 
    if (h - dif) < 0: 
        print(-1, -1) 

    else: 
        w = (h - dif) // 9 
        wl = (h - dif) % 9 

        for i in range(w): 
            mx += "9" 
        
        if wl != 0: 
            mx += str(wl)  
        
        for i in range(dif): 
            mx += "1"
        
        if mx: 
            print(int(mx[:][::-1]), int(mx)) 
        else: 
            print(0, 0)
        
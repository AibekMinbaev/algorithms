t = int(input()) 

for _ in range(t): 
    n = int(input()) 
    s = input() 
    cnt_1 = 0 
    cnt_2 = 0 
    for char in s: 
        if char == "-": 
            cnt_1 += 1 
        else: 
            cnt_2 += 1 
    
    a = cnt_1 // 2 
    b = a + (1 if cnt_1 % 2 > 0 else 0) 
    print(a * cnt_2 * b) 
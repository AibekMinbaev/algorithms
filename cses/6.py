t = int(input()) 

for _ in range(t): 
    y, x = map(int, input().split()) 

    mx = max(y,x) 

    diag = mx * mx - (mx - 1) 

    if y > x: 
        if y % 2 == 0: 
            print(diag + y - x)
        else: 
            print(diag - y -x)
    elif y < x: 
        if y % 2 == 0: 
            print(diag + x - y) 
        else: 
            print(diag - x - y) 
    else: 
        print(diag) 
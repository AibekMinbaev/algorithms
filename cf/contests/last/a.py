t = int(input()) 

for _ in range(t): 
    abc = list(map(int, input().split())) 

    abc.sort() 

    mx = abc[2]

    dif1 = mx - abc[1] + 1 
    dif2 = mx - abc[0] + 1 

    if (5 - dif2) > 0: 
        if (5 - dif2 - dif1) > 0: 
            temp = 5 - dif2 - dif1 
            abc[1] += dif1 
            abc[0] += dif2 
            abc.sort() 

            abc[0] += 1 
            temp -= 1 
            if temp: 
                abc[1] += 1 
                temp -= 1 
            if temp: 
                abc[2] += 1 
            
            print(abc[0] * abc[1] * abc[2]) 

        else: 
            print(mx * (abc[1] + 5 - dif2) * (abc[0] + dif2))


    else: 
        print(mx * abc[1] * (abc[0] + 5))


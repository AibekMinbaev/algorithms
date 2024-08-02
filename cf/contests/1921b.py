for _ in range(int(input())): 
    n = int(input()) 
    a = input() 
    f = input() 

    cnt = 0 
    ones = [] 
    zeros = [] 
    for i in range(n): 
        if a[i] != f[i]: 
            if f[i] == "0": 
                if not ones: 
                    zeros.append(0) 
                else: 
                    cnt += 1 
                    ones.pop() 
            else:
                if not zeros:  
                    ones.append(1) 
                else: 
                    cnt += 1 
                    zeros.pop()  
    print(cnt + len(ones) + len(zeros)) 

            
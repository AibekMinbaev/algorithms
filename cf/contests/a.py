t = int(input()) 

for _ in range(t): 
    s = input() 
    res = 0 
    for char in s: 
        if char == "1": 
            res += 1 
    print(res) 
    
from collections import Counter 

for _ in range(int(input())): 
    s = input() 
    d = Counter(s) 

    res = 0 
    for i in range(len(s)): 
        if s[i] == "0": 
            if d["1"] == 0: 
                res = len(s) - i
                break 
            else: 
                d["1"] -= 1  
        else: 
            if d["0"] == 0: 
                res = len(s) - i
                break 
            else: 
                d["0"] -= 1 
    print(res) 
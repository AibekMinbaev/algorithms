from collections import Counter 

for _ in range(int(input())): 
    s = input() 
    d = Counter(s) 
    res = 0
    for i in range(len(s)): 
        if d[str(1 - int(s[i]))] == 0: 
            res = len(s) - i
            break 
        d[str(1 - int(s[i]))] -= 1 
    print(res)  


s = input().split("WUB") 

res = "" 
for i in range(len(s)): 
    if s[i] != "": 
        res += s[i] 
        if i != len(s) - 1: 
            res += " " 

print(res) 
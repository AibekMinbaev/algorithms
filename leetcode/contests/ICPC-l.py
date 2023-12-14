import collections 

n = int(input()) 
s = input() 

d = collections.Counter(s) 

bread = 0 
onion = 0 

res = -1 
for i in range(len(s)): 
    if s[i] == "L": 
        d["L"] -= 1 
        bread += 1 
    else: 
        d["O"] -= 1   
        onion += 1 
    
    if bread + onion > 0 and d["L"] + d["O"] > 0: 
        if bread != d["L"] and onion != d["O"]: 
            res = i + 1
            break
print(res)  




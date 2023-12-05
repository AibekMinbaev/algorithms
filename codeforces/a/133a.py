t = input() 

commands = set("HQ9") 

res = "NO"
for ch in t: 
    if ch in commands: 
        res = "YES" 
print(res) 

s = input() 
res = "" 
for ch in s: 
    if ch.lower() not in ["a", "o", "y", "e", "u", "i"]: 
        res += "." + ch.lower() 
print(res) 
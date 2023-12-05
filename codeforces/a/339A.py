input_str = input().split("+")
s = [int(num) for num in input_str]
s.sort() 
res = "" 

for num in s: 
    res += str(num)  
    res += "+" 
print(res[:-1]) 


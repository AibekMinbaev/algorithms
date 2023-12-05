n = int(input()) 

res = 0

for i in range(n): 
    temp = [int(elem) for elem in input().split()] 
    if sum(temp) >= 2: 
        res += 1 

print(res) 



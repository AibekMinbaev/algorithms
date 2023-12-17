arr = []
s = set() 
d = {} 
for i in range(30): 
    d[i] = 2 ** i 


for _ in range(int(input())): 
    t, v = list(map(int, input().split())) 
    
    if t == 1: 
        for i in range(len(arr)): 
            arr.append(arr[i] + d[v])
            s.add(arr[i] + d[v])         
        
        arr.append(d[v])
        s.add(d[v])

    else: 
        if v in s: 
            print("YES") 
        else: 
            print("NO")  
# print(s) 
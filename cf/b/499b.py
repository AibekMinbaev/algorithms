n, m = map(int, input().split()) 

d = {} 
for _ in range(m):  
    w1, w2 = input().split() 
    d[w1] = w2   

arr = input().split() 
for elem in arr: 
    if len(elem) <= len(d[elem]): 
        print(elem) 
    else: 
        print(d[elem]) 

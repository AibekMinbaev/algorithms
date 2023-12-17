n = int(input()) 
res = [0 for i in range(n)] 
arr = list(map(int, input().split())) 

for i in range(n): 
    res[arr[i]-1] = i + 1 

for elem in res: 
    print(elem) 
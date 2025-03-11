t = int(input()) 

for _ in range(t): 
    n, x = map(int, input().split())    
    nums = list(map(int, input().split())) 

    res = sum(nums)/n == x

    if res: 
        print("YES") 
    else: 
        print("NO") 
    
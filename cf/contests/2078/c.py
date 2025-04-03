t = int(input()) 

for _ in range(t): 
    n = int(input()) 
    arr = list(map(int, input().split())) 
    arr.sort() 

    odd = sum(arr[-n+1:]) 
    even = sum(arr[:n-1]) 
    print(odd, even) 

    res = [odd-even] + arr 
    print(*res) 




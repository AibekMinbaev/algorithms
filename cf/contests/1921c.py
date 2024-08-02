for _ in range(int(input())): 
    n, f, a, b = map(int, input().split()) 
    arr = list(map(int, input().split())) 

    cnt = min(b, (arr[0] * a))
    for i in range(1, n): 
        cnt += min(b, (arr[i] - arr[i-1]) * a) 

    if cnt < f: 
        print("YES") 
    else: 
        print("NO") 


for _ in range(int(input())): 
    n, k = list(map(int, input().split())) 
    arr = [i for i in range(n, 0, -1)] 

    for i in range(n - (k + 1)): 
        print(arr[i])
        arr[i] = -1 

    ind = len(arr) - 1
    while arr[ind] != -1 and ind != -1: 
        print(arr[ind])
        ind -= 1 


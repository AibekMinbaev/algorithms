for _ in range(int(input())): 
    n, k = map(int, input().split()) 

    s = "" 
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(k): 
        s += alpha[i]
    
    res = ""
    for m in range(n): 
        res += s 
    print(res) 
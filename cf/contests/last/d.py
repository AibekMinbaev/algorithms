t = int(input().split()) 

for _ in range(t): 
    n, m, k = map(int, input().split()) 
    st = input()  # L W C 

    last_ind = n 

    for i in range(n-1, -1, -1): 
        if st[i] == "L": 
            if last_ind - i <= m: 
                last_ind = i 

        elif st[i] == "W": 
            




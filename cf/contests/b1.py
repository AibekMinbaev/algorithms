t = int(input()) 

for _ in range(t): 
    n, m = map(int, input().split())  

    mat = [] 
    for r in range(n): 
        col = input().split() 
        mat.append(col) 
    
    mx = 1 
    d = {}  
    for i in range(n): 
        for j in range(m): 
            if mat[i][j] not in d: 
                d[mat[i][j]] = 1 
            if (i+1 < n and mat[i][j] == mat[i+1][j]) or (j+1 < m and mat[i][j] == mat[i][j+1]): 
                d[mat[i][j]] = 2 
                mx = 2
    
    print(sum(d.values()) - mx) 
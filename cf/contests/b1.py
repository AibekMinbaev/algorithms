t = int(input()) 

for _ in range(t): 
    n, m = map(int, input().split())  

    mat = [] 
    for r in range(n): 
        col = input().split() 
        mat.append(col)  
    

    d = {} 
    for r in range(n): 
        for c in range(m): 
            col = mat[r][c] 
            if col not in d: 
                d[col] = []  
            
            for sets in d[col]: 
                if (r,c) not in sets: 
                    sets.add((r-1,c)) 
                    sets.add((r+1, c)) 
                    sets.add((r,c-1)) 
                    sets.add((r,c+1)) 
                    break 
            else: 
                st = set() 
                st.add((r-1,c)) 
                st.add((r+1, c)) 
                st.add((r,c-1)) 
                st.add((r,c+1))  
                d[col].append(st) 
    
    res = 0 
    mx = 0 
    for k, v in d.items(): 
        res += len(v) 
        mx = max(mx, len(v)) 
    print(res - mx) 
    























# st1 = set() 
# st2 = set() 

# for r in range(n): 
#     for c in range(m):  
#         if (r+c) % 2 == 0: 
#             st1.add(mat[r][c]) 
#         else: 
#             st2.add(mat[r][c]) 

# res = len(st1) + len(st2) 
# mn_res = res

# for elem in st1: 
#     print(elem, res) 
#     if elem in st2: 
#         mn_res = min(mn_res, res - 2) 
#     else: 
#         mn_res = min(mn_res, res - 1) 

# print(mn_res) 
        





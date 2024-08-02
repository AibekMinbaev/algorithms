
def rec(st, s): 
    if s not in st and len(s) > 0: 
        st.add(s) 
        if len(s) > 1: 
            if len(s) == 2: 
                st.add(s[0]) 
                st.add(s[1]) 
            else: 
                rec(st, s[1:])
                rec(st, s[0] + s[2:]) 
    return 

for _ in range(int(input())): 
    n = int(input()) 
    s = input() 
    if s: 
        st = set()  
        rec(st, s)  

        print(len(st)) 


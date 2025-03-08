q = int(input()) 

st = [0] * 100 

for _ in range(q): 
    query = list(map(int, input().split())) 
    if query[0] == 1: 
        st.append(query[1]) 
    else: 
        print(st.pop()) 
    
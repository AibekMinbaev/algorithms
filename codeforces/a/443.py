s = input() 

st = set() 
for char in s: 
    if char.isalpha(): 
        st.add(char)  

print(len(st)) 

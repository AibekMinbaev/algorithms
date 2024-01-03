import math

n = int(input()) 
arr = list(map(int, input().split())) 

st = set() 
m = 10 ** 6 + 1
is_prime = [True for i in range(m + 1)] 
is_prime[0] = is_prime[1] = False  

for i in range(2, m+1): 
    if is_prime[i]: 
        st.add(i * i) 

    if is_prime[i] and i * i <= m:
        for j in range(i * i, m+1, i): 
            is_prime[j] = False 

for i in range(n): 
    if arr[i] in st: 
        print("YES") 
    else:
        print("NO") 


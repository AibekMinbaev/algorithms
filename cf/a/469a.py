n = int(input()) 
arr1 = list(map(int, input().split())) 
arr2 = list(map(int, input().split())) 

st = set() 

for elem in arr1[1:]: 
    st.add(elem) 
for elem in arr2[1:]: 
    st.add(elem) 

res = True 
for i in range(1, n+1): 
    if i not in st: 
        res = False 

if res: 
    print("I become the guy.")
else: 
    print("Oh, my keyboard!") 

# Method 1 - One loop
# n, m = map(int, input().split()) 
# a = list(map(int, input().split())) 
# b = list(map(int, input().split())) 

# i = j = 0 

# while j < m: 
#     if i < n and a[i] < b[j]: 
#         i += 1 
#     else: 
#         print(i) 
#         j += 1 

n, m = map(int, input().split()) 
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 

i = 0 
for j in range(m): 
    while i < n and a[i] < b[j]: 
        i += 1 
    print(i) 

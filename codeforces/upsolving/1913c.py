# Upsolved: 

cnt = [0 for i in range(30)] 
ans = [] 

for _ in range(int(input())): 
    t, v = list(map(int, input().split())) 

    if t == 1: 
        cnt[v] += 1 
    else: 
        pass 





for elem in ans: 
    if elem: 
        print("YES") 
    else: 
        print("NO") 




























# d = {} 
# for i in range(30): 
#     d[i] = 2 ** i 

# arr = [] 
# finres = [] 

# for _ in range(int(input())): 
#     t, v = list(map(int, input().split())) 
    
#     if t == 1: 
#         arr.append(d[v])
#     else: 
        
#         l, r = 0, len(arr) - 1 
#         res = 0 
#         while l <= r: 
#             m = (l + r) // 2 

#             if arr[m] == v: 
#                 res = 1 
#                 break 
#             elif arr[m] < v: 
#                 l = m + 1 
#             else:   
#                 r = m - 1 

#         if res == 0: 
#             ind = r
#             while v > 0 and ind > -1: 
#                 if arr[ind] <= v: 
#                     v -= arr[ind] 
#                 ind -= 1 
#             res = 1 if v == 0 else 0
#         # finres.append("YES" if res == 1 else "NO")
#         print("YES" if res == 1 else "NO")
# # print(arr)
# # print(finres) 


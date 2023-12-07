#Solution after upsolving 
#Time: m log elem  #because bin(n) in python is log n
#Space: 1 if we don't consider input arr   

t = list(map(int,input().split())) 
n = t[0] 
m = t[1] 
k = t[2] 

arr = [int(input()) for i in range(m)] 
fed = int(input()) 

res = 0 
for elem in arr: 
    xor_elem = bin(fed ^ elem) # returns the number after xoring, now we need to calculate the number of ones in this number 
    cnt = 0 
    for char in xor_elem: 
        if char == '1': 
            cnt += 1 
    if cnt <= k: 
        res += 1 

print(res) 




# #1st Solution 
# #Time: m log x
# #Space: 1 if don't calculate the input arr 
# #Topics: Merging

# t = list(map(int, input().split())) 
# n = t[0] 
# m = t[1] 
# k = t[2] 

# arr = [] 
# for i in range(m): 
#     arr.append(bin(int(input()))[2:][::-1]) 

# fed = bin(int(input()))[2:][::-1]
# res = 0 

# for elem in arr: 
#     cnt = 0 

#     i = 0 
#     while i < min(len(fed), len(elem)):
#         if fed[i] != elem[i]: 
#             cnt += 1 
#         i += 1 
    
#     while i < len(fed): 
#         if fed[i] == '1': 
#             cnt += 1 
#         i += 1 

#     while i < len(elem): 
#         if elem[i] == '1': 
#             cnt += 1 
#         i += 1 

#     if cnt <= k: 
#         res += 1 
# print(res) 
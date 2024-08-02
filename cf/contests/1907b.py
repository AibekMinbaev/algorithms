#Solution after upsolving: 
#Time: n 
#Space: n
#Topics: implementation 
# Notes: this approach is much easier then merging.  

for _ in range(int(input())): # new 
    s = input() 
    ans = [] 
    low = [] 
    up = [] 

    for ch in s: 
        if ch != 'b' and ch != 'B': 
            ans.append(ch) 

            if ch.islower(): 
                low.append(len(ans) - 1) # capturing the index of added char 
            else: 
                up.append(len(ans) - 1) # if the char is upper_case 
        
        elif ch == "b": 
            if low: 
                ind = low.pop() 
                ans[ind] = "" # new 
        elif ch == "B": 
            if up: 
                ind = up.pop() 
                ans[ind] = "" 

    print("".join(ans))
    
# # Solution during the contest
# # Time: n
# # Space: n
# # Topics: merging 

# def main(): 
#     s = input() 
#     ch_lower = [] 
#     ch_upper = [] 

#     for i in range(len(s)):
#         ch = s[i] 
#         if ch == 'b': 
#             if ch_lower:
#                 ch_lower.pop() 
#         elif ch == 'B': 
#             if ch_upper: 
#                 ch_upper.pop() 
#         else: 
#             if ch.islower(): 
#                 ch_lower.append((i, ch))
#             else: 
#                 ch_upper.append((i, ch))
    
#     res = ""
#     i = 0 
#     j = 0 
#     while i < len(ch_lower) and j < len(ch_upper): 
#         if ch_lower[i][0] < ch_upper[j][0]: 
#             res += ch_lower[i][1] 
#             i += 1 
#         else: 
#             res += ch_upper[j][1]
#             j += 1 

#     while i < len(ch_lower): 
#         res += ch_lower[i][1]
#         i += 1 

#     while j < len(ch_upper): 
#         res += ch_upper[j][1] 
#         j += 1 

#     print(res) 

# T = int(input()) 
# t = 1 
# while t <= T: 
#     main() 
#     t += 1 

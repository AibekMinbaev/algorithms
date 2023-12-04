# Solution after upsolving 
# Topics: binary search 
# Time: log n Space: 1 

def main(): 
    n, p, l, t = map(int, input().split()) 
    total_tasks = (n - 1) // 7 + 1 

    def helper(days):
        lessons_score = days * l 
        tasks_score = min(total_tasks, days * 2) * t 
        return lessons_score  + tasks_score >= p 


    left = 0 # Start from 0 because it might happend that student must study whole semester 
    right = n 
    while left < right: 
        mid = (left + right) // 2 
        if helper(mid) == False: # Score is not enough 
            left = mid + 1 
        else: 
            right = mid 

    return n - right 


T = int(input()) 
t = 1 
while t <= T: 
    print(main()) 
    t += 1 



# Solution during the contest: 
# Time: 1 S: 1 


# tc = int(input()) 

# for i in range(tc): 
#     arr = [int(elem) for elem in input().split()]
#     n, p, l, t = arr[0], arr[1], arr[2], arr[3] 
    
#     nt = n // 7 
#     if n % 7 != 0: 
#         nt += 1 

#     full_days = nt // 2 # for how many days we can solve by 2 tasks 
#     left_days = nt % 2 # additional tests 
    
#     full_score = 2 * t + l  # one day 
#     half_score = t + l

#     total_score = full_days * full_score
#     cnt = full_days

#     if total_score >= p: 
#         extra_score = total_score - p 
#         cnt -= extra_score // full_score
#     else: 
#         if left_days == 1: 
#             total_score += half_score 
#             cnt += 1 

#         if total_score < p: 
#             left_score = p - total_score 
#             cnt += left_score // l 
#             if left_score % l > 0: 
#                 cnt += 1 
    
#     res = n - cnt # Total number of day minus days of work 
#     print(res)  

n = int(input()) 
nums = list(map(int, input().split())) 

for i in range(2, n): 
    if nums[i-2] == nums[i-1] == nums[i]: 
        print("Yes") 
        break 
else: 
    print("No")
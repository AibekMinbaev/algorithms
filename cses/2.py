n = int(input()) 
s = map(int, input().split())

sum_n = (n * (n + 1)) // 2 
print(sum_n - sum(s))

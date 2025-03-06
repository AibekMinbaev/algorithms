
def solve(n,k,s,pen): 
    pass 


t = int(input()) 

for _ in range(t): 
    n, k = map(int, input().split()) 
    s = input() 
    pen = [int(elem) for elem in input().split()] 

    print(solve(n,k,s,pen))
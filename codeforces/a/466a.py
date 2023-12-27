n, m, a, b = list(map(int, input().split())) 

if b / m >= a: 
    print(a * n) 
else: 
    abon = n // m 
    left = n % m 
    res = abon * b 
    res += (left * a) if left * a < b else b 
    print(res) 
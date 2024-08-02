# Sieve of Eratosthenes (Решето Эратосфена) is an algorithm for finding all the prime numbers in a range [1; n] using O(n log log n) 
# Time: n log log n 
# Space: n (space can optimized when we consider only odd numbers, because all even numbers except for 2 are not primes )
# Source: https://e-maxx.ru/algo/eratosthenes_sieve


# Code Implementation given n - until which we must calculate prime numbers.  

def sieve(n): 
    prime = [True for i in range(n+1)] 
    prime[0] = prime[1] = False 

    for i in range(2, n + 1): 
        if prime[i]: 

            if i * i <= n: 
                for j in range(i * i, n + 1, i): 
                    prime[j] = False  
    
    return prime 


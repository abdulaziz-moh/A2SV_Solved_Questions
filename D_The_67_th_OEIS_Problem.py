mxprime = 150000
is_prime = [True] * (mxprime + 1)
primes = []
for p in range(2, mxprime + 1):
    if is_prime[p]:
        primes.append(p)
        for i in range(p * p, mxprime + 1, p):
            is_prime[i] = False
# print(primes)
t = int(input())
for _ in range(t):
    n = int(input())
    ans = [1]
    
    for i in range(1,n):
        ans.append(primes[i-1] * primes[i])
        
    print(*ans)
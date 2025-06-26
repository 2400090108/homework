def sieve(n):
    isprime = [True]*(n+1)
    isprime[1] = False
    for i in range(2,int(n**0.5)+1):
        if isprime[i]==True:
            for j in range(2*i, n+1, i):
                isprime[j]=False
    return [str(x) for x in range(2,n) if isprime[x]]

T=int(input())
prime_l = sieve(10010)
for i in range(T):
    n = int(input())
    tmp_l = [x for x in prime_l if int(x)<n]
    primes = [x for x in tmp_l if x[-1]=='1']
    print('Case' + str(i+1) + ':')
    if primes==[]:
        print('NULL')
    else:
        print(' '.join(primes))
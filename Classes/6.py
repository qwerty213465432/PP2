<<<<<<< HEAD
def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True



nums = []

primes= list(filter(lambda x: isprime(x), nums)) 

print(primes) 
=======
def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True



nums = []

primes= list(filter(lambda x: isprime(x), nums)) 

print(primes) 
>>>>>>> 4f5a363e377dab23b995e5eeecba25a7e240298a

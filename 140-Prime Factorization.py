import math

#checks if given number is Prime
def isPrime(x, primes):
    for divisor in primes:
        #shorten searching beacause, if one of divisors is bigger than sqrt(x) that means it's a biggest multiplier
        if divisor > math.sqrt(x):
            break
        if x % divisor == 0:
            return (False, primes)
    primes.append(x)        
    return (True, primes)

#finds all Prime factors of given number
def factorize(x):
    primes = []
    primeFactors = []
    divisor = 2
    while x > 1:
        if isPrime(divisor, primes)[0]:          
            if x % divisor == 0:
                x = x / divisor
                primeFactors.append(divisor)
            else:
                divisor += 1    
        else:
            divisor += 1

    return primeFactors

number = int(input("Enter number: "))
factors = factorize(number)
print(f'Prime factors for number {number} are: {factors[0]}, {factors[1]}, {factors[2]}')                
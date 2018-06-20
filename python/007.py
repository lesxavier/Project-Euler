# PE's #007 solution by lesxavier
# Description
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Here I'll be using sort of a Sieve of Eratosthenes

# It would be smarter if we just use a upper limit to this prime (I guess it is n/ln(n), but I'm not sure). Someday in the future I might want to research it and improve this solution.
import time

def primes(n):
    primes = [2]
    x = 1
    while len(primes) < n :
        x += 1
        is_prime = True
        for p in primes:
            if x % p == 0 :
                is_prime = False
        if is_prime:
            primes.append(x)
    return primes

def main():
    start_time = time.time()
    prms = primes(10001)
    end_time = time.time()
    print(prms[len(prms)-1])
    print('Time Elapsed: ',end_time-start_time,'s')


if __name__ == '__main__':
    main()
# PE's #009 solution by lesxavier [INCOMPLETE]
# Description:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
import sys

animation = '|/_\|'

import time
def eratosthenes(n):
    resp = list(range(2,n+1))
    for i in resp:
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        if i == 0 :
            continue
        lim = int(n/i)
        for t in range(2,lim+1):
            resp[i*t-2] = 0
    return resp

def main():
    print('\nCalculating primes...')
    start = time.time()
    primes = eratosthenes(2000000)
    print('\nCalculating the sum...')
    print('\nSum: ',sum(primes))
    end = time.time()
    print('\nTime Elapsed: ',end-start)

if __name__ == '__main__':
    main()
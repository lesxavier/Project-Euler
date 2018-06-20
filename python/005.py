# PE's 005 soluiton by lesxavier
# Description:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math_belt as mb

def main():
    factors = [] 
    for n in range(1,21):
        temp = n
        for f in factors:
            if temp % f == 0 :
                temp = temp/f
        if temp > 1 :
            divisors = mb.factorization(temp)
            for d in divisors :
                factors.append(int(d))
    print(factors)
    temp = mb.prod(factors)
    print(temp)


    
if __name__ == '__main__':
    main()
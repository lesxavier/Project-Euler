# Solution to PE's problem #003 by lesxavier
# Description:
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143? 

from math import sqrt

def factoration(number):
    d = 2
    lim = sqrt(number)
    while number % d != 0 and d <= lim :
        d += 1
    if d > lim:
        print(int(number))
    else:
        print(int(d))
        return factoration(number/d)

def reduct(number,factor):
    while number % factor == 0 :
        number = number/factor
    return number

def fermat(number):
    # This will assume that the given number is odd
    lim = (number+1)/2
    x = int(sqrt(number))
    if x**2 == number :
        return int(x)
    while x < lim :
        x += 1
        y = sqrt(x**2 - number)
        if y%1 == 0 :
            return int(y+x)
    return int(number)   


def factorization(number) :
    # To solve this problem I'll use Fermat Factorization Algorithm, and record all factors found of the number on a list, and then I'm going to use it again until only prime numbers remain on the list.
    end = False
    divisors = [1,number]
    if number % 2 == 0 :
        divisors.append(2)
        reduct(number,2)
    while not end :
        end = True
        for d in divisors:
            f = fermat(d)
            if f != d :
                divisors.remove(d)
                divisors.append(f)
                divisors.append(int(d/f))
                end = False
    return divisors
            

def main():
    divisors_list = factorization(600851475143)
    divisors_list.sort()
    print(divisors_list)

if __name__ == '__main__':
    main()
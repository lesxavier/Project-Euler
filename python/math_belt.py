# Here I'm going to store function that I've made to solve an especific problem but they've turned out to be useful with another problem or set of problems.

from math import sqrt

def fermat(number):
    # From #003
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
    # Adapted from #003 
    # Return, in a list, all the factors of a integer number
    end = False
    divisors = [number]
    if number % 2 == 0 :
        divisors.append(2)
        while number%2 == 0:
            number = number/2
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

def prod(vec):
    # Calculate the product of all elements of a vector/list
    resp = 1
    for v in vec :
        resp = resp*v
    return resp

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
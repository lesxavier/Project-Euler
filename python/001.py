# Solution to PE's 001 Problem by lesxavier
# Description:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


def sum_multiples(numbers,sup=100):
    #Sum all multiples of each of the numbers in 'numbers' from 0 up to 'sup'.
    resp = 0
    for x in range(sup):
        for n in numbers:
            if ( x % n == 0 ):
                resp += x
                break
    return resp
        

if __name__ == '__main__':
    res = sum_multiples([3,5],1000)
    print(res)
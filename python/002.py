# Solution to PE's 002 problem by lesxavier
# Description:
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def solution():
    resp = 0
    fib1 = 1
    fib2 = 1
    while fib2 <= 4e+6 :
        temp = fib1 + fib2
        if temp%2 == 0 :
            resp += temp
        fib1 = fib2
        fib2 = temp
    return resp 

if __name__ == '__main__':
    resp = solution()
    print(resp)
# PE's #006 solution by lesxavier
# Description
# The sum of the squares of the first ten natural numbers is,

# 1² + 2² + ... + 10² = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)² = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# In this problem, I could work with optimization in calculating the square of que sum and the sum of the squeres. But, if we use some math we can conclude that:
# 1² + ... + n² = n(n+1)(2n+1)/6 and 1 + ... + n = (n+1)n/2 (prove it if you will)
# Whith so purposed, we can easily get rid of this problem

def sum_of_squares(n=10):
    if n < 1 :
        return -1
    return n*(n+1)*(2*n + 1)/6

def square_of_sum(n=10):
    resp = (n+1)*n/2
    return resp**2

def main():
    sum_of_sqrs = sum_of_squares(100)
    sqr_of_sum = square_of_sum(100)
    print(int(sqr_of_sum - sum_of_sqrs)) 
    

if __name__ == '__main__':
    main()
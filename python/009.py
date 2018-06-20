# PE's #009 solution by lesxavier
# Description:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# With some basic math we can find out that actually the problem is to solve 2000a + ab + 2000b = 1e+6
# So, to this problem I'll use something more sofisticated, but not too hard to learn. Here I'll be applying the Gradient Descendant Algorithm. Many  Numerical Calculus/Methods might teach this, sometimes only the 1-dimensional version of this algorithm (a.k.a. Newton's Method), so it should'nt be a problem to research and read something about it.

import numpy as np
# F(a,b) = 2000a + ab + 2000b - 1e+6
# gradF(a,b) = ( 2000 + b , 2000 + a )

def gradF(x):
    return np.array([ 2000 + x[0] , 2000 + x[1] ])

def grad_desc(x0,h,tol=1e-2,nmax=1e+6):
    x_next = x0 - h*gradF(x0)
    x_old = x0
    index = 0
    while np.linalg.norm(x_old-x_next) > tol and index < nmax :
        index += 1
        x_old = x_next
        x_next = x_old - h*gradF(x_old)
    if index == nmax :
        print('Maximum steps reached!')
    return(x_next)

def main():
    resp = grad_desc(np.array([3000,4000]),1,1e-3)
    print(resp)

if __name__ == '__main__':
    main()
    
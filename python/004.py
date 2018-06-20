# PE's 004 solution by lesxavier
# Description:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# 999 x 999 = 998001
# abccba ()

def is_palindromic(number) :
    # To determine if a number is palindromic I'm gonna store it on a vector, and compare it's elements.
    #10000
    size = 0
    num_vec = []
    while number >= 1 :
        size += 1
        num_vec.append(number%10)
        number = int(number/10)
        # It doesn't matter if I'm going to read a palindromic number backwards or fowards
    i = 0
    j = size - 1
    while  i != j and i < size/2 :
        if num_vec[i] != num_vec[j] :
            return False
        i += 1
        j -= 1
    return True
    


def main():
    palindromics = []
    for x in range(100,1000) :
        for y in range(100,1000) :
            temp = x*y
            if is_palindromic(temp):
                print(temp)
                palindromics.append(temp)
    palindromics.sort()
    print(palindromics[len(palindromics)-1])

if __name__ == '__main__':
    main()
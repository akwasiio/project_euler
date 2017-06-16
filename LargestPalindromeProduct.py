"""A palindromic number reads the same both ways.


The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 x 99. 
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def ispalindrome(number):
    check = number
    palindrome = 0

    if isinstance(number, int):
        while number != 0:
            remainder = number % 10
            palindrome = palindrome * 10 + remainder
            number = number // 10
        if palindrome == check:
            return True

    return False


def multiply(num1, num2):
    product = num1 * num2
    return product


def largest_palindrome():
    large_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if ispalindrome(multiply(i, j)):
                large_palindrome = multiply(i, j)

    return large_palindrome


print("Largest palindrome:", largest_palindrome())
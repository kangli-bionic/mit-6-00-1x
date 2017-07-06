"""
@project_name: Prime Number Generator

@file_name: generator.py

@description: Generate a sequence of prime numbers on successive calls.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 06, 2017
@updated: July 06, 2017
"""


def genPrimes():
    """
    Returns the sequence of prime number on successive calls to its next()
    method: 2, 3, 5, 7, 11, ...
    """

    # initiate the list of prime numbers
    prime_list = []
    # initiate the next value
    next = 1

    # generate on successive calls
    while True:
        # get a new candidate by adding one to the prime at the end of the list
        next += 1
        # assume the candidate is prime
        is_prime = True

        # n is not a prime if n is a multiple of any of the previous prime
        # numbers on the list. Flag False and break out of for loop immediately
        for prime_number in prime_list:
            if next % prime_number == 0:
                is_prime = False
                break

        # append n to the end of the prime list if n is a prime number
        if is_prime == True:
            prime_list.append(next)
            yield next

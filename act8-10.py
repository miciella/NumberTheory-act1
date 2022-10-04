import math
from math import *

def one():

        n = 56
        # Print the number of two's that divide n
        print("Prime factors of 56:")
        while n % 2 == 0:
            print(2),
            n = n / 2

        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used

        for i in range(3, int(math.sqrt(n)) + 1, 2):

            # while i divides n , print i and divide n
            while n % i == 0:
                print(i),
                n = n / i

        # Condition if n is a prime
        # number greater than 2
        if n > 2:
            return int(n)


def two():
    return


def three():
    return


def four():
    quit()


def default():
    return "Invalid option. Try again"


number_choices = {
    1: one,
    2: two,
    3: three,
    4: four
}


def choice_function(number):
    return number_choices.get(number, default)()


def menu_option():
    print("""Divisibility Theory in the Integers:
        1. Prime factors of 56 (Prime Factorization)
        2. 
        3.
        4.
        5.
        6. Exit""")

    choice = int(input("Choice: "))
    print(choice_function(choice))


menu_option()
try_again = input("\nTry again? y/n: ").lower()

while try_again == 'y':
    menu_option()
    try_again = input("\nTry again? y/n: ").lower()

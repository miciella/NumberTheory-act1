import math
from math import *

def one():

        n = 56
        print("Prime factors of 56:")
        while n % 2 == 0:
            print(2),
            n = n / 2

        for i in range(3, int(math.sqrt(n)) + 1, 2):

            while n % i == 0:
                print(i),
                n = n / i

        if n > 2:
            return int(n)


def two():
    print("****************************")
    print("Linear Diophantine Equation")
    print("****************************")
    #quotient
    q = 0 
    #remainder
    r = 1 
    #s-variables
    k = 1 
    l = 0 
    m = 1 
    #t-variables
    n = 0
    o = 1 
    p = 0 
    
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))
    gcd = math.gcd(a,b)

    while r > 0:
        q = math.floor(a / b)
        r = a - (q * b)
        m = k - (q * l)
        p = n - (q * o)

        if r > 0:
            a = b
            b = r
            k = l
            l = m
            n = o
            o = p
    x = l
    y = o
    print("\nGreatest Common Denominator:", gcd)
    print("Partial Solution:", "x =", x, ",", "y =", y)
    return x, y

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
        2. Linear Diophantine Equation
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

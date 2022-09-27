def one():
    return


def two():
    prime = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    p = 2
    max = len(prime)

    while p * p <= max:
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, max, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    print("Following are the prime numbers less than", 11)
    for p in range(2, max):
        if prime[p]:
            print(p)
    return ""


def three():
    # Python program to print all
    # primes less than to n
    # using Sieve of Eratosthenes
    number = 25
    prime = [True for _ in range(number + 1)]
    p = 2

    while p * p <= number:
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, number + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    print("Following are the prime numbers less than", number)
    for p in range(2, number + 1):
        if prime[p]:
            print(p)
    return ""


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
        1. Show that 3|99
        2. Sieve of Erastosthenes (generate all prime numbers less than 11)
        3. Sieve of Erastosthenes (generate all prime numbers less than 25)
        4. Exit""")

    choice = int(input("Choice: "))
    print(choice_function(choice))


menu_option()
try_again = input("\nTry again? y/n: ").lower()

while try_again == 'y':
    menu_option()
    try_again = input("\nTry again? y/n: ").lower()

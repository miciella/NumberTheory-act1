def one():
    return


def two():
    return


def three():
    return


def four():
    return


def five():
    return


def six():
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


def seven():
    quit()


def default():
    return "Invalid option. Try again"


number_choices = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
}


def choice_function(number):
    return number_choices.get(number, default)()


def menu_option():
    print("""Divisibility Theory in the Integers:
        1. Show that 3|99
        2. Division algorithm (7 does not divide 1717)
        3. Determine whether 121 is a prime number
        4. Are 67942 and 4209 relatively prime?
        5. Are 121, 122, and 123 pairwise relatively prime?
        6. Sieve of Erastosthenes (generate all primes less than 25)
        7. Exit""")

    choice = int(input("Choice: "))
    print(choice_function(choice))


menu_option()
try_again = input("\nTry again? y/n: ").lower()

while try_again == 'y':
    menu_option()
    try_again = input("\nTry again? y/n: ").lower()

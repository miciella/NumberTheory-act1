def one():
    # is this right?? lolx
    print("""\nAssociative (Addition)
    x+(y+z) = (x+y)+z\n""")
    x = input("Enter value of x: ")
    y = input("Enter value of y: ")
    z = input("Enter value of z: ")

    return f"{x}+({y}+{z}) = ({x}+{y})+{z}"


def two():
    print("Commutative (Addition)")


def three():
    print("Identity (Addition)")


def four():
    print("Associative (Multiplication)")


def five():
    print("Commutative (Multiplication)")


def six():
    print("Identity (Multiplication)")


def seven():
    print("Distribution")


def eight():
    print("Addition is closed")


def nine():
    print("Multiplication is closed")


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
    8: eight,
    9: nine
    }


def choice_function(number):
    return number_choices.get(number, default)()


def menu_option():
    print("""Properties of Natural Numbers:
        1. Associative (Addition)
        2. Commutative (Addition)
        3. Identity (Addition)
        4. Associative (Multiplication)
        5. Commutative (Multiplication)
        6. Identity (Multiplication)
        7. Distribution
        8. Addition is closed
        9. Multiplication is closed
        10. Exit""")

    choice = int(input("Choose a property for Natural Numbers: "))
    print(choice_function(choice))


menu_option()
try_again = input("\nTry again? y/n: ").lower()


# lol idk if this is efficient (change if meron pa other way hehe)
while try_again == 'y':
    menu_option()
    try_again = input("\nTry again? y/n: ").lower()





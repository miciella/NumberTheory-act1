def one():
    print("""\nAssociative (Addition)
    x+(y+z) = (x+y)+z\n""")
    x = int(input("Enter value of x: "))
    y = int(input("Enter value of y: "))
    z = int(input("Enter value of z: "))

    print(f"{x}+({y}+{z}) = ({x}+{y})+{z}")
    return f"{x+(y+z)} = {(x+y)+z}"


def two():
    print("""\nCommutative (Addition)
       m+n = n+m\n""")
    m = int(input("Enter value of m: "))
    n = int(input("Enter value of n: "))

    print(f"{m}+{n} = {n}+{m}")
    return f"{m+n} = {n+m}"


def three():
    print("""\nIdentity (Addition)
           0+n = n\n""")
    n = input("Enter value of n: ")

    return f"0+{n} = {n}"


def four():
    print("""\nAssociative (Multiplication)
    (x*y)*z = x*(y*z)\n""")
    x = int(input("Enter value of x: "))
    y = int(input("Enter value of y: "))
    z = int(input("Enter value of z: "))

    
    print(f"({x}*{y})*{z} = {x}*({y}*{z})")
    return f"{(x*y)*z} = {x*(y*z)}"

def five():
    print("""\nCommutative (Multiplication)
    x*y = y*x\n""")
    x = int(input("Enter value of x: "))
    y = int(input("Enter value of y: "))

    print(f"{x}*{y} = {y}*{x}")
    return f"{x*y} = {y*x}"


def six():
    print("""\nIdentity (Multiplication)
    n*1 = n = 1*n\n""")
    n = int(input("Enter value of n: "))
    
    
    print(f"{n} * {1} = {n} = {1} * {n}") 
    return f"{n * 1} = {n} = {1 * n}"

def seven():
    print("""\nDistribution (Multiplication over Addition)
    (x+y)*z = (x*z)+(y*z)\n""")
    x = int(input("Enter value of x: "))
    y = int(input("Enter value of y: "))
    z = int(input("Enter value of z: "))

    print(f"({x}+{y})*{z} = ({x}*{z})+({y}*{z})")
    return f"{(x+y)*z} = {(x*z)+(y*z)}"


def eight():
    print("""\nClosure Property (Addition)
       m+n ∈ N, for all m, n ∈ N\n""")
    m = int(input("Enter value of m: "))
    n = int(input("Enter value of n: "))
    
    return f"{m}+{n} = {int(n) + int(m)}"

def nine():
    print("""\nClosure Property (Multiplication)
       m*n ∈ N, for all m, n ∈ N\n""")
    m = input("Enter value of m: ")
    n = input("Enter value of n: ")
    
    return f"{m}*{n} = {int(n) * int(m)}"


def ten():
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
    8: eight,
    9: nine,
    10: ten
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
        8. Closure Property (Addition)
        9. Closure Property (Multiplication)
        10. Exit""")

    choice = int(input("Choose a property for Natural Numbers: "))
    print(choice_function(choice))


menu_option()
try_again = input("\nTry again? y/n: ").lower()

while try_again == 'y':
    menu_option()
    try_again = input("\nTry again? y/n: ").lower()


def mainMenu():

    print()
    print(""""=== Subtopics 3 & 4 Calculators and Generators ===
        1 - Permutations
        2 - Combinations
        3 - Pascal Triangle Generator
        4 - Binomial Expansion""")

    choice = int(input("What would you like to do? "))
    if choice == 1:
        permMenu()
    elif choice == 2:
        combMenu()
    elif choice == 3:
        pascalGen()
    elif choice == 4:
        binomialExp()
    else:
        quit()

def permMenu():

    print()
    print("=== Permutation Calculator ===")
    print("1 - Normal Permutation")
    print("2 - Round Table Permutation")
    print("3 - Distinguishable Permutation")

    choice = int(input("What would you like to do? "))
    if choice == 1:
        normalPermutation()
    elif choice == 2:
        circlePermutation()
    elif choice == 3:
        distPermutation()
    else:
        quit()

def normalPermutation():

    os.system("PAUSE")

def circlePermutation():
    print()
    x = int(input("How many total items are there? "))

    newX = 1

    for i in range( x -1, 1, -1):
        newX = i * newX

    finalPerm = newX

    print(int(finalPerm), "ways")
    os.system("PAUSE")

def distPermutation():
    print()
    itemTypes = int(input("How many types of items are there? "))
    itemCount = []
    totalItems = 0
    newX = 1
    newY = 1

    for i in range(1, itemType s +1):
        print("How many type", i, "items are there? ")
        itemCount.append(int(input()))
        totalItems = totalItems + itemCount[ i -1]

    for i in range(totalItems, 1, -1):
        newX = i * newX

    newY = 1
    for i in itemCount:
        newZ = 1
        for j in range(i, 1, -1):
            newZ = j * newZ
        newY = newY * newZ

    finalPerm = newX / newY
    print(int(finalPerm), "ways")
    os.system("PAUSE")

def combMenu():

    print()
    print("=== Combination Calculator ===")
    print("1 - Normal Combination")
    print("2 - Mixed Combination")

    choice = int(input("What would you like to do? "))
    if choice == 1:
        baseCombination()
    elif choice == 2:
        mixedCombination()
    else:
        quit()

def baseCombination():
    print()
    x = int(input("How many total items are there? "))
    y = int(input("How many items are to be selected? "))

    newX = 1
    newY = 1
    newZ = 1

    for i in range(x, 1, -1):
        newX = i * newX

    for i in range(y, 1, -1):
        newY = i * newY

    for i in range( x -y, 1, -1):
        newZ = i * newZ

    finalComb = newX / (newY * newZ)

    print(int(finalComb), "combinations")
    os.system("PAUSE")

def mixedCombination():
    print()
    itemTypes = int(input("How many types of items are there? "))
    itemCount = []
    itemSelect = []
    itemDiff = []
    newItemCount = []
    newItemSelect = []
    newItemDiff = []
    perCombination = []
    newA = 1

    for i in range(1, itemType s +1):
        print("How many type", i, "items are there? ")
        itemCount.append(int(input()))

    for i in range(1, itemType s +1):
        print("How many of type", i, "items are to be selected? ")
        itemSelect.append(int(input()))

    for i in range(1, itemType s +1):
        newItem = itemCount[ i -1] - itemSelect[ i -1]
        itemDiff.append(newItem)

    for i in itemCount:
        newX = 1
        for j in range(i, 1, -1):
            newX = j * newX
        newItemCount.append(newX)

    for i in itemSelect:
        newY = 1
        for j in range(i, 1, -1):
            newY = j * newY
        newItemSelect.append(newY)

    for i in itemDiff:
        newZ = 1
        for j in range(i, 1, -1):
            newZ = j * newZ
        newItemDiff.append(newZ)

    for i in range(0, itemTypes):
        itemCombs = newItemCount[i] / (newItemSelect[i] * newItemDiff[i])
        perCombination.append(itemCombs)

    for i in perCombination:
        newA = newA * i

    finalComb = newA

    print(int(finalComb), "combinations")
    os.system("PAUSE")

def pascalGen():
    print()
    exponent = int(input("Please enter the exponent to generate Pascal Triangle: "))
    arrayOne = []
    arrayTwo = [1]

    print(arrayTwo)
    for i in range(1, exponen t +1):
        arrayTwo.clear()
        arrayTwo.append(1)
        for j in range(1, i+ 1):
            if j == i:
                arrayTwo.append(1)
            else:
                arrayTwo.append(arrayOne[j - 1] + arrayOne[j])
        print(arrayTwo)
        arrayOne.clear()
        arrayOne = arrayTwo.copy()
    os.system("PAUSE")


def binomialExp():
    print()
    exponent = int(input("Please enter the exponent to generate Pascal Triangle: "))
    a = int(input("Please enter coefficient of x: "))
    b = int(input("Please enter coefficient of y: "))
    arrayOne = []
    arrayTwo = []

    for i in range(1, exponent + 1):
        arrayTwo.clear()
        arrayTwo.append(1)
        for j in range(1, i + 1):
            if j == i:
                arrayTwo.append(1)
            else:
                arrayTwo.append(arrayOne[j - 1] + arrayOne[j])
        arrayOne.clear()
        arrayOne = arrayTwo.copy()

    x = len(arrayTwo) - 1
    y = 0

    print()
    print("Your expanded equation is:")
    for i in arrayTwo:
        coEf = ((a ** x) * (b ** y) * i)
        if coEf == 1:
            pass
        else:
            print(coEf, end="")
        if y == 0:
            print("x^" + str(x) + " + ", end="")
        elif y == 1:
            print("x^" + str(x) + "y + ", end="")
        elif x == 1:
            print("xy^" + str(y) + " + ", end="")
        elif x == 0:
            print("y^" + str(y), end="")
        else:
            print("x^" + str(x) + "y^" + str(y) + " + ", end="")
        x -= 1
        y += 1
    os.system("PAUSE")


while True:
    mainMenu()


# def one():
#     print("""\nAssociative (Addition)
#     x+(y+z) = (x+y)+z\n""")
#     x = int(input("Enter value of x: "))
#     y = int(input("Enter value of y: "))
#     z = int(input("Enter value of z: "))
#
#     print(f"{x}+({y}+{z}) = ({x}+{y})+{z}")
#     return f"{x+(y+z)} = {(x+y)+z}"
#
#
# def two():
#     print("""\nCommutative (Addition)
#        m+n = n+m\n""")
#     m = int(input("Enter value of m: "))
#     n = int(input("Enter value of n: "))
#
#     print(f"{m}+{n} = {n}+{m}")
#     return f"{m+n} = {n+m}"
#
#
# def three():
#     print("""\nIdentity (Addition)
#            0+n = n\n""")
#     n = input("Enter value of n: ")
#
#     return f"0+{n} = {n}"
#
#
# def four():
#     print("""\nAssociative (Multiplication)
#     (x*y)*z = x*(y*z)\n""")
#     x = int(input("Enter value of x: "))
#     y = int(input("Enter value of y: "))
#     z = int(input("Enter value of z: "))
#
#
#     print(f"({x}*{y})*{z} = {x}*({y}*{z})")
#     return f"{(x*y)*z} = {x*(y*z)}"
#
# def five():
#     print("""\nCommutative (Multiplication)
#     x*y = y*x\n""")
#     x = int(input("Enter value of x: "))
#     y = int(input("Enter value of y: "))
#
#     print(f"{x}*{y} = {y}*{x}")
#     return f"{x*y} = {y*x}"
#
#
# def six():
#     print("""\nIdentity (Multiplication)
#     n*1 = n = 1*n\n""")
#     n = int(input("Enter value of n: "))
#
#
#     print(f"{n} * {1} = {n} = {1} * {n}")
#     return f"{n * 1} = {n} = {1 * n}"
#
# def seven():
#     print("""\nDistribution (Multiplication over Addition)
#     (x+y)*z = (x*z)+(y*z)\n""")
#     x = int(input("Enter value of x: "))
#     y = int(input("Enter value of y: "))
#     z = int(input("Enter value of z: "))
#
#     print(f"({x}+{y})*{z} = ({x}*{z})+({y}*{z})")
#     return f"{(x+y)*z} = {(x*z)+(y*z)}"
#
#
# def eight():
#     print("""\nClosure Property (Addition)
#        m+n ∈ N, for all m, n ∈ N\n""")
#     m = int(input("Enter value of m: "))
#     n = int(input("Enter value of n: "))
#
#     return f"{m}+{n} = {int(n) + int(m)}"
#
# def nine():
#     print("""\nClosure Property (Multiplication)
#        m*n ∈ N, for all m, n ∈ N\n""")
#     m = input("Enter value of m: ")
#     n = input("Enter value of n: ")
#
#     return f"{m}*{n} = {int(n) * int(m)}"
#
#
# def ten():
#     quit()
#
#
# def default():
#     return "Invalid option. Try again"
#
#
# number_choices = {
#     1: one,
#     2: two,
#     3: three,
#     4: four,
#     5: five,
#     6: six,
#     7: seven,
#     8: eight,
#     9: nine,
#     10: ten
#     }
#
#
# def choice_function(number):
#     return number_choices.get(number, default)()
#
#
# def menu_option():
#     print("""Properties of Natural Numbers:
#         1. Associative (Addition)
#         2. Commutative (Addition)
#         3. Identity (Addition)
#         4. Associative (Multiplication)
#         5. Commutative (Multiplication)
#         6. Identity (Multiplication)
#         7. Distribution
#         8. Closure Property (Addition)
#         9. Closure Property (Multiplication)
#         10. Exit""")
#
#     choice = int(input("Choose a property for Natural Numbers: "))
#     print(choice_function(choice))
#
#
# menu_option()
# try_again = input("\nTry again? y/n: ").lower()
#
# while try_again == 'y':
#     menu_option()
#     try_again = input("\nTry again? y/n: ").lower()

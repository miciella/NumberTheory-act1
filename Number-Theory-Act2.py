
    def one():
        print("""\nPermutations
        1 - Normal Permutation
        2 - Round Table Permutation
        3 - Distinguishable Permutation\n""")

        choice = int(input("What would you like to do? "))
        if choice == 1:
            # normalPermutation()
        elif choice == 2:
            # circlePermutation()
        elif choice == 3:
            # distPermutation()
        else:
            quit()


    def two():
        print("""\nCombinations\n
            1. Normal Combination
            2. Mixed Combination""")

        choice = int(input("Choose a type of combination: "))
        if choice == 1:
            # baseCombination()
        elif choice == 2:
            # mixedCombination()
        else:
            quit()


    def three():
        print("""\nPascal Generator\n""")
        exponent = int(input("Please enter the exponent to generate Pascal Triangle: "))
        arrayOne = []
        arrayTwo = [1]

        print(arrayTwo)
        for i in range(1, exponen t +1):
            arrayTwo.clear()
            arrayTwo.append(1)
            for j in range(1, i + 1):
                if j == i:
                    arrayTwo.append(1)
                else:
                    arrayTwo.append(arrayOne[j - 1] + arrayOne[j])
            print(arrayTwo)
            arrayOne.clear()
            arrayOne = arrayTwo.copy()


    def four():
        print("""\nBinomial Expression\n""")
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


    def five():
        quit()


    def default():
        return "Invalid option. Try again"


    number_choices = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five
    }


    def choice_function(number):
        return number_choices.get(number, default)()


    def menu_option():
        print("""Properties of Natural Numbers:
            1. Permutations
            2. Combinations
            3. Pascal Triangle Generator
            4. Binomial Expansion
            5. Exit""")

        choice = int(input("Select option: "))
        print(choice_function(choice))


    menu_option()
    try_again = input("\nTry again? y/n: ").lower()

    while try_again == 'y':
        menu_option()
        try_again = input("\nTry again? y/n: ").lower()
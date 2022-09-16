
def one():
    print("""\nPermutations
    1 - Normal Permutation
    2 - Round Table Permutation
    3 - Distinguishable Permutation\n""")

    choice = int(input("What would you like to do? "))
    if choice == 1:
        if choice == 1:
            x = int(input("How many total items are there? "))
            y = int(input("How many items are to be arranged at a time? "))
            new_x = 1
            new_y = 1
            if (x >= y):
                for i in range(x, 1, -1):
                    new_x = i * new_x

                for i in range(x - y, 1, -1):
                    new_y = i * new_y
                final_perm = int(new_x / new_y)

                return f"{final_perm} ways"
            else:
                return "\nWARNING: Total items should be bigger than items to be arranged"

    elif choice == 2:
        x = int(input("How many total items are there? "))
        new_x = 1

        for i in range(x - 1, 1, -1):
            new_x = i * new_x

        final_perm = new_x
        return f"{int(final_perm)} ways"

    elif choice == 3:
        item_types = int(input("How many types of items are there? "))
        item_count = []
        total_items = 0
        new_x = 1

        for i in range(1, item_types +1):
            print("How many type", i, "items are there? ")
            item_count.append(int(input()))
            total_items = total_items + item_count[i - 1]

        for i in range(total_items, 1, -1):
            new_x = i * new_x

        new_y = 1
        for i in item_count:
            new_z = 1
            for j in range(i, 1, -1):
                new_z = j * new_z
            new_y = new_y * new_z

        final_perm = new_x / new_y

        return f"{int(final_perm)} ways"
    else:
        return "Invalid option"

def two():
    print("""\nCombinations\n
        1. Normal Combination
        2. Mixed Combination""")

    choice = int(input("Choose a type of combination: "))
    if choice == 1:
            x = int(input("How many total items are there? "))
            y = int(input("How many items are to be selected? "))

            if(x>=y):
                new_x = 1
                new_y = 1
                new_z = 1

                for i in range(x, 1, -1):
                    new_x = i * new_x

                for i in range(y, 1, -1):
                    new_y = i * new_y

                for i in range(x - y, 1, -1):
                    new_z = i * new_z

                final_comb = new_x / (new_y * new_z)

                return f"{int(final_comb)} combinations"
            else:
                return "\nWARNING: Total items should be bigger than items to be arranged"

    elif choice == 2:
            item_types = int(input("How many types of items are there? "))
            item_count = []
            item_select = []
            item_diff = []
            new_item_count = []
            new_item_select = []
            new_item_diff = []
            per_combination = []
            new_a = 1

            for i in range(1, item_types +1):
                print("How many type", i, "items are there? ")
                item_count.append(int(input()))

            for i in range(1, item_types +1):
                print("How many of type", i, "items are to be selected? ")
                item_select.append(int(input()))

            for i in range(1, item_types +1):
                new_item = item_count[i - 1] - item_select[i - 1]
                item_diff.append(new_item)

            for i in item_count:
                new_x = 1
                for j in range(i, 1, -1):
                    new_x = j * new_x
                new_item_count.append(new_x)

            for i in item_select:
                new_y = 1
                for j in range(i, 1, -1):
                    new_y = j * new_y
                new_item_select.append(new_y)

            for i in item_diff:
                new_z = 1
                for j in range(i, 1, -1):
                    new_z = j * new_z
                new_item_diff.append(new_z)

            for i in range(0, item_types):
                item_combs = new_item_count[i] / (new_item_select[i] * new_item_diff[i])
                per_combination.append(item_combs)

            for i in per_combination:
                new_a = new_a * i

            final_comb = new_a

            return f"{int(final_comb)} combinations"
    else:
        return "Invalid option"

def three():
    print("""\nPascal Generator\n""")
    exponent = int(input("Please enter the exponent to generate Pascal Triangle: "))
    arr1 = []
    arr2 = [1]

    print(arr2)
    for i in range(1, exponent +1):
        arr2.clear()
        arr2.append(1)
        for j in range(1, i + 1):
            if j == i:
                arr2.append(1)
            else:
                arr2.append(arr1[j - 1] + arr1[j])
        print(arr2)
        arr1.clear()
        arr1 = arr2.copy()
    return ""

def four():
    print("""\nBinomial Expression\n""")
    exponent = int(input("Please enter the exponent to generate Pascal Triangle: "))
    a = int(input("Enter coefficient of x: "))
    b = int(input("Enter coefficient of y: "))
    arr1 = []
    arr2 = []

    for i in range(1, exponent + 1):
        arr2.clear()
        arr2.append(1)
        for j in range(1, i + 1):
            if j == i:
                arr2.append(1)
            else:
                arr2.append(arr1[j - 1] + arr1[j])
        arr1.clear()
        arr1 = arr2.copy()

    x = len(arr2) - 1
    y = 0

    print()
    print("Your expanded equation is:")
    for i in arr2:
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
    return ""

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
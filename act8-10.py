import math
from math import *
from functools import reduce

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
    print("""\nDetermine the prime factors of 96 using a factor tree.\n""")

    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.key = key

    def newNode(key):
        temp = Node(key)
        return temp

    def factorTree(node, v):
        node = newNode(v)

        for i in range(2, int(v / 2)):

            if (v % i != 0):
                continue

            node.left = factorTree(((node).left), i)
            node.right = factorTree(((node).right), int(v / i))
            return node

        return node

    def levelOrder(root):

        if (root == None):
            return
        q = [];
        q.append(root);
        while (len(q) > 0):

            node = q[0]
            print(node.key, end=" ")
            q = q[1:]
            if (node.left != None):
                q.append(node.left)
            if (node.right != None):
                q.append(node.right)

    value = 96
    root = None
    root = factorTree(root, value)
    levelOrder(root)
    print("\n96 = 2 × 2 × 2 × 2 × 2 × 3 = 2^5 × 3^1")
    print("\nTherefore, the prime factors of 96 are 2 and 3.")
    return ""

def three():
    def primeFactors(n):
        primelist = []
        while n % 2 == 0:
            primelist.append(2)
        n = n / 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                primelist.append(i)
            n = n / i

        if n > 2:
            primelist.append(n)
        return primelist


    x = primeFactors(315)
    print(x)
    y = primeFactors(825)
    print(y)

    prime_arr = []
    for elem in x:
        if elem in y:
            prime_arr.append(elem)
            y.remove(elem)

    final = 1
    for elem in prime_arr:
        final = final * elem
    print(final)

    return ""


def four():
    def gcd(x, y):
        r = x % y
        if r == 0:
            return y
        else:
            x = y
            y = r
            return gcd(x, y)

    if __name__ == '__main__':
        print(gcd(4361, 42371))

    return ""

def five():
    print("****************************")
    print("Linear Diophantine Equation")
    print("****************************")
    # quotient
    q = 0
    # remainder
    r = 1
    # s-variables
    k = 1
    l = 0
    m = 1
    # t-variables
    n = 0
    o = 1
    p = 0

    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))
    gcd = math.gcd(a, b)

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

def six():
    print("""\nDetermine the LCM(24,32, 40) using Factor Tree.\n""")

    def test(nums):
        return reduce(lambda x, y: lcm(x, y), nums)

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    nums = [24, 32, 40]
    print("Original list elements:")
    print(nums)
    print("LCM of the given numbers :", test(nums))
    return ""

def seven():
    print("""\nDetermine the LCM (175, 60, 128) using ladder method.\n""")

    def compute_lcm(x, y, z):
        values = [x, y, z]
        values.sort()

        greater = values[-1]

        while (True):
            if ((greater % x == 0) and (greater % y == 0) and (greater % z == 0)):
                lcm = greater
                break
            greater += 1

        return lcm

    num1 = 175
    num2 = 60
    num3 = 128

    print("The LCM is", compute_lcm(num1, num2, num3))
    return

def eight():
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
}


def choice_function(number):
    return number_choices.get(number, default)()


def menu_option():
    print("""Divisibility Theory in the Integers:
        Activity 8:
        1. Prime factors of 56 (Prime Factorization)
        2. Determine the prime factors of 96 using a factor tree.
        Activity 9:
        3. Determine GCD(315, 825) using Factor Tree.
        4. Determine GCD(4361, 42371) using Euclidean Algorithm.
        5. Linear Diophantine Equation
        Activity 10:
        6. Determine LCM(24, 32, 40) using Factor Tree.
        7. Determine LCM(175, 60, 128) using Ladder Method.
        8. Exit""")

    choice = int(input("Choice: "))
    print(choice_function(choice))


menu_option()
try_again = input("\nTry again? y/n: ").lower()

while try_again == 'y':
    menu_option()
    try_again = input("\nTry again? y/n: ").lower()

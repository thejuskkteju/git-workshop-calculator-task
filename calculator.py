"""
Simple Menu-Driven Calculator
Part of Git & GitHub Hands-on Workshop
Organized by Algon DC GCEK
Date: November 8, 2025

"""


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# TODO: Implement this function
def divide(a, b):
    if b ==0:
        return "zero div error"
    else:
        return a/b

# TODO: Implement this function
def power(a, b):
    return a**b

while True:
    print("\n---- CALCULATOR MENU ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Exiting... Byeee !!")
        break

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice! Please try again.")
        continue

    try:
        num1 = float(input("Enter  number: "))
        num2 = float(input("Enter  number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))

    elif choice == '4':
        print("Result:", divide(num1, num2))  
    elif choice == '5':
        print("Result:", power(num1, num2))   
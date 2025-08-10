class Calculator:
    def __init__(self):
        print(" Simple Calculator Ready!")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return " Error: Cannot divide by zero."
        return a / b


calc = Calculator()


while True:
    print("\nOperations:")
    print("1. Add ")
    print("2. Subtract ")
    print("3. Multiply ")
    print("4. Divide ")
    print("5. Exit ")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("👋 Goodbye!")
        break

  
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print(" Please enter valid numbers.")
        continue


    if choice == '1':
        result = calc.add(num1, num2)
    elif choice == '2':
        result = calc.subtract(num1, num2)
    elif choice == '3':
        result = calc.multiply(num1, num2)
    elif choice == '4':
        result = calc.divide(num1, num2)
    else:
        print(" Invalid choice. Try again.")
        continue

    print("Result:", result)

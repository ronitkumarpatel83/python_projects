class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        try:
            return self.num1 + self.num2
        except Exception as message:
            return message

    def sub(self):
        try:
            return self.num1 - self.num2
        except Exception as message:
            return message

    def mul(self):
        try:
            return self.num1 * self.num2
        except Exception as message:
            return message

    def div(self):
        try:
            return self.num1 // self.num2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        except Exception as message:
            return message


if __name__ == "__main__":
    print("="*120)
    print("="*120)
    print("="*53, " Calculator ", "="*53)
    print("="*120)
    print("="*120)

    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Please select a number : "))
        except ValueError:
            print("Invalid input! Please enter a number between 1-5.")
            continue

        if choice == 5:
            print("Exiting Calculator... Goodbye!")
            break

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please try again.")
            continue

        try:
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number : "))
        except ValueError:
            print("Invalid number entered!")
            continue

        cal = Calculator(num1, num2)

        if choice == 1:
            print("Result:", cal.add())
        elif choice == 2:
            print("Result:", cal.sub())
        elif choice == 3:
            print("Result:", cal.mul())
        elif choice == 4:
            print("Result:", cal.div())

    print("="*120)
    print("="*120)

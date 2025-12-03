class Temperature_Converter:
    def __init__(self, number):
        self.number = number

    def celcius_to_fahrenheit(self):
        return (self.number * 9/5) + 32
    
    def fahrenheit_to_celcius(self):
        return (self.number - 32) * 5/9
    
if __name__ == "__main__":
    print("="*120)
    print("="*120)
    print("="*47, " Temperature Calculator ", "="*47)
    print("="*120)
    print("="*120)

    while True:
        print("\n1. Celcius to Farhenheit\n2. Fahrenheit to Celcius")
        print("0. Exit")

        try:
            choice = int(input("Please select a number : "))
        except ValueError:
            print("Invalid input! Please enter a number between 1-5.")
            continue

        if choice == 0:
            print("Exiting Temperature Calculator... Goodbye!")
            break

        if choice not in [1, 2]:
            print("Invalid choice! Please try again.")
            continue

        try:
            num1 = int(input("Enter Temperature value : "))
        except ValueError:
            print("Invalid number entered!")
            continue

        tem_cal = Temperature_Converter(num1)

        if choice == 1:
            print("Result:", tem_cal.celcius_to_fahrenheit())
        elif choice == 2:
            print("Result:", tem_cal.fahrenheit_to_celcius())

    print("="*120)
    print("="*120)


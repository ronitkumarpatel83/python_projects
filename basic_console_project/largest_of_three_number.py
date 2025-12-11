class LargestOfThree:
    def __init__(self):
        pass

    def largest_number(self, a, b, c):
        # Comparing three numbers
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c


if __name__ == "__main__":
    print("="*120)
    print("="*120)
    print("="*45, " Largest of Three Numbers ", "="*45)
    print("="*120)
    print("="*120)

    while True:
        try:
            user_input = input("\nEnter three numbers separated by space (write exit to exit): ").strip()
        except Exception as e:
            print("Invalid input! Please try again.")
            continue

        if user_input.lower() == "exit":
            print("\nThank you for using Largest Number Finder!")
            break

        parts = user_input.split()

        # Validate count
        if len(parts) != 3:
            print("Please enter exactly THREE numbers!")
            continue

        try:
            a, b, c = map(float, parts)
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        finder = LargestOfThree()
        largest = finder.largest_number(a, b, c)

        print("Largest Number :", largest)

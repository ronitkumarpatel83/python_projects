import random
import string

class SimplePasswordGenerator:
    def __init__(self):
        pass

    def pass_generator(self, length):
        letters = list(string.ascii_letters)
        digits = list(string.digits)
        symbols = list(string.punctuation)

        characters = letters + digits + symbols
        password_list = random.choices(characters, k=length)
        random.shuffle(password_list)
        password = "".join(password_list)
        print("\nGenerated Password:", password)


if __name__ == "__main__":
    print("="*120)
    print("="*120)
    print("="*50, " Simple Password Generator ", "="*50)
    print("="*120)
    print("="*120)

    while True:
        try:
            length = int(input("\nEnter password length (0 to exit): "))
        except Exception as e:
            print("Invalid input! Please enter a number.")
            continue

        if length == 0:
            print("\nThank you for using the Password Generator!")
            break

        if length < 0:
            print("Length cannot be negative!")
            continue

        spg = SimplePasswordGenerator()
        spg.pass_generator(length)

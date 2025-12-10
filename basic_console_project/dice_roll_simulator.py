import random

class DiceRollSimulator:
    def __init__(self):
        pass

    def dice_roll(self):
        return random.randint(1, 6)
    
if __name__ == "__main__":
    print("="*120)
    print("="*120)
    print("="*49, " Dice Roll Simulator ", "="*48)
    print("="*120)
    print("="*120)

    while True:
        print("\n1. Roll Dice")
        print("0. Exit")

        try:
            choice = int(input("Please enter your choice: "))
        except Exception as message:
            print("Error:", message)
            continue

        if choice not in [0, 1]:
            print("Invalid number! Enter 0 or 1.")
            continue

        if choice == 0:
            print("\nThank you for using Dice Roll Simulator!")
            break

        dice = DiceRollSimulator()
        result = dice.dice_roll()
        print(f"You rolled a {result}")

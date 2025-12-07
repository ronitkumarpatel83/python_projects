import string

class CountVowelsOrConsonants:
    def __init__(self):
        pass

    def vowels_and_consonants_count(self, string_line):
        vowel = 0
        consonant = 0

        string_line = string_line.lower()

        for char in string_line:
            if char.isalpha():
                if char in ["a", "e", "i", "o", "u"]:
                    vowel += 1
                else:
                    consonant += 1

        return vowel, consonant


if __name__ == "__main__":
    print("="*120)
    print("="*120)
    print("="*50, " Count Vowels/Consonants in a string ", "="*50)
    print("="*120)
    print("="*120)

    while True:
        try:
            string_line = input("\nEnter string line (write exit for exit): ")
        except Exception as e:
            print("Invalid input! Please enter a string.")
            continue

        if string_line.lower() == "exit":
            print("\nThank you for using Vowels and Consonants count!")
            break

        if len(string_line) == 0:
            print("String should not be empty!")
            continue

        counter = CountVowelsOrConsonants()
        vowel, consonant = counter.vowels_and_consonants_count(string_line)

        print("Vowels      :", vowel)
        print("Consonants :", consonant)

class PalindromeChecker:
    def __init__(self):
        pass

    def is_palindrome(self, string_word):
        string_word = string_word.lower().strip()
        reversed_string_word = string_word[::-1]

        return string_word == reversed_string_word


if __name__ == "__main__":

    print("="*120)
    print("="*120)
    print("="*49, " Palindrome Checker ", "="*49)
    print("="*120)
    print("="*120)
    
    while True:
        try:
            string_line = input("\nEnter string (write exit for exit): ")
        except Exception as e:
            print("Invalid input! Please enter a string.")
            continue

        if string_line.lower() == "exit":
            print("\nThank you for using Palindrome Checker!")
            break

        if len(string_line) == 0:
            print("String should not be empty!")
            continue

        checker = PalindromeChecker()
        palindrome = checker.is_palindrome(string_line)

        if palindrome:
            print(f"'{string_line}' is a Palindrome")
        else:
            print(f"'{string_line}' is NOT a Palindrome")

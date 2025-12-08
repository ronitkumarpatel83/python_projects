
class WordOrCharacterFrequencyCounter:
    def __init__(self):
        pass

    def word_counter(self, string_line):
        word_list = string_line.split()
        word_counter_dict = {}

        for item in word_list:
            if item in word_counter_dict:
                word_counter_dict[item] += 1
            else:
                word_counter_dict[item] = 1
        return word_counter_dict

if __name__ == "__main__":
    print("="*120)
    print("="*120)
    print("="*42, " Word/Character Frequency Counter ", "="*42)
    print("="*120)
    print("="*120)
    
    while True:
        try:
            string_line = input("\nEnter string line (write exit for exit): ")
        except Exception as e:
            print("Invalid input! Please enter string.")
            continue

        if string_line.lower() == "exit":
            print("\nThank you for using Word/Character Frequency Counter!")
            break

        if len(string_line) == 0:
            print("String should not be empty!")
            continue

        word_counter = WordOrCharacterFrequencyCounter()
        count_value = word_counter.word_counter(string_line)

        print(count_value)

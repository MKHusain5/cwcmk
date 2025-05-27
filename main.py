import random

def load_word_list(file_path):
    """Load words from a text file."""
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def generate_random_phrase(word_list, num_words):
    """Generate a random phrase with a specified number of words."""
    return ' '.join(random.choice(word_list) for _ in range(num_words))

def show_menu():
    """Display the menu and handle user selection."""
    print("Select an option:")
    print("1. Random 12-word Crypto Wallet Checker")
    print("2. Random 24-word Crypto Wallet Checker")

    choice = input("Enter your choice (1 or 2): ")

    word_list = load_word_list('wordlist.txt')

    if choice == '1':
        phrase = generate_random_phrase(word_list, 12)
        print(f"\nRandom 12-word secret phrase: {phrase}\n")
    elif choice == '2':
        phrase = generate_random_phrase(word_list, 24)
        print(f"\nRandom 24-word secret phrase: {phrase}\n")
    else:
        print("\nInvalid choice. Please enter 1 or 2.\n")

if __name__ == "__main__":
    show_menu()

import random

def create_secret_phrase(filename='wordlist.txt', num_words=12):
    try:
        # Read the word list from the file
        with open(filename, 'r') as file:
            words = file.read().splitlines()

        # Check if the file has enough words
        if len(words) < num_words:
            raise ValueError(f"The word list must contain at least {num_words} words.")

        # Select random words
        secret_phrase = random.sample(words, num_words)

        # Return the list of words
        return secret_phrase

    except FileNotFoundError:
        print("Error: The file 'wordlist.txt' was not found.")
    except ValueError as e:
        print(f"Error: {e}")

# Example usage
secret_phrase_list = create_secret_phrase()
if secret_phrase_list:
    print("Secret Phrase List:", secret_phrase_list)

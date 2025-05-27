
 ```python
     import random

     def load_word_list(file_path):
         with open(file_path, 'r') as file:
             words = file.read().splitlines()
         return words

     def generate_random_phrase(word_list, num_words=12):
         return ' '.join(random.choice(word_list) for _ in range(num_words))

     # Load words from the text file
     word_list = load_word_list('../wordlist.txt')

     # Generate a random 12-word secret phrase
     random_phrase = generate_random_phrase(word_list, 12)

     print(f"Random 12-word secret phrase: {random_phrase}")￼Enter

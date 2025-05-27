import random
import requests
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

def load_word_list(file_path):
    """Load words from a text file."""
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def generate_random_phrase(word_list, num_words):
    """Generate a random phrase with a specified number of words."""
    return ' '.join(random.choice(word_list) for _ in range(num_words))

def generate_wallet_from_phrase(phrase):
    """Generate a BSC wallet address from a mnemonic phrase."""
    seed_bytes = Bip39SeedGenerator(phrase).Generate()
    bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BINANCE_SMART_CHAIN)
    bip44_acc = bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    return bip44_acc.PublicKey().ToAddress()

def get_bsc_balance(address, api_key):
    """Get the balance of a BSC address using BscScan API."""
    url = f'https://api.bscscan.com/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    balance_wei = int(data['result'])
    return balance_wei / (10 ** 18)  # Convert Wei to BNB

def start_searching_for_valid_phrases(word_list, num_words, api_key):
    """Start searching for valid secret phrases."""
    valid_phrases = []

    print("\nStarting search for valid secret phrases...\n")
    try:
        while True:
            phrase = generate_random_phrase(word_list, num_words)
            address = generate_wallet_from_phrase(phrase)
            balance = get_bsc_balance(address, api_key)
            print(f"Generated Address: {address}, Balance: {balance} BNB")
            if balance > 0:
                valid_phrases.append((phrase, address, balance))
                print(f"Valid secret phrase found: {phrase}, Address: {address}, Balance: {balance:.2f} BNB")
    except KeyboardInterrupt:
        print("\nSearch stopped by user.")
    
    # Show all collected valid phrases
    if valid_phrases:
        print("\nCollected valid secret phrases and their balances:")
        for i, (phrase, address, balance) in enumerate(valid_phrases, 1):
            print(f"{i}. {phrase} - Address: {address} - Balance: {balance:.2f} BNB")
    else:
        print("\nNo valid secret phrases found.")

def search_menu(num_words, word_list, api_key):
    """Display the search menu and handle user selection."""
    while True:
        print("\nSearch Menu:")
        print(f"1. Start Searching for {num_words}-word phrase")
        print("2. Main Menu")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            start_searching_for_valid_phrases(word_list, num_words, api_key)
        elif choice == '2':
            return
        else:
            print("\nInvalid choice. Please enter 1 or 2.\n")

def show_main_menu():
    """Display the main menu and handle user selection."""
    word_list = load_word_list('wordlist.txt')
    api_key = 'YOUR_BSCSCAN_API_KEY'  # Replace with your BscScan API key

    while True:
        print("Select an option:")
        print("1. Random 12-word Crypto Wallet Checker")
        print("2. Random 24-word Crypto Wallet Checker")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            search_menu(12, word_list, api_key)  # Call the search menu for 12-word phrases
        elif choice == '2':
            search_menu(24, word_list, api_key)  # Call the search menu for 24-word phrases
        elif choice == '3':
            print("\nExiting the program.\n")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    show_main_menu()

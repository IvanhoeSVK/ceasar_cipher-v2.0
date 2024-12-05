import string
import sys

alphabet = list(string.ascii_lowercase)

def ceasar_cipher(word, shift, action):
    result = ""
    shift = shift if action else -shift
    for letter in word:
        letter_index = alphabet.index(letter)
        new_index = (letter_index + shift) % 26
        result += alphabet[new_index]
    return result

def main():
    print("Welcome to Ceasar Cipher!\n")
    while True:
        choice = input("Enter 1 for encode or 2 for decode: ")
        if choice == "1" or choice == "2":
            while True:
                word = input("Enter word: ").strip().lower()
                if word.isalpha():
                    break
                else:
                    print("Enter only letters from alphabet!\n")
                    continue
            while True:
                shift = input("Enter shift: ")
                if shift.isdigit():
                    shift = int(shift)
                    break
                else:
                    print("Enter only numbers!\n")
                    continue
            action = choice == "1"    
            result = ceasar_cipher(word, shift, action)
            cipher = "Encode" if action else "Decode"
            print(f"{cipher} word is: {result}!\n")
        else:
            print("Enter only 1 or 2!\n")
            continue   
        while True:
            end = input("Do you want to continue? y/n ").lower().strip()
            if end in {"y", "n"}:
                if end == "y":
                    break
                else:
                    print("Exiting program...")
                    sys.exit()                          
            else:
                print("Enter only y or n!\n")
                continue
           
if __name__ == "__main__":
    main()
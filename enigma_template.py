# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: S.Winter.C
# created: 11.18.2024
# last update:  11.18.2024
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"
len(alphabet)


# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    key = (random.randint(0, 25))
    encoded_msg = ""
    msg = input("Please input a message to encode.").lower()
    for char in msg:
        msg_char = alphabet[(alphabet.index(char)+key) % 26]
        encoded_msg += msg_char
    print(f"Your message is now encoded as: '{encoded_msg}'. The key used to get this message is: {key}")
    pass


# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    x = 0
    while x == 0:
        try:
            f = open(input("What file will you be opening?"))
            awesome = f.count("x")
            print(f.read())
            print(awesome)

        except FileNotFoundError:
            print("File not found.")
    pass


# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    pass


# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
   pass


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()

# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: S.Winter.C
# created: 11.18.2024
# last update:  11.18.2024
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"


# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    # Inputs a key that must be a number, automatically makes it in range of 0-25 or makes it a random code
    key_select = input(f"Would you like to select your key? (y/N).").lower()
    if key_select == "y":
        key = int(input(f"Please select a key")) % 26
    else:
        key = (random.randint(0, 25))
    # variable for the encoded message and the input for the user to send the message they want encoded
    encoded_msg = ""
    msg = input("Please input a message to encode.").lower()
    # Encodes using alphabet index manipulation, then adds the letter. If the letter is a special char, add the special
    # char without index manipulation.
    for char in msg:
        try:
            msg_char = alphabet[(alphabet.index(char) + key) % 26]
            encoded_msg += msg_char
        except ValueError:
            encoded_msg += char
    # prints the new pretty encoded message
    print(f"Your message is now encoded as: '{encoded_msg}'. The key used to get this message is: {key}")
    pass


# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    # Asks for file to encode, loops back if the file isn't real.
    x = 0
    while x == 0:
        try:
            file_name = input("What file will you be encoding?")
            file = open(file_name, "r")
            key = (random.randint(0, 25))
            textfile = file.read().lower()
            encoded_file = ""
            x = 1
            # Same process as before, just instead within a now opened file.
            for char in textfile:
                try:
                    msg_char = alphabet[(alphabet.index(char) + key) % 26]
                    encoded_file += msg_char
                except ValueError:
                    encoded_file += char
            # Opens file to rewrite it then opens it as "read" to print for the user to view.
            file = open(file_name, "w")
            file.write(encoded_file)
            file = open(file_name, "r")
            print(f"Your newly encoded file now reads: {file.read()}\n"
                  f"A key of {key} was used for this.")
            file.close()

        except FileNotFoundError:
            print("File not found.")
    pass


# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    # Reverses the process from before, they input a file and subtract the key they know from the index in order to
    # decode the file.
    z = 0
    while z == 0:
        try:
            file_name = input("What file will you be decoding?")
            file = open(file_name, "r")
            z = 1
        except FileNotFoundError:
            print("File not found.")

    code_known = input("Is the key for the decoding known? (y/N)")
    if code_known == "y":
        x = 0
        while x == 0:
            y = 0
            while y == 0:
                try:
                    key = int(input("What key was used for this file"))
                    y = 1
                except ValueError:
                    print("Improper input.")
            textfile = file.read().lower()
            decoded_file = ""
            x = 1
            for char in textfile:
                try:
                    msg_char = alphabet[(alphabet.index(char) - key) % 26]
                    decoded_file += msg_char
                except ValueError:
                    decoded_file += char
            file = open(file_name, "w")
            file.write(decoded_file)
            file.close()
            print("Your file has been decoded.")
    # Sends them to the unknown key decoder if they don't know the key
    else:
        decode_unknown_key(file_name)
        pass


# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
    # use 48 letters for simplicity, function subtracts 8 every time if they're out of index range for the file.
    ex_len = 48
    # 'i' is alphabet length to sift through different keys
    file = open(filename, "r")
    textfile = file.read().lower()
    # Decodes excerpt from file and asks user if it's a correctly written excerpt.
    # If it is, decode full file and rewrite.
    for i in range(26):
        decodedfile = ""
        try:
            for char in textfile[:ex_len]:
                try:
                    msg_char = alphabet[(alphabet.index(char) + i) % 26]
                    decodedfile += msg_char
                except ValueError:
                    decodedfile += char
        except IndexError:
            ex_len = ex_len - 8
        print(decodedfile)
        corr_ident = input("Is this a correctly decoded excerpt? (y/N)")
        if corr_ident == "y":
            key = i
            decodedfile = ""
            for char in textfile:
                try:
                    msg_char = alphabet[(alphabet.index(char) + key) % 26]
                    decodedfile += msg_char
                except ValueError:
                    decodedfile += char
            file = open(filename, "w")
            file.write(decodedfile)
            file.close()
            print("Your file has been decoded.")
            break


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
    

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        index = alphabet.index(letter)
        new_index = (index + shift) % 26
        encrypted_text += alphabet[new_index]

    print(f"{text} has shifted {shift} and was encrypted to {encrypted_text}")

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        index = alphabet.index(letter)
        new_index = (index - shift) % 26
        decrypted_text += alphabet[new_index]

    print(f"{text} has shifted {shift} and was decrypted to {decrypted_text}")

def caesar(direction, text, shift):
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("No valid input was sgiven. Please enter 'encode' or 'decode'.\n")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(direction, text, shift)
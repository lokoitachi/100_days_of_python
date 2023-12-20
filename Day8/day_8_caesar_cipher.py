from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, plain_shift, plain_direction, flag_detector):
    if plain_direction.lower() == "encode":
        word_encripted = ""
        for letter in plain_text:
            if letter not in alphabet:
                word_encripted += letter
            else:
                position = alphabet.index(letter)
                new_position = position + plain_shift
                word_encripted += alphabet[new_position]
        print(f"The encoded text is {word_encripted}")

    elif plain_direction.lower() == "decode":
        word_decripted = ""
        for letter in plain_text:
            if letter not in alphabet:
                word_decripted += letter
            else:
                position_2 = alphabet.index(letter)
                old_position = position_2 - plain_shift
                word_decripted += alphabet[old_position]
        print(f"The decrypted word is {word_decripted}")
    else:
        print("That is not a valid option.")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    flag = True
    caesar(plain_text=text, plain_shift=shift, plain_direction=direction, flag_detector=flag)

    result = input("Type yes if you want to go again. Otherwise type no. ")
    if result == "no":
        should_continue = False



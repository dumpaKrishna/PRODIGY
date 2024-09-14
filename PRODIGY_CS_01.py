def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = ord(char) + shift_amount

            if char.islower():
                if shifted_char > ord('z'):
                    shifted_char -= 26
                elif shifted_char < ord('a'):
                    shifted_char += 26

            elif char.isupper():
                if shifted_char > ord('Z'):
                    shifted_char -= 26
                elif shifted_char < ord('A'):
                    shifted_char += 26

            result += chr(shifted_char)
        else:

            result += char

    return result

message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))

mode = input("Would you like to 'encrypt' or 'decrypt' the message? ").strip().lower()

if mode == 'encrypt':
    encrypted_message = caesar_cipher(message, shift_value, mode='encrypt')
    print(f"Encrypted message: {encrypted_message}")
elif mode == 'decrypt':
    decrypted_message = caesar_cipher(message, shift_value, mode='decrypt')
    print(f"Decrypted message: {decrypted_message}")
else:
    print("Invalid option. Please enter 'encrypt' or 'decrypt'.")

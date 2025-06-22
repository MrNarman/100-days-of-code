alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input('Type your message:\n').lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for char in original_text:
        shifted_position = alphabet.index(char) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"Here is your encoded result: {cipher_text}")
# TODO-1: Create a function called decrypt() that takes original_text and shift_amount as 2 inputs
# TODO-2: Inside the decrypt() function, shift each letter of the original_text backwards in the alphabet backwards by
#  the shift_amount and print the decrypted text
def decrypt(original_text, shift_amount):
    plain_text = ""
    for char in original_text:
        shifted_position = alphabet.index(char) - shift_amount
        shifted_position %= len(alphabet)
        plain_text += alphabet[shifted_position]

    print(f"Here is your encoded result: {plain_text}")

# TODO-3: Combine the 'encrypt' and 'decrypt' functions into a single function called caesar().
#  Use the value of the user chosen direction variable to determine which functionality to use. Call the Caesar
#  function instead of encrypt/decrypt and pass in all the three variables direction/text/shift
# encrypt(original_text=text, shift_amount=shift)
decrypt(original_text=text, shift_amount=shift)
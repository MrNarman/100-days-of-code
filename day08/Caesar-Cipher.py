from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input('Type your message:\n').lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, direction_to_take):
    cipher_text = ""
    for char in original_text:

        if direction_to_take == 'decode':
            shift_amount *= -1
        shifted_position = alphabet.index(char) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"Here is your {direction_to_take}d result: {cipher_text}")
caesar(original_text=text, shift_amount=shift, direction_to_take=direction)

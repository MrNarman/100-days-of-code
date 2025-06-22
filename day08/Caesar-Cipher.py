from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(original_text, shift_amount, direction_to_take):
    cipher_text = ""
    if direction_to_take == 'decode':
        shift_amount *= -1

    for char in original_text:
        if char not in alphabet:
            cipher_text += char
        else:
            shifted_position = alphabet.index(char) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Here is your {direction_to_take}d result: {cipher_text}")

# TODO-3: figure out to restart the program
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input('Type your message:\n').lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, direction_to_take=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
    if restart == 'no':
        should_continue = False
        print("Good Bye")


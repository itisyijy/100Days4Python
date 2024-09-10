# Day8 for 100Days4Python
# Project for Day8
import caesar_logo

alphabet_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(original, shift):
    result = ""
    for letter in original:
        if letter in alphabet_list:
            result += alphabet_list[(alphabet_list.index(letter) + shift) % len(alphabet_list)]
        else:
            result += letter
    return result

def decrypt(original, shift):
    result = ""
    for letter in original:
        if letter in alphabet_list:
            result += alphabet_list[(alphabet_list.index(letter) - shift) % len(alphabet_list)]
        else:
            result += letter
    return result

def caesar(direction, text, shift):
    result = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet_list:
            result += alphabet_list[(alphabet_list.index(letter) + shift) % len(alphabet_list)]
        else:
            result += letter
    return result

print(caesar_logo.caesar_logo)

restart = 'y'
while restart != 'n':
    print("\n----------------------------------------------------------------------------------")
    input_direction = input("[encode] for encrypt, [decode] for decrypt >>> ")
    input_text = input("Type your message >>> ").lower()
    input_shift = int(input("Type the shift amount >>> "))
    print(f"[{input_direction.upper()} RESULT] >>> {caesar(input_direction, input_text, input_shift)}")
    restart = input("[y] for RESTART | [n] for EXIT >>> ")

print("\n----------------------------------------------------------------------------------")
print("Good Bye.")
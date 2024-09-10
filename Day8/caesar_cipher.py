# Day8 for 100Days4Python
# Project for Day8
# Caesar Cipher

alphabet_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

#input_direction = input("[encode] for encrypt, [decode] for decrypt >>> ")
#input_text = input("Type your message >>> ")
#input_shift = int(input("Type the shift amount >>> "))

def encrypt(original, shift):
    result = ""
    for letter in original:
        if letter in alphabet_list:
            result += alphabet_list[(alphabet_list.index(letter) + shift) % 26]
        else:
            result += letter
    return result
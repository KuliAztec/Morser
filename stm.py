from mordict import MORSE_CODE_DICT

def string_to_morse(input_string):
    morse_string = ' '.join(MORSE_CODE_DICT[char] if char in MORSE_CODE_DICT else '?' for char in input_string)
    return morse_string
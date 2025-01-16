from mordict import MORSE_CODE_DICT

REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def morse_to_string(morse_code):
    words = morse_code.split('   ')  # Three spaces separate words in Morse code
    decoded_message = []
    
    for word in words:
        letters = word.split()  # One space separates letters in Morse code
        decoded_word = ''.join(REVERSE_MORSE_CODE_DICT.get(letter, '?') for letter in letters)
        decoded_message.append(decoded_word)
    
    return ' '.join(decoded_message)
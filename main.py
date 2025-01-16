# ...existing code...

def morse_to_string(morse_code):
    reverse_morse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    words = morse_code.split(' / ')
    decoded_message = ''
    for word in words:
        for morse_char in word.split():
            if morse_char in reverse_morse_dict:
                decoded_message += reverse_morse_dict[morse_char]
        decoded_message += ' '
    return decoded_message.strip()

# ...existing code...

import tkinter as tk
from tkinter import messagebox
from stm import string_to_morse
from mts import morse_to_string

def on_button_click(text_entry):
    input_text = text_entry.get("1.0", tk.END).strip()
    if input_text:
        morse_code = string_to_morse(input_text)
        messagebox.showinfo("Morse Code", morse_code)
        text_entry.clipboard_clear()
        text_entry.clipboard_append(morse_code)

def on_decode_button_click(text_entry):
    input_text = text_entry.get("1.0", tk.END).strip()
    if input_text:
        decoded_message = morse_to_string(input_text)
        messagebox.showinfo("Decoded Message", decoded_message)
        text_entry.clipboard_clear()
        text_entry.clipboard_append(decoded_message)

def create_text_input_window(root):
    text_window = tk.Toplevel(root)
    text_window.title("Text Input")

    text_frame = tk.LabelFrame(text_window, text="Text Input")
    text_frame.pack(pady=10, padx=10, fill="both", expand="yes")

    text_entry = tk.Text(text_frame, height=10, width=50)
    text_entry.pack(pady=10, padx=10)

    button_frame = tk.Frame(text_window)
    button_frame.pack(pady=10)

    button = tk.Button(button_frame, text="Convert to Morse Code", command=lambda: on_button_click(text_entry))
    button.pack(pady=10, padx=10, side=tk.LEFT)

    decode_button = tk.Button(button_frame, text="Decode Morse Code", command=lambda: on_decode_button_click(text_entry))
    decode_button.pack(pady=10, padx=10, side=tk.LEFT)

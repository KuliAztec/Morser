import tkinter as tk
from tkinter import messagebox, filedialog
import os
from stm import string_to_morse
from mts import morse_to_string

def on_button_click(file_entry):
    file_path = file_entry.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a file first.")
        return

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return

    morse_code = '\n'.join(string_to_morse(line.strip()) for line in lines)

    output_file_path = os.path.join(os.path.dirname(file_path), 'morse_code.txt')
    if os.path.exists(output_file_path):
        if not messagebox.askyesno("Overwrite?", f"File {output_file_path} exists. Overwrite?"):
            return

    with open(output_file_path, 'w') as output_file:
        output_file.write(morse_code)

    messagebox.showinfo("Success", f"Morse code saved to {output_file_path}")
    file_entry.clipboard_clear()
    file_entry.clipboard_append(morse_code)

def on_decode_button_click(file_entry):
    file_path = file_entry.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a file first.")
        return

    try:
        with open(file_path, 'r') as file:
            morse_code = file.read().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return

    decoded_message = morse_to_string(morse_code)
    messagebox.showinfo("Decoded Message", decoded_message)
    file_entry.clipboard_clear()
    file_entry.clipboard_append(decoded_message)

def browse_file(file_entry):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def create_file_input_window(root):
    file_window = tk.Toplevel(root)
    file_window.title("File Input")

    file_frame = tk.LabelFrame(file_window, text="File Input")
    file_frame.pack(pady=10, padx=10, fill="both", expand="yes")

    file_entry = tk.Entry(file_frame, width=50)
    file_entry.pack(pady=10, padx=10, side=tk.LEFT)

    browse_button = tk.Button(file_frame, text="Browse", command=lambda: browse_file(file_entry))
    browse_button.pack(pady=10, padx=10, side=tk.LEFT)

    button_frame = tk.Frame(file_window)
    button_frame.pack(pady=10)

    button = tk.Button(button_frame, text="Convert to Morse Code", command=lambda: on_button_click(file_entry))
    button.pack(pady=10, padx=10, side=tk.LEFT)

    decode_button = tk.Button(button_frame, text="Decode Morse Code", command=lambda: on_decode_button_click(file_entry))
    decode_button.pack(pady=10, padx=10, side=tk.LEFT)

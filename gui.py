import tkinter as tk
from texti import create_text_input_window
from filer import create_file_input_window

root = tk.Tk()
root.title("Simple GUI")

main_frame = tk.Frame(root)
main_frame.pack(pady=10)

text_input_button = tk.Button(main_frame, text="Open Text Input Window", command=lambda: create_text_input_window(root))
text_input_button.pack(pady=10, padx=10, side=tk.LEFT)

file_input_button = tk.Button(main_frame, text="Open File Input Window", command=lambda: create_file_input_window(root))
file_input_button.pack(pady=10, padx=10, side=tk.LEFT)

root.mainloop()
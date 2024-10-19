import tkinter as tk
from tkinter import filedialog
import sys


# script.py
def open_file():
    try:
        # initiating root
        root = tk.Tk()
        # bring the window upfront
        root.wm_attributes('-topmost', 0)
        # this suppress the tk window
        root.withdraw()
        # file dialog box
        file_path = filedialog.askopenfilenames(master=root)
        # Destroying window
        root.destroy()
        # Check if no files were selected
        if not file_path:
            return None  # Return None if no files are selected
        return file_path
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    Final_list = open_file()
    if Final_list is None:
        print(())
        sys.exit(0)
    elif isinstance(Final_list, str):
        # If an error occurred, print the error message and exit with code 1
        Error = sys.stderr.write(Final_list + '\n')
        print(Error)
        sys.exit(1)  # Exit with code 1
    else:
        # If there was no error, print the result
        print(Final_list)

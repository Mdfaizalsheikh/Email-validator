import tkinter as tk
from tkinter import messagebox
import re

class EmailValidator:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Validator")

        
        self.email_label = tk.Label(root, text="Enter Email:")
        self.email_label.pack(pady=10)
        self.email_entry = tk.Entry(root, width=40)
        self.email_entry.pack(pady=5)

        self.validate_button = tk.Button(root, text="Validate", command=self.validate_email)
        self.validate_button.pack(pady=20)

    def validate_email(self):
        email = self.email_entry.get()
        if self.is_valid_email(email):
            messagebox.showinfo("Result", "The email address is valid.")
        else:
            messagebox.showerror("Result", "The email address is not valid.")

    def is_valid_email(self, email):
        
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(regex, email)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailValidator(root)
    root.mainloop()

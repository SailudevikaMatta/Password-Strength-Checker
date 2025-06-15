#tkinter: Python’s standard library for building GUIs.
#messagebox: Used for showing pop-up alerts.
#zxcvbn: Evaluates password strength and gives feedback.

import tkinter as tk
from tkinter import messagebox
from zxcvbn import zxcvbn


#This function is triggered when the user clicks “Check Strength”.
#It retrieves the entered password from the entry widget.
#If nothing is entered, it shows a warning dialog.
def analyze_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return


#zxcvbn() analyzes the password and returns:
#a).A score from 0 (weak) to 4 (strong).
#b).A list of suggestions on how to improve.  
    result = zxcvbn(password)
    score = result['score']
    suggestions = result['feedback']['suggestions']
    

#Maps numeric score to human-readable text.
#Updates the label on the GUI to show the strength.
    strength_levels = {
        0: "Very Weak 😟",
        1: "Weak 😕",
        2: "Fair 😐",
        3: "Good 🙂",
        4: "Strong 💪"
    }

    strength_label.config(text=f"Strength: {strength_levels[score]}")


#If feedback exists, show suggestions.
#If no suggestions are needed (i.e., strong password), show positive message.    
    if suggestions:
        suggestions_text = "\n".join("- " + s for s in suggestions)
    else:
        suggestions_text = "Great password! No suggestions needed."

    suggestions_label.config(text=f"{suggestions_text}")


#GUI SETUP BELOW
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.configure(padx=20, pady=20)

# Input Label and Entry
label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack()

password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
password_entry.pack(pady=10)

# Check Button
check_button = tk.Button(root, text="Check Strength", command=analyze_password, font=("Arial", 12))
check_button.pack(pady=5)

# Strength Display
strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack(pady=10)

# Suggestions Display
suggestions_label = tk.Label(root, text="", font=("Arial", 10), justify="left", wraplength=350)
suggestions_label.pack()

# Start GUI Event Loop
root.mainloop()

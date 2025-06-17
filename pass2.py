# 👋 Let's build a friendly Password Strength Checker using Python's tkinter for GUI and zxcvbn for smart analysis

import tkinter as tk                          # GUI toolkit that comes with Python
from tkinter import messagebox               # To show warning popups
from zxcvbn import zxcvbn                    # Library that checks password strength (like a smart advisor)

# 🎯 Function to analyze password strength when button is clicked
def check_password_strength():
    user_password = password_input.get()     # Grab the password the user typed

    if not user_password:                    # If nothing is entered, gently remind the user
        messagebox.showwarning("Input Missing", "Oops! Please enter a password first.")
        return

    # Analyze the password and get a report
    password_analysis = zxcvbn(user_password)
    strength_score = password_analysis['score']                  # Strength score from 0 to 4
    improvement_tips = password_analysis['feedback']['suggestions']  # Suggestions to improve

    # Convert the score into a user-friendly message with emoji feedback
    score_to_text = {
        0: "Very Weak 😟",
        1: "Weak 😕",
        2: "Fair 😐",
        3: "Good 🙂",
        4: "Strong 💪"
    }

    # Show the password strength on screen
    strength_display.config(text=f"Strength: {score_to_text[strength_score]}")

    # If there are suggestions, display them nicely. If not, say it's a great password!
    if improvement_tips:
        tips_formatted = "\n".join(f"- {tip}" for tip in improvement_tips)
    else:
        tips_formatted = "✅ Great job! No improvements needed."

    suggestions_display.config(text=tips_formatted)


# 🖼️ Now let's build the GUI layout

# Create the main window
window = tk.Tk()
window.title("Password Strength Checker")     # Title of the app window
window.geometry("400x300")                    # Set window size
window.configure(padx=20, pady=20)            # Add a bit of spacing around the content

# Label asking the user to enter a password
prompt_label = tk.Label(window, text="Enter your password:", font=("Arial", 12))
prompt_label.pack()

# Entry box for the user to type their password (characters are hidden)
password_input = tk.Entry(window, show="*", font=("Arial", 12), width=30)
password_input.pack(pady=10)

# Button that checks the password when clicked
check_button = tk.Button(window, text="Check Strength", command=check_password_strength, font=("Arial", 12))
check_button.pack(pady=5)

# Label that shows the strength result
strength_display = tk.Label(window, text="", font=("Arial", 12, "bold"))
strength_display.pack(pady=10)

# Label that shows suggestions (if any)
suggestions_display = tk.Label(window, text="", font=("Arial", 10), justify="left", wraplength=350)
suggestions_display.pack()

# 🚀 Start the application — this keeps the window open and interactive
window.mainloop()

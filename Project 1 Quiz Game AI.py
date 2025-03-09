import tkinter as tk
from tkinter import messagebox

# Function to check answers and update score
def check_answer():
    global score, question_index
    answer = entry.get().lower()
    if answer == questions[question_index][1]:
        score += 1
        messagebox.showinfo("Result", "Correct answer!")
    else:
        messagebox.showinfo("Result", "Incorrect answer.")
    
    question_index += 1
    if question_index < len(questions):
        question_label.config(text=questions[question_index][0])
        entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Final Score", f"Your Total Score is: {score}\nYou got: {((score / len(questions)) * 100)}%")
        root.quit()

# Initialize variables
score = 0
question_index = 0
questions = [
    ("What is the full form of CPU?", "central processing unit"),
    ("What is the full form of GPU?", "graphics processing unit"),
    ("What is the full form of PSU?", "power supply unit"),
    ("What is the full form of UPS?", "uninterruptible power supply"),
    ("What is the full form of NPU?", "neural processing unit")
]

# Create main window
root = tk.Tk()
root.title("Computer Quiz Game")
root.geometry("400x300")

# Create and place widgets
question_label = tk.Label(root, text=questions[question_index][0])
question_label.pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit Answer", command=check_answer)
submit_button.pack(pady=20)

# Start the GUI loop
root.mainloop()

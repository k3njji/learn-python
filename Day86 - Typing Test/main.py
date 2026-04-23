import tkinter as tk
import random
import time

# ===== SAMPLE TEXTS =====
SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast requires practice and consistency every day.",
    "Python is a powerful programming language for many applications.",
    "Stay focused and keep improving your typing skills.",
    "Accuracy is more important than speed at the beginning."
]

# ===== GLOBAL STATE =====
start_time = None
time_left = 60
running = False

# ===== FUNCTIONS =====

def start_test():
    global start_time, running, time_left

    if not running:
        running = True
        start_time = time.time()
        time_left = 60
        update_timer()
        input_box.config(state="normal")
        input_box.delete("1.0", tk.END)


def update_timer():
    global time_left, running

    if running:
        timer_label.config(text=f"Time Left: {time_left}s")
        if time_left > 0:
            time_left -= 1
            root.after(1000, update_timer)
        else:
            end_test()


def end_test():
    global running
    running = False
    input_box.config(state="disabled")
    calculate_results()


def calculate_results():
    typed_text = input_box.get("1.0", tk.END).strip()
    original_text = text_label.cget("text")

    typed_words = typed_text.split()
    num_words = len(typed_words)

    # WPM
    wpm = num_words  # since test is 60 seconds

    # Accuracy
    correct_chars = 0
    for i in range(min(len(typed_text), len(original_text))):
        if typed_text[i] == original_text[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(original_text)) * 100 if original_text else 0

    result_label.config(
        text=f"WPM: {wpm} | Accuracy: {accuracy:.2f}%"
    )


def reset_test():
    global running
    running = False
    input_box.config(state="normal")
    input_box.delete("1.0", tk.END)
    result_label.config(text="")
    timer_label.config(text="Time Left: 60s")
    load_text()


def load_text():
    sample = random.choice(SAMPLE_TEXTS)
    text_label.config(text=sample)


# ===== UI =====
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("700x400")

# Sample text
text_label = tk.Label(root, text="", wraplength=650, font=("Arial", 14))
text_label.pack(pady=10)

# Input box
input_box = tk.Text(root, height=5, width=80, font=("Arial", 12))
input_box.pack(pady=10)

# Timer
timer_label = tk.Label(root, text="Time Left: 60s", font=("Arial", 12))
timer_label.pack()

# Result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Buttons
start_btn = tk.Button(root, text="Start", command=start_test)
start_btn.pack(side="left", padx=20, pady=20)

reset_btn = tk.Button(root, text="Reset", command=reset_test)
reset_btn.pack(side="right", padx=20, pady=20)

# Load initial text
load_text()

root.mainloop()
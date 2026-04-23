import tkinter as tk

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")

        self.text = tk.Text(root, font=("Arial", 14), wrap="word")
        self.text.pack(expand=True, fill="both")

        self.timer_label = tk.Label(root, text="Time left: 5", font=("Arial", 12))
        self.timer_label.pack()

        self.timeout = 5000
        self.remaining = 5
        self.timer_id = None

        # Bind keypress
        self.text.bind("<Key>", self.reset_timer)

        self.start_timer()

    def start_timer(self):
        self.remaining = 5
        self.update_label()
        self.schedule_delete()

    def reset_timer(self, event=None):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.start_timer()

    def schedule_delete(self):
        self.timer_id = self.root.after(1000, self.countdown)

    def countdown(self):
        self.remaining -= 1
        self.update_label()

        if self.remaining <= 0:
            self.text.delete("1.0", tk.END)
            self.timer_label.config(text="💀 You stopped. Text deleted.")
        else:
            self.schedule_delete()

    def update_label(self):
        self.timer_label.config(text=f"Time left: {self.remaining}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
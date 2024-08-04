import tkinter as tk


class LoadingScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Loading")
        self.geometry("200x100")
        self.resizable(False, False)
        self.label = tk.Label(self, text="Loading...", font=("Helvetica", 16))
        self.label.pack(expand=True)
        self.spinner = tk.Label(self, text="|", font=("Helvetica", 24))
        self.spinner.pack(expand=True)

        self.animate_spinner()

    def animate_spinner(self):
        self.spinner.after(100, self.rotate_spinner)

    def rotate_spinner(self):
        current_text = self.spinner.cget("text")
        next_text = {
            "|": "/",
            "/": "-",
            "-": "\\",
            "\\": "|"
        }[current_text]
        self.spinner.config(text=next_text)
        self.animate_spinner()
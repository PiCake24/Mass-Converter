import tkinter as tk
from tkinter import PhotoImage

class RoundCheckButton(tk.Frame):
    def __init__(self, parent, checked_image, unchecked_image, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.checked_image = PhotoImage(file=checked_image)
        self.unchecked_image = PhotoImage(file=unchecked_image)
        self.is_checked = tk.BooleanVar()

        self.canvas = tk.Canvas(self, width=50, height=50, highlightthickness=0)
        self.canvas.pack()

        self.canvas.create_image(25, 25, image=self.unchecked_image, tags="button")

        self.canvas.bind("<Button-1>", self.toggle)

    def toggle(self, event=None):
        self.is_checked.set(not self.is_checked.get())
        self.update_image()

    def update_image(self):
        if self.is_checked.get():
            self.canvas.itemconfig("button", image=self.checked_image)
        else:
            self.canvas.itemconfig("button", image=self.unchecked_image)

    def get(self):
        return self.is_checked.get()

    def set(self, value):
        self.is_checked.set(value)
        self.update_image()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")

    # Replace 'checked.png' and 'unchecked.png' with the paths to your icon images
    checked_image = 'checked.png'
    unchecked_image = 'unchecked.png'

    custom_checkbutton = RoundCheckButton(root, checked_image, unchecked_image)
    custom_checkbutton.pack(pady=20)

    def print_state():
        print("Checked" if custom_checkbutton.get() else "Unchecked")

    check_state_button = tk.Button(root, text="Check State", command=print_state)
    check_state_button.pack(pady=10)

    root.mainloop()

import tkinter as tk

from Gui.Gui import ThreePanelsGUI

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    app = ThreePanelsGUI(root)
    root.mainloop()

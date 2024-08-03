import tkinter as tk

from Data.Champion import Champion
from Data.Skin import Skin
from Gui.Gui import ThreePanelsGUI

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    championList = []
    champion = Champion("Akali", [Skin(1, 2, True), Skin(2, 25, False), Skin(5, 5, True)], True)
    championList.append(champion)
    champion = Champion("Leona", [Skin(1, 2, False)], True)
    championList.append(champion)

    app = ThreePanelsGUI(root, championList)
    root.mainloop()
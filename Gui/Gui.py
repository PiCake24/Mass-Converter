import os
import threading
import time
import tkinter as tk
from tkinter import scrolledtext, filedialog

from Data.SystemPaths import SystemPaths
from Gui.LoadingScreenGui import LoadingScreen
from MainControl import Control
from MainControl.Startup import startup


class ThreePanelsGUI:
    def __init__(self, root):
        self.thread = None
        self.root = root
        self.root.title("Mass-Converter")
        self.root.geometry("1000x800")
        self.champion_list = []
        self.system_paths = SystemPaths("", "", "")

        self.right_checkbuttons = []
        self.file_path_vars = [tk.StringVar() for _ in range(3)]
        self.stop_event = threading.Event()

        # Show loading screen
        self.loading_screen = LoadingScreen(self.root)
        self.root.update()

        # Perform initialization in a separate thread
        self.thread2 = threading.Thread(target=self.initialize_gui)
        self.thread2.start()

    def initialize_gui(self):
        startup(self)

        # Close the loading screen and show the main GUI
        self.root.after(0, self.close_loading_screen)

    def create_main_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create the top panel with buttons
        self.top_panel = tk.Frame(self.root, bg="lightblue", height=50)
        self.top_panel.pack(fill=tk.X)
        self.top_panel.pack_propagate(False)

        # Options button
        self.options_button = tk.Button(self.top_panel, text="Options", command=self.show_options_gui)
        self.options_button.pack(side=tk.LEFT, anchor=tk.W, padx=20, pady=10)

        # Select Champions button
        self.select_champions_button = tk.Button(self.top_panel, text="Select Champions", command=self.select_champions)
        self.select_champions_button.pack(side=tk.LEFT, anchor=tk.W, padx=20, pady=10)

        # Create the middle panel with two scrollable text areas
        self.middle_panel = tk.Frame(self.root, bg="lightgreen", height=500)
        self.middle_panel.pack(fill=tk.X)
        self.middle_panel.pack_propagate(False)

        # Left scrollable frame with multiple sub-panels
        self.left_scrollframe = tk.Frame(self.middle_panel, bg="lightyellow", width=500)
        self.left_scrollframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.left_scrollframe.pack_propagate(False)
        self.left_canvas = tk.Canvas(self.left_scrollframe, bg="lightyellow")
        self.left_scrollbar = tk.Scrollbar(self.left_scrollframe, orient="vertical", command=self.left_canvas.yview)
        self.left_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.left_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.left_canvas.configure(yscrollcommand=self.left_scrollbar.set)

        self.left_inner_frame = tk.Frame(self.left_canvas, bg="lightyellow")
        self.left_canvas.create_window((0, 0), window=self.left_inner_frame, anchor="nw")
        self.left_inner_frame.bind("<Configure>",
                                   lambda event: self.left_canvas.configure(scrollregion=self.left_canvas.bbox("all")))

        # Add buttons with checkboxes to the left side
        self.left_checkbuttons = []
        self.left_panels = []
        self.panel_positions = {}  # Store original positions
        for i, champion in enumerate(self.champion_list):
            button_frame = tk.Frame(self.left_inner_frame, bg="lightblue", pady=10)
            button_frame.pack(fill=tk.X, padx=10, pady=5)
            var1 = tk.IntVar(value=0)
            checkbutton1 = tk.Checkbutton(button_frame, text=f"Activate", variable=var1, onvalue=1, offvalue=0)
            checkbutton1.pack(side=tk.LEFT, padx=5)
            button = tk.Button(button_frame, text=champion.champion, bg="lightblue",
                               command=lambda i=i: self.show_skins(i))
            button.pack(side=tk.LEFT, padx=5)

            self.left_checkbuttons.append(var1)
            self.left_panels.append(button_frame)
            self.panel_positions[button_frame] = i

        # Right scrollable frame with multiple sub-panels
        self.right_scrollframe = tk.Frame(self.middle_panel, bg="lightgrey", width=500)
        self.right_scrollframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.right_scrollframe.pack_propagate(False)
        self.right_canvas = tk.Canvas(self.right_scrollframe, bg="lightgrey")
        self.right_scrollbar = tk.Scrollbar(self.right_scrollframe, orient="vertical", command=self.right_canvas.yview)
        self.right_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.right_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.right_canvas.configure(yscrollcommand=self.right_scrollbar.set)

        self.right_inner_frame = tk.Frame(self.right_canvas, bg="lightgrey")
        self.right_canvas.create_window((0, 0), window=self.right_inner_frame, anchor="nw")
        self.right_inner_frame.bind("<Configure>", lambda event: self.right_canvas.configure(
            scrollregion=self.right_canvas.bbox("all")))

        # Create the bottom panel with log and buttons
        self.bottom_panel = tk.Frame(self.root, bg="lightcoral", height=250)
        self.bottom_panel.pack(fill=tk.X, padx=20, pady=20)
        self.bottom_panel.pack_propagate(False)

        # Scrollable text area (log)
        self.log_area = scrolledtext.ScrolledText(self.bottom_panel, wrap=tk.WORD, width=40, height=10)
        self.log_area.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Create the interrupt and start buttons
        self.interrupt_button = tk.Button(self.bottom_panel, text="Interrupt", command=self.stop_program)
        self.interrupt_button.pack(side=tk.RIGHT, padx=20, pady=10)
        self.start_button = tk.Button(self.bottom_panel, text="Start", command=self.start_program)
        self.start_button.pack(side=tk.RIGHT, padx=20, pady=10)

    def start_program(self):
        self.start_button.config(state=tk.DISABLED)
        # if self.thread and self.thread.is_alive():
        #    self.log_area.insert(tk.END, "A task is already running. Please wait for it to finish or interrupt it.\n")
        #    return

        self.stop_event.clear()  # Clear the stop event flag
        self.thread = threading.Thread(target=self.execute_control)
        self.thread.start()

    def stop_program(self):
        self.stop_event.set()
        self.start_button.config(state=tk.NORMAL)

    def execute_control(self):
        # Function to execute Control.pys control method
        def log_callback(message):
            self.log_area.insert(tk.END, message + "\n")
            self.log_area.see(tk.END)  # Scroll to the bottom
            self.root.update_idletasks()  # Update the GUI

        try:
            Control.control(log_callback, self.stop_event, self.champion_list, "pathvariables")
            self.start_button.config(state=tk.NORMAL)
        except Exception as e:
            self.log_area.insert(tk.END, f"Error: {str(e)}\n")
            self.log_area.see(tk.END)  # Scroll to the bottom
            self.start_button.config(state=tk.NORMAL)

    def show_skins(self, champion_index):
        # Clear the right_inner_frame
        for widget in self.right_inner_frame.winfo_children():
            widget.destroy()

        # Add sub-panels for the skins of the selected champion
        selected_champion = self.champion_list[champion_index]
        for i, skin in enumerate(selected_champion.skin_list):
            sub_panel = tk.Frame(self.right_inner_frame, bg="lightblue", pady=10)
            sub_panel.pack(fill=tk.X, padx=10, pady=5)

            var1 = tk.IntVar(value=0)
            checkbutton1 = tk.Checkbutton(sub_panel, text=f"Activate", variable=var1, onvalue=1, offvalue=0)
            checkbutton1.pack(side=tk.LEFT, padx=5)
            text = tk.Label(sub_panel, text=f"skin {skin.skin_number}", bg="lightblue")
            text.pack(side=tk.LEFT, padx=5)

            self.right_checkbuttons.append(var1)

        # Update the right canvas scroll region
        self.right_inner_frame.update_idletasks()
        self.right_canvas.configure(scrollregion=self.right_canvas.bbox("all"))

    def close_loading_screen(self):
        self.loading_screen.destroy()
        # Continue with showing the main GUI
        self.root.deiconify()

        self.create_main_gui()

    def show_options_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create the top panel with back button
        self.top_panel = tk.Frame(self.root, bg="lightblue", height=50)
        self.top_panel.pack(fill=tk.X)
        self.top_panel.pack_propagate(False)

        # Back button
        self.back_button = tk.Button(self.top_panel, text="Back", command=self.create_main_gui)
        self.back_button.pack(side=tk.LEFT, anchor=tk.W, padx=20, pady=10)

        # Create the file choosers
        self.file_choosers_panel = tk.Frame(self.root, bg="lightgreen")
        self.file_choosers_panel.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Riot Path
        self.riot_path_label = tk.Label(self.file_choosers_panel, text="Riot Path:", bg="lightgreen")
        self.riot_path_label.pack(anchor=tk.W, pady=5)
        self.league_path_entry = tk.Entry(self.file_choosers_panel, width=50)
        self.league_path_entry.pack(anchor=tk.W, pady=5)
        self.league_path_entry.insert(0, self.system_paths.league_path)
        self.riot_path_button = tk.Button(self.file_choosers_panel, text="Choose League Path",
                                          command=self.choose_riot_path)
        self.riot_path_button.pack(anchor=tk.W, pady=5)

        # Ritobin Path
        self.ritobin_path_label = tk.Label(self.file_choosers_panel, text="Ritobin Path:", bg="lightgreen")
        self.ritobin_path_label.pack(anchor=tk.W, pady=5)
        self.ritobin_path_entry = tk.Entry(self.file_choosers_panel, width=50)
        self.ritobin_path_entry.pack(anchor=tk.W, pady=5)
        self.ritobin_path_entry.insert(0, self.system_paths.ritobin_path)
        self.ritobin_path_button = tk.Button(self.file_choosers_panel, text="Choose Ritobin Path",
                                             command=self.choose_ritobin_path)
        self.ritobin_path_button.pack(anchor=tk.W, pady=5)

        # Root Path
        self.root_path_label = tk.Label(self.file_choosers_panel, text="Root Path:", bg="lightgreen")
        self.root_path_label.pack(anchor=tk.W, pady=5)
        self.root_path_entry = tk.Entry(self.file_choosers_panel, width=50)
        self.root_path_entry.pack(anchor=tk.W, pady=5)
        self.root_path_entry.insert(0, self.system_paths.root_path)
        self.root_path_button = tk.Button(self.file_choosers_panel, text="Choose Root Path",
                                          command=self.choose_root_path)
        self.root_path_button.pack(anchor=tk.W, pady=5)

    def choose_riot_path(self):
        path = filedialog.askopenfilename()
        if path:
            path = os.path.normpath(path)
            self.system_paths.riot_path = path
            self.league_path_entry.delete(0, tk.END)
            self.league_path_entry.insert(0, path)

    def choose_ritobin_path(self):
        path = filedialog.askopenfilename()
        if path:
            path = os.path.normpath(path)
            self.system_paths.ritobin_path = path
            self.ritobin_path_entry.delete(0, tk.END)
            self.ritobin_path_entry.insert(0, path)

    def choose_root_path(self):
        path = filedialog.askdirectory()
        if path:
            path = os.path.normpath(path)
            self.system_paths.root_path = path
            self.root_path_entry.delete(0, tk.END)
            self.root_path_entry.insert(0, path)

    def select_champions(self): #TODO
        for widget in self.root.winfo_children():
            widget.destroy()
        self.top_panel = tk.Frame(self.root, bg="lightblue", height=50)
        self.top_panel.pack(fill=tk.X)
        self.top_panel.pack_propagate(False)

        # Select Champions button
        self.select_champions_button = tk.Button(self.top_panel, text="Select Champions", command=self.select_champions)
        self.select_champions_button.pack(side=tk.LEFT, anchor=tk.W, padx=20, pady=10)

        # Create the middle panel with two scrollable text areas
        self.middle_panel = tk.Frame(self.root, bg="lightgreen", height=500)
        self.middle_panel.pack(fill=tk.X)
        self.middle_panel.pack_propagate(False)

        # Left scrollable frame with multiple sub-panels
        self.left_scrollframe = tk.Frame(self.middle_panel, bg="lightyellow", width=500)
        self.left_scrollframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.left_scrollframe.pack_propagate(False)
        self.left_canvas = tk.Canvas(self.left_scrollframe, bg="lightyellow")
        self.left_scrollbar = tk.Scrollbar(self.left_scrollframe, orient="vertical", command=self.left_canvas.yview)
        self.left_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.left_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.left_canvas.configure(yscrollcommand=self.left_scrollbar.set)

        self.left_inner_frame = tk.Frame(self.left_canvas, bg="lightyellow")
        self.left_canvas.create_window((0, 0), window=self.left_inner_frame, anchor="nw")
        self.left_inner_frame.bind("<Configure>",
                                   lambda event: self.left_canvas.configure(scrollregion=self.left_canvas.bbox("all")))

        # Add buttons with checkboxes to the left side
        self.left_checkbuttons = []
        self.left_panels = []
        self.panel_positions = {}  # Store original positions
        for i, champion in enumerate(self.champion_list):
            button_frame = tk.Frame(self.left_inner_frame, bg="lightblue", pady=10)
            button_frame.pack(fill=tk.X, padx=10, pady=5)
            var1 = tk.IntVar(value=0)
            checkbutton1 = tk.Checkbutton(button_frame, text=f"Activate", variable=var1, onvalue=1, offvalue=0)
            checkbutton1.pack(side=tk.LEFT, padx=5)
            button = tk.Button(button_frame, text=champion.champion, bg="lightblue",
                               command=lambda i=i: self.show_skins(i))
            button.pack(side=tk.LEFT, padx=5)

            self.left_checkbuttons.append(var1)
            self.left_panels.append(button_frame)
            self.panel_positions[button_frame] = i

        # Right scrollable frame with multiple sub-panels
        self.right_scrollframe = tk.Frame(self.middle_panel, bg="lightgrey", width=500)
        self.right_scrollframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.right_scrollframe.pack_propagate(False)
        self.right_canvas = tk.Canvas(self.right_scrollframe, bg="lightgrey")
        self.right_scrollbar = tk.Scrollbar(self.right_scrollframe, orient="vertical", command=self.right_canvas.yview)
        self.right_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.right_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.right_canvas.configure(yscrollcommand=self.right_scrollbar.set)

        self.right_inner_frame = tk.Frame(self.right_canvas, bg="lightgrey")
        self.right_canvas.create_window((0, 0), window=self.right_inner_frame, anchor="nw")
        self.right_inner_frame.bind("<Configure>", lambda event: self.right_canvas.configure(
            scrollregion=self.right_canvas.bbox("all")))
    def toggle_panel_visibility(self, panel, var, idx):
        if var.get() == 1 and not self.show_hidden_var.get():
            panel.pack_forget()
        else:
            self.repack_panels()

    def repack_panels(self):
        # Clear all panels from the container
        for panel in self.left_panels:
            panel.pack_forget()

        # Re-add panels based on their original positions and visibility states
        for panel in sorted(self.left_panels, key=lambda p: self.panel_positions[p]):
            if self.show_hidden_var.get() or not self.left_checkbuttons[self.panel_positions[panel]][1].get():
                panel.pack(fill=tk.X, padx=10, pady=5)

    def toggle_show_hidden(self):
        self.repack_panels()
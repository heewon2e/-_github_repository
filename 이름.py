import tkinter as tk
from tkinter import messagebox

class WordFinderGUI:
    def __init__(self, root):
        self.root = root
        root.title("Word Finder")

        self.label_text = tk.Label(root, text="Text:")
        self.label_text.grid(row=0, column=0, padx=10, pady=5)
        self.entry_text = tk.Text(root, height=10, width=40)
        self.entry_text.grid(row=0, column=1, padx=10, pady=5)

        self.label_word = tk.Label(root, text="Word:")
        self.label_word.grid(row=1, column=0, padx=10, pady=5)
        self.entry_word = tk.Entry(root)
        self.entry_word.grid(row=1, column=1, padx=10, pady=5)

        self.button_find = tk.Button(root, text="Find", command=self.find_word)
        self.button_find.grid(row=2, column=0, pady=5)

        self.button_clear = tk.Button(root, text="Clear", command=self.clear_fields)
        self.button_clear.grid(row=2, column=1, pady=5)

        self.button_quit = tk.Button(root, text="Quit", command=root.quit)
        self.button_quit.grid(row=2, column=2, pady=5)

    def find_word(self):
        text = self.entry_text.get("1.0", tk.END)
        word = self.entry_word.get()
        if not word:
            messagebox.showwarning("Warning", "Please enter a word to find.")
            return

        start = "1.0"
        locations = []
        while True:
            start = self.entry_text.search(word, start, stopindex=tk.END)
            if not start:
                break
            end = f"{start}+{len(word)}c"
            locations.append(start)
            start = end

        if locations:
            messagebox.showinfo("Found", f"Word found at positions: {', '.join(locations)}")
        else:
            messagebox.showinfo("Not Found", "Word not found.")

    def clear_fields(self):
        self.entry_text.delete("1.0", tk.END)
        self.entry_word.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = WordFinderGUI(root)
    root.mainloop()

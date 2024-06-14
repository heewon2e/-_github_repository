import tkinter as tk
from tkinter import messagebox

class WordBookApp:
    def __init__(self, root):
        self.root = root
        root.title("Word Book")

        # Dictionary to store words and their meanings
        self.word_dict = {}

        # Word entry
        self.label_word = tk.Label(root, text="단어:")
        self.label_word.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_word = tk.Entry(root)
        self.entry_word.grid(row=0, column=1, padx=10, pady=5)

        # Buttons next to word entry
        self.button_search = tk.Button(root, text="검색", command=self.search_word)
        self.button_search.grid(row=0, column=2, padx=5, pady=5)

        self.button_add = tk.Button(root, text="추가", command=self.add_word)
        self.button_add.grid(row=0, column=3, padx=5, pady=5)

        # Meaning entry
        self.label_meaning = tk.Label(root, text="뜻:")
        self.label_meaning.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_meaning = tk.Entry(root, width=50)
        self.entry_meaning.grid(row=1, column=1, columnspan=3, padx=10, pady=5)

        # Buttons at the bottom
        self.button_clear = tk.Button(root, text="초기화", command=self.clear_fields)
        self.button_clear.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.button_quit = tk.Button(root, text="종료", command=root.quit)
        self.button_quit.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    def add_word(self):
        word = self.entry_word.get().strip()
        meaning = self.entry_meaning.get().strip()

        if word and meaning:
            self.word_dict[word] = meaning
            messagebox.showinfo("추가 확인", f"단어 '{word}'를 추가했습니다.")
            self.clear_fields()
        else:
            messagebox.showwarning("입력 오류", "단어와 뜻을 모두 입력하세요.")

    def search_word(self):
        word = self.entry_word.get().strip()
        if word in self.word_dict:
            meaning = self.word_dict[word]
            messagebox.showinfo("검색 결과", f"단어: {word}\n뜻: {meaning}")
        else:
            messagebox.showwarning("검색 오류", f"단어 '{word}'를 찾을 수 없습니다.")

    def clear_fields(self):
        self.entry_word.delete(0, tk.END)
        self.entry_meaning.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = WordBookApp(root)
    root.mainloop()



import tkinter as tk
from tkinter import messagebox
import os

class WordBookApp:
    def __init__(self, root):
        self.root = root
        root.title("Word Book")

        # Dictionary to store words and their meanings
        self.word_dict = self.load_words()

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

        self.button_quit = tk.Button(root, text="종료", command=self.quit_program)
        self.button_quit.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    def load_words(self):
        if os.path.exists("words.txt"):
            with open("words.txt", "r", encoding="utf-8") as file:
                word_dict = {}
                for line in file:
                    word, meaning = line.strip().split(':')
                    word_dict[word] = meaning
                return word_dict
        else:
            return {}

    def save_words(self):
        with open("words.txt", "w", encoding="utf-8") as file:
            for word, meaning in self.word_dict.items():
                file.write(f"{word}:{meaning}\n")

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

    def quit_program(self):
        self.save_words()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordBookApp(root)
    root.mainloop()

#단어 입력 필드: label_word와 entry_word를 사용하여 단어를 입력
#검색 및 추가 버튼: 단어 입력 필드 옆에 button_search와 button_add를 나란히 배치
#뜻 입력 필드: label_meaning과 entry_meaning을 사용하여 뜻을 입력. entry_meaning은 width=50으로 설정하여 길게 배치
# 초기화 및 종료 버튼: 왼쪽 하단에 button_clear와 button_quit를 나란히 배치
# self.word_dict 단어와 뜻의 쌍을 저장하는 딕셔너리
#load_words 메서드는 words.txt 파일이 존재하면 내용을 불러와 self.word_dict에 저장. 파일이 없으면 빈 딕셔너리를 반환
#파일에 단어를 저장: save_words 메서드는 self.word_dict의 내용을 words.txt 파일에 저장
#종료 시 파일 저장: quit_program 메서드는 save_words를 호출하여 파일에 단어를 저장한 후 프로그램을 종료


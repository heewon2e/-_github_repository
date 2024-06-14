import tkinter as tk
from tkinter import messagebox

class UserInfoApp:
    def __init__(self, root):
        self.root = root
        root.title("User Information Form")

        # Name entry
        self.label_name = tk.Label(root, text="이름:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        # Grade selection (Radio buttons)
        self.label_grade = tk.Label(root, text="학년:")
        self.label_grade.grid(row=1, column=0, padx=10, pady=5)

        self.grade_var = tk.StringVar()
        self.grade_var.set(None)

        grades = ["1", "2", "3", "4"]
        for idx, grade in enumerate(grades):
            radio = tk.Radiobutton(root, text=grade, variable=self.grade_var, value=grade)
            radio.grid(row=1, column=idx + 1, padx=5, pady=5)

        # Hobbies selection (Check buttons)
        self.label_hobbies = tk.Label(root, text="취미:")
        self.label_hobbies.grid(row=2, column=0, padx=10, pady=5)

        self.hobbies_vars = {}
        hobbies = ["영화시청", "음악감상", "사진찍기", "운동"]
        for idx, hobby in enumerate(hobbies):
            var = tk.BooleanVar()
            chk = tk.Checkbutton(root, text=hobby, variable=var)
            chk.grid(row=2, column=idx + 1, padx=5, pady=5)
            self.hobbies_vars[hobby] = var

        # Buttons
        self.button_submit = tk.Button(root, text="입력", command=self.submit)
        self.button_submit.grid(row=3, column=0, pady=10)

        self.button_quit = tk.Button(root, text="종료", command=root.quit)
        self.button_quit.grid(row=3, column=1, pady=10)

    def submit(self):
        name = self.entry_name.get()
        grade = self.grade_var.get()
        selected_hobbies = [hobby for hobby, var in self.hobbies_vars.items() if var.get()]

        if not name:
            messagebox.showwarning("Input Error", "이름을 입력하세요.")
            return

        if not grade:
            messagebox.showwarning("Input Error", "학년을 선택하세요.")
            return

        if not selected_hobbies:
            messagebox.showwarning("Input Error", "취미를 하나 이상 선택하세요.")
            return

        print(name)
        print(grade)
        for hobby in selected_hobbies:
            print(hobby)

if __name__ == "__main__":
    root = tk.Tk()
    app = UserInfoApp(root)
    root.mainloop()

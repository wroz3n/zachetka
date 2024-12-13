import tkinter as tk
from tkinter import simpledialog, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("You weak!")
        self.root.geometry("400x200")
        self.label = tk.Label(root, text="МДК-01.01", font=("Arial", 24))
        self.label.pack(expand=True)

        # Блокируем возможность закрыть окно
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind("<Unmap>", self.on_minimize)

    def on_closing(self):
        self.ask_password()

    def on_minimize(self, event):
        self.ask_password()

    def ask_password(self):
        password = simpledialog.askstring("Пароль", "Введите пароль для закрытия окна:")
        if password == "111":
            self.root.destroy()
        else:
            messagebox.showerror("Ошибка", "Неверный пароль!")


if __name__ == "__main__":
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: None) # Disable closing the window
    root.attributes("-toolwindow", 1) # Hide from task manager
    app = App(root)
    root.mainloop()

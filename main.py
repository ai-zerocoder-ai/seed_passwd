import tkinter as tk
from tkinter import messagebox
import random
import string


# Функция для генерации пароля
def generate_password():
    try:
        length = int(entry_password_length.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Необходимо ввести количество символов!")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    output_password.config(state=tk.NORMAL)
    output_password.delete(0, tk.END)
    output_password.insert(0, password)

# Функция для генерации парольной фразы
def generate_passphrase():
    try:
        words_count = int(entry_phrase_words.get())
        if words_count <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Необходимо ввести количество слов!")
        return

    # Увеличенный список слов
    words = [
        "apple", "banana", "orange", "elephant", "giraffe", "tiger", "house", "car", "bicycle", "river",
        "mountain", "cloud", "forest", "laptop", "keyboard", "window", "coffee", "phone", "book", "train",
        "sun", "moon", "star", "tree", "flower", "water", "fire", "earth", "wind", "sky",
        "cat", "dog", "bird", "fish", "boat", "plane", "road", "bridge", "computer", "mouse",
        "pen", "paper", "table", "chair", "cup", "bottle", "shoe", "hat", "door", "wall"
    ]

    passphrase = ' '.join(random.choice(words) for _ in range(words_count))
    output_passphrase.config(state=tk.NORMAL)
    output_passphrase.delete(1.0, tk.END)
    output_passphrase.insert(tk.END, passphrase)

# Создаем главное окно
root = tk.Tk()
root.title("Генератор паролей и парольных фраз")
root.geometry("400x400")

# Виджеты для генерации пароля
label_password = tk.Label(root, text="Введите количество символов для пароля:")
label_password.pack(pady=5)

entry_password_length = tk.Entry(root)
entry_password_length.pack(pady=5)

button_generate_password = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
button_generate_password.pack(pady=5)

output_password = tk.Entry(root, width=40)
output_password.pack(pady=5)

# Виджеты для генерации парольной фразы
label_phrase = tk.Label(root, text="Введите количество слов для парольной фразы:")
label_phrase.pack(pady=5)

entry_phrase_words = tk.Entry(root)
entry_phrase_words.pack(pady=5)

button_generate_passphrase = tk.Button(root, text="Сгенерировать парольную фразу", command=generate_passphrase)
button_generate_passphrase.pack(pady=5)

# Используем Text вместо Entry для отображения большого количества слов
output_passphrase = tk.Text(root, height=4, width=40, wrap=tk.WORD)
output_passphrase.pack(pady=5)

# Запуск главного цикла приложения
root.mainloop()

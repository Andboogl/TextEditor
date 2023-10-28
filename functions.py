from PyQt6.QtWidgets import QFileDialog, QMessageBox
import os


def block_widgets(*args):
    """Блокує всі віджети, що вказані у args."""
    for widget in args:
        widget.setEnabled(False)


def unblock_widgets(*args):
    """Розблоковує всі віджети, що вказані у args."""
    for widget in args:
        widget.setEnabled(True)


def get_file_text(file_path):
    """Отримати текст файла який знаходиться за шляхом file_path."""
    with open(file_path) as f:
        return f.read()


def get_user_file(main_window):
    """Попросити користувача вибрати файл."""
    path = QFileDialog.getOpenFileName(main_window, 'Виберіть файл', '/Users')[0]
    return path


def get_user_folder(main_window):
    """Попросити користувача вибрати папку."""
    path = QFileDialog.getExistingDirectory(main_window, 'Виберіть папку', '/Users')
    return path

def show_message(window, text):
    """Показує QMessageBox на вікні window з текстом text."""
    messageBox = QMessageBox(window)
    messageBox.setText(text)
    messageBox.exec()

def write_text(file, text):
    """Записує текст text у файл за шляхом file."""
    if os.path.exists(file):
        with open(file, 'w') as f:
            f.write(text)
    
    # Якщо користувач видалив файл під час роботи программи, та хоче зберігти текст
    else:
        with open(file, 'x') as f:
            f.write(text)

def create_file(path):
    """Створює файл за шляхом path."""
    with open(path, 'x') as f:
        f.write('Цей файл створений программою TextEditor. Ви можете видалити цей напис.')

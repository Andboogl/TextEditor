from PyQt6.QtWidgets import QMessageBox
import os


def get_file_text(path):
    with open(path) as f:
        return f.read()


def save(path, text):
    if os.path.exists(path):
        with open(path, 'w') as f:
            f.write(text)

    else:
        with open(path, 'x') as f:
            f.write(text)


def show_message(window, text, type=None):
    messageBox = QMessageBox(window)
    messageBox.setText(text)

    if type == 1:
        messageBox.setIcon(QMessageBox.Icon.Information)
    
    elif type == 2:
        messageBox.setIcon(QMessageBox.Icon.Warning)

    messageBox.exec()

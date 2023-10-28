from windows.main_window import Ui_MainWindow
from file_creating import FileCreatingWindow
from PyQt6 import QtWidgets
from functions import *
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        QtWidgets.QMainWindow.__init__(self)

        self.file = None

        # Загружаємо віджети
        self.widgets = Ui_MainWindow()
        self.widgets.setupUi(self)

        # Блокуємо поки-що непотрібні віджети
        block_widgets(
            self.widgets.text_editor,
            self.widgets.clear,
            self.widgets.save_changes
        )

        # Встановлюємо дії до кнопок
        self.widgets.chose_path.clicked.connect(self.chose_file)
        self.widgets.clear.clicked.connect(self.clear)
        self.widgets.save_changes.clicked.connect(self.save_changes)
        self.widgets.create_file.clicked.connect(self.open_file_creating_window)
    
    def clear(self):
        """Очистити QTextEdit."""
        self.widgets.text_editor.clear()
    
    def save_changes(self):
        """Зберегти зміни."""
        write_text(self.file, self.widgets.text_editor.toPlainText())
    
    def chose_file(self):
        """Вибрати файл."""
        try:
            path = get_user_file(self)

            # Якщо користувач НЕ натиснув Cancel
            if path:
                self.file = path
                self.widgets.text_editor.setText(get_file_text(path))
                self.widgets.path.setText(self.file)
                unblock_widgets(self.widgets.save_changes, self.widgets.text_editor, self.widgets.clear)

        except:
            show_message(
                self,
                'Помилка під час завантаження файлу. Можливо, він не того формату, що підтримує программа.'
            )
    
    def open_file_creating_window(self):
        """Відкриває вікно створення файла."""
        self.file_creating_window = FileCreatingWindow()
        self.file_creating_window.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

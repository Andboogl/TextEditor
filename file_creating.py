from windows.file_creating_window import Ui_MainWindow
from PyQt6 import QtWidgets
from functions import *


class FileCreatingWindow(QtWidgets.QMainWindow):
    """Класс створює вікно створення файла."""
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.directory_of_file = None

        # Загружаємо віджети
        self.widgets = Ui_MainWindow()
        self.widgets.setupUi(self)
        
        # Додаємо дії кнопкам
        self.widgets.chose_path.clicked.connect(self.chose_directory)
        self.widgets.create_file.clicked.connect(self.create_file)

    def chose_directory(self):
        """Вибрати директорію, де буде знаходитись файл.""" 
        path = get_user_folder(self)

        # Якщо користувач НЕ натиснув Cancel
        if path:
            self.directory_of_file = path
            self.widgets.path.setText(self.directory_of_file)

    def create_file(self):
        """Створює файл."""
        # Якщо користувач ввів назву файлу
        if self.widgets.file_name.text().strip():
            # Якщо користувач вибрав папку де буде створений файл
            if self.widgets.path.text().strip():
                file_path = os.path.join(self.widgets.path.text(), self.widgets.file_name.text())

                if os.path.exists(file_path):
                    show_message(
                        self,
                        f'Файл за шляхом {file_path} вже існує. Ви можете видалити його або відкрити на редагування.'
                        )
                
                else:
                    create_file(file_path)
                    show_message(self, f'Файл створений за шляхом {file_path}')
            
            else:
                show_message(self, 'Ви не вказали папку, де створювати файл')

        else:
            show_message(self, 'Ви не вказали імʼя файлу')

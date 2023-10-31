from PyQt6.QtGui import QAction, QFont, QKeySequence
from PyQt6 import QtWidgets


class MainWindowWidgets:
     def __init__(self, main_window):
         self.text_editor = QtWidgets.QTextEdit(main_window)
         self.text_editor.setPlaceholderText('Ввведіть текст вашого текстового файлу')
         main_window.setCentralWidget(self.text_editor)
         main_window.setWindowTitle('TextEditor 2.1 BETA')
         main_window.resize(450, 200)
         main_window.setMinimumSize(450, 200)

         # Встановлюемо шрифт
         font = QFont()
         font.setFamily('Monaco')
         font.setPointSize(18)
         self.text_editor.setFont(font)

         self.createMenuBar(main_window)

     def createMenuBar(self, main_window):
         menu_bar = QtWidgets.QMenuBar(main_window)
         
         self.file_menu = QtWidgets.QMenu('&Файл', main_window)
         self.edit_menu = QtWidgets.QMenu('&Редагувати', main_window)
         menu_bar.addMenu(self.file_menu)
         menu_bar.addMenu(self.edit_menu)

         self.font_menu = QtWidgets.QMenu('&Шрифт')
         self.edit_menu.addMenu(self.font_menu)

         # Додаємо кнопки
         self.open_button = QAction('&Відкрити', main_window)
         self.save_button = QAction('&Зберегти', main_window)
         self.save_as_button = QAction('&Зберегти як...', main_window)
         self.clear_button = QAction('&Очистити', main_window)
         self.set_font_button = QAction('&Встановити шрифт...', main_window)
         self.set_default_font_button = QAction('&Встановити шрифт за замовчюванням', main_window)

         # Додаємо комбінації клавіш кнопкам
         self.open_button.setShortcut(QKeySequence('Ctrl+o'))
         self.save_button.setShortcut(QKeySequence('Ctrl+s'))
         self.save_as_button.setShortcut(QKeySequence('Ctrl+shift+s'))
         self.clear_button.setShortcut(QKeySequence('Ctrl+l'))
         self.set_font_button.setShortcut(QKeySequence('Ctrl+f'))
         self.set_default_font_button.setShortcut(QKeySequence('Ctrl+shift+f'))


from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QFont


class MainWindowWidgets:
	"""Класс створює віджети головного вікна."""
	def __init__(self, main_window):
		main_window = main_window
		main_window.resize(500, 300)
		main_window.setMinimumSize(500, 300)
		main_window.setWindowTitle('TextEditor 2')

		# Додаємо редактор тексту
		self.text_edit = QtWidgets.QTextEdit(main_window)
		self.text_edit.setPlaceholderText('Введіть сюди текст вашого текстового файлу')
		
		font = QFont()
		font.setFamily('Arial Rounded MT Bold')
		font.setPointSize(18)

		self.text_edit.setFont(font)
		main_window.setCentralWidget(self.text_edit)

		self.createMenuBar(main_window)
	
	def createMenuBar(self, main_window):
		"""Створює меню."""
		menu_bar = QtWidgets.QMenuBar(main_window)
		main_window.setMenuBar(menu_bar)

		# Додаємо меню файл та редагувати
		self.file_menu = QtWidgets.QMenu('&Файл', main_window)
		self.edit_menu = QtWidgets.QMenu('&Редагувати', main_window)
		menu_bar.addMenu(self.file_menu)
		menu_bar.addMenu(self.edit_menu)
			
		# Додаємо пункт шрифт
		self.font_menu = self.edit_menu.addMenu('&Шрифт')


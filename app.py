from design import MainWindowWidgets
from PyQt6 import QtWidgets, QtGui
import functions
import sys
import os


class MainWindow(QtWidgets.QMainWindow):
	"""Класс створює головне вікно программи."""
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.file = None  # Змінна з шляхом до файлу, який вибрав користувач

		# Загружаємо дизайн
		self.widgets = MainWindowWidgets(self)

		# Додаємо дії кнопкам на QMenuBar
		self.widgets.file_menu.addAction('Відкрити', self.open_file)
		self.widgets.edit_menu.addAction('Очистити', lambda: self.widgets.text_edit.clear())
		self.widgets.file_menu.addAction('Зберегти як...', self.save_as)
		self.widgets.file_menu.addAction('Зберегти', self.save)
		self.widgets.font_menu.addAction('Вибрати...', self.set_font)
		self.widgets.font_menu.addAction('Встановити шрифт за замовчюванням', self.set_default_font)

	def set_default_font(self):
		"""Встановити шрифт за замовчюванням."""
		font = QtGui.QFont()
		font.setFamily('Arial Rounded MT Bold')
		font.setPointSize(18)
	
		self.widgets.text_edit.setFont(font)

	def set_font(self):
		"""Встановити шрифт."""
		font = QtWidgets.QFontDialog.getFont()

		# Якщо користувач НЕ натиснув Cancel
		if font[1]:
			self.widgets.text_edit.setFont(font[0])

	def save(self):
		"""Зберегти файл."""
		if self.file:
			if os.path.exists(self.file):
				with open(self.file, 'w') as file:
					file.write(self.widgets.text_edit.toPlainText())
			
			else:
				with open(self.file, 'x') as file:	
					file.write(self.widgets.text_edit.toPlainText())

		else:
			functions.show_message(self, 'Ви не вказали файл')
	
	def save_as(self):
		"""Зберегти як..."""
		save_path = QtWidgets.QFileDialog.getSaveFileName(self)[0]
		print(save_path)
		
		# Якщо користувач НЕ натиснув Cancel
		if save_path:
			# Якщо такий файл вже існує
			if os.path.exists(save_path):
				with open(save_path, 'w') as f:
					f.write(self.widgets.text_edit.toPlainText())

			else:	
				with open(save_path, 'x') as f:
					f.write(self.widgets.text_edit.toPlainText())
		
			self.file = save_path

	def open_file(self):
		"""Відкрити файл."""
		try:
			file = QtWidgets.QFileDialog.getOpenFileName(self, 'Виберіть файл', '~')[0]
			self.widgets.text_edit.setText(open(file, 'r').read())
			self.file = file

		except:
			functions.show_message(self, f'Не вдалося відкрити файл по шляху {file}. Можливо, це папка або программа поки не підтримує такий формат файлів.')


def start_app():
	"""Функція запускає программу."""
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()


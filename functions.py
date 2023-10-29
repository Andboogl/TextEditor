from PyQt6.QtWidgets import QMessageBox


def show_message(main_window, text):
	"""Показує повідомлення з текстом text на вікні main_window."""
	message_box = QMessageBox(main_window)
	message_box.setText(text)
	message_box.exec()

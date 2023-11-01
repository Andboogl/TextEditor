from design import MainWindowWidgets
from PyQt6.QtGui import QFont
from PyQt6 import QtWidgets
import functions
import sys



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.file = None

        # Загружаемо дизайн
        self.widgets = MainWindowWidgets(self)

        # Додаємо пункти меню
        self.widgets.file_menu.addAction(self.widgets.open_button)
        self.widgets.file_menu.addAction(self.widgets.save_button)
        self.widgets.file_menu.addAction(self.widgets.save_as_button)
        self.widgets.edit_menu.addAction(self.widgets.clear_button)
        self.widgets.font_menu.addAction(self.widgets.set_default_font_button)
        self.widgets.font_menu.addAction(self.widgets.set_font_button)

        # Додаємо дії кнопкам
        self.widgets.open_button.triggered.connect(self.open_file)
        self.widgets.save_button.triggered.connect(self.save)
        self.widgets.save_as_button.triggered.connect(self.save_as)
        self.widgets.clear_button.triggered.connect(lambda: self.widgets.text_editor.clear())
        self.widgets.set_font_button.triggered.connect(self.set_font)
        self.widgets.set_default_font_button.triggered.connect(self.set_default_font)
    
    def set_default_font(self):
         font = QFont()
         font.setFamily('Monaco')
         font.setPointSize(18)
         self.widgets.text_editor.setFont(font)
    
    def set_font(self):
        font = QtWidgets.QFontDialog.getFont(self)

        # Якщо користувач НЕ натиснув Cancel
        if font[1]:
            self.widgets.text_editor.setFont(font[0])
    
    def save(self):
        if self.file:
            functions.save(self.file, self.widgets.text_editor.toPlainText())
        
        else:
            functions.show_message(self, 'Ви не вибрали файл', type=1)

    def save_as(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self, 'Виберіть папку та назву файлу', 'name', 'Txt file (*.txt);; File (*)')

        # Якщо користувач НЕ натиснув Cancel
        if file[0]:
            try:
                functions.save(file[0], self.widgets.text_editor.toPlainText())
                self.file = file[0]
            
            except:
                functions.show_message(self, 'Ви не можете зберегти файл у цій директорії')
                self.save_as()

    def open_file(self):
        try:
            file = QtWidgets.QFileDialog.getOpenFileName(self, 'Виберіть текстовий файл', '~')[0]

            # Якщо користувач НЕ натиснув Cancel
            if file:
                self.widgets.text_editor.setText(functions.get_file_text(file))
                self.file = file

        except:
            functions.show_message(self, 'Такий формат файлів не підтримується', type=2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


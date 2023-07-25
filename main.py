#!/usr/bin/python
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar
from PyQt6.QtGui import QAction
import sys

from lib.database import Database
from ui.CreatePasswordWindow import CreatePasswordWindow
from ui.ShowPasswordsWindow import ShowPasswordsWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        Database().create_password_table()


        # TOOLBAR
        toolbar = QToolBar(self)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        # ToolBar Actions
        generate_password_action = QAction("Generate", self)
        generate_password_action.triggered.connect(self.show_generate_password_screen)
        toolbar.addAction(generate_password_action)

        passwords_action = QAction("Passwords", self)
        passwords_action.triggered.connect(self.show_passwords_window)
        toolbar.addAction(passwords_action)
        
    def show_generate_password_screen(self):
        self.setCentralWidget(CreatePasswordWindow())

    def show_passwords_window(self):
        self.setCentralWidget(ShowPasswordsWindow())

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

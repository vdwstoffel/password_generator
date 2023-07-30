from PyQt6.QtWidgets import QMainWindow, QLabel
from datetime import datetime


class IntroWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        QLabel("Welcome to Random Password Generator",
               self).setGeometry(40, 50, 480, 20)
        QLabel("A local vault to generate random passwords and save the domain",
               self).setGeometry(40, 80, 480, 20)
        current_year = datetime.now().strftime('%Y')
        QLabel("© " + current_year, self).setGeometry(40, 110, 480, 20)

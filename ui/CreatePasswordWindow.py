from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon

from lib.password_generator import PasswordGenerator
from lib.database import Database

class CreatePasswordWindow(QMainWindow):
    '''
    Window To create password
    '''

    def __init__(self):
        super().__init__()

        self.HEIGHT = 20 # default height for all components
        self.password_generator = PasswordGenerator()
        self.database = Database()
        clipboard_svg = QIcon('./clipboard.svg')

        # Components
        self.heading_label = QLabel("Generate New Password", self)
        self.domain_label = QLabel("Domain: ", self)
        self.domain_line_edit = QLineEdit(self)
        self.username_label = QLabel("Username: ", self)
        self.username_line_edit = QLineEdit(self)
        self.password_label = QLabel("Password: ", self)
        self.generated_password_label = QLabel("", self)
        self.copy_to_clipboard_button = QPushButton(self)
        self.copy_to_clipboard_button.setIcon(clipboard_svg)
        self.generate_button = QPushButton("Generate Password", self)
        self.save_button = QPushButton("Save Password", self)
        self.feedback_label = QLabel("", self)

        # Window Placement
        # Left, Top, Width, Heigh
        self.heading_label.setGeometry(60, 10, 200, self.HEIGHT)
        self.domain_label.setGeometry(10, 40, 100, self.HEIGHT)
        self.domain_line_edit.setGeometry(100, 40, 180, self.HEIGHT)
        self.username_label.setGeometry(10, 70, 100, self.HEIGHT)
        self.username_line_edit.setGeometry(100, 70, 180, self.HEIGHT)
        self.password_label.setGeometry(10, 100, 100, self.HEIGHT)
        self.generated_password_label.setGeometry(100, 100, 180, self.HEIGHT)
        self.copy_to_clipboard_button.setGeometry(280, 100, 20, self.HEIGHT)
        self.generate_button.setGeometry(60, 130, 200, self.HEIGHT)
        self.save_button.setGeometry(60, 160, 200, self.HEIGHT)
        self.feedback_label.setGeometry(10, 190, 200, self.HEIGHT)

        # Interactions
        self.generate_button.clicked.connect(self.generate_password_handler)
        self.copy_to_clipboard_button.clicked.connect(self.copy_to_clipboard)
        self.save_button.clicked.connect(self.save_password_info)

    def generate_password_handler(self):
        '''
        Generate a random password and display it in the generated password label
        '''
        password = self.password_generator.generate_password()
        self.generated_password_label.setText(password)

    def copy_to_clipboard(self):
        """
        Copy the password text to the clipboard
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(self.generated_password_label.text())

    def save_password_info(self):
        '''
        Save the domain and password info
        '''
        domain = self.domain_line_edit.text()
        username = self.username_line_edit.text()
        password = self.generated_password_label.text()
        ret = self.database.insert_new_password(domain, username, password)

        # if no details is entered function will return false
        if ret is False:
            self.feedback_label.setText("Please enter details")
            return
        # reset the fields
        self.domain_line_edit.setText("")
        self.username_line_edit.setText("")
        self.generated_password_label.setText("")
        self.feedback_label.setText("Password Saved")

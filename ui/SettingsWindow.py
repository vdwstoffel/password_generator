from PyQt6.QtWidgets import QMainWindow, QPushButton, QMessageBox
import subprocess
import re
import os

from lib.database import Database


class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.HEIGHT = 20
        self.BASE_LEFT = 0
        self.BASE_TOP = 0

        self.delete_db_button = QPushButton("Delete Data", self)
        self.delete_db_button.clicked.connect(self.delete_data_confirmation)
        
        # Window Placement
        # Left, Top, Width, Heigh
        self.delete_db_button.setGeometry(self.BASE_LEFT + 50, self.BASE_TOP + 50, 100, self.HEIGHT)

    def delete_data_confirmation(self):
        '''
        Pop up to confirm that all data must be deleted
        '''
        confirmation_message = QMessageBox.question(self, "Delete Data", 
                                                    "Are you sure you want to delete all data?", 
                                                    QMessageBox.StandardButton.Yes,
                                                    QMessageBox.StandardButton.No)
        
        if confirmation_message == QMessageBox.StandardButton.Yes:
            self.delete_database_data()

    def delete_database_data(self):
        '''
        Delete the database .sqlite3 file
        '''
        sqlite_re = r'.+.sqlite3|.+.log'

        folder_contents = subprocess.run('ls -a', capture_output=True, shell=True)
        sql_files = re.findall(sqlite_re, folder_contents.stdout.decode("utf-8"))

        for item in sql_files:
            os.remove(item)
        
        # Create a new empty file and table to prevent the show password from crashing the app
        os.system('touch passwords.sqlite3')
        Database().create_password_table()

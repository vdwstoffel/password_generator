from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication,QPushButton
from functools import partial
from lib.database import Database


class ShowPasswordsWindow(QMainWindow):
    '''
    Window that shows all the passwords
    '''
    def __init__(self) -> None:
        super().__init__()
        self.database = Database()
        self.records = self.database.get_all_records()
        self.row_count = len(self.records)
        self.records_table = QTableWidget(self.row_count, 4, self)
        self.setup_table()

    def setup_table(self):
        '''
        Create a instance of the table with data read from the database
        '''
        self.records = self.database.get_all_records()
        self.row_count = len(self.records)

        self.records_table.setRowCount(self.row_count)  # resized the column to the number of records

        self.records_table.cellClicked.connect(self.copy_to_clipboard)  # copy the clicked cell to clipboard
        self.records_table.setGeometry(10, 10, 480, 240)
        self.records_table.setHorizontalHeaderLabels(["Domain", "Username", "Password", "Action"])
        
        for index, item in enumerate(self.records):
            uuid, domain, username, password = item
            self.records_table.setItem(index, 0, QTableWidgetItem(domain))
            self.records_table.setItem(index, 1, QTableWidgetItem(username))
            self.records_table.setItem(index, 2, QTableWidgetItem(password))

            delete_button = QPushButton('X')
            # grab the uuid to pass to the function
            delete_button.clicked.connect(partial(self.delete_record, uuid))
            self.records_table.setCellWidget(index, 3, delete_button)

        # Auto size the width of columns to fit the content
        self.records_table.resizeColumnsToContents()

    def copy_to_clipboard(self):
        """
        When a cell is clicked, copy the item to the clipboard
        """
        clipboard = QApplication.clipboard()
        text = self.records_table.currentItem().text()  # get the text of the current item
        clipboard.setText(text)

    def delete_record(self, uuid):
        '''
        Delete a single record based on the uuid
        '''
        self.database.delete_record(uuid)
        self.setup_table()


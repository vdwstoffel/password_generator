from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication
from lib.database import Database


class ShowPasswordsWindow(QMainWindow):
    '''
    Window that shows all the passwords
    '''
    def __init__(self) -> None:
        super().__init__()
        self.database = Database()
        records = self.database.get_all_records()
        row_count = len(records)

        self.records_table = QTableWidget(row_count, 3, self)
        self.records_table.cellClicked.connect(self.copy_to_clipboard)                   # copy the clicked cell to clipboard
        self.records_table.setGeometry(10, 10, 480, 240)
        self.records_table.setHorizontalHeaderLabels(["Domain", "Username", "Password"])

        for index, item in enumerate(records):
            uuid, domain, username, password = item
            self.records_table.setItem(index, 0, QTableWidgetItem(domain))
            self.records_table.setItem(index, 1, QTableWidgetItem(username))
            self.records_table.setItem(index, 2, QTableWidgetItem(password))
        
        # Auto size the width of columns to fit the content
        self.records_table.resizeColumnsToContents()

    def copy_to_clipboard(self):
        """
        When a cell is clicked, copy the item to the clipboard
        """
        clipboard = QApplication.clipboard()
        text = self.records_table.currentItem().text()          # get the text of the current item
        clipboard.setText(text)



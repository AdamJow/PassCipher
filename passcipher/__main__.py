import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QDialog, QTableWidgetItem, QPushButton, \
    QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from .ui.sidebar_ui import Ui_MainWindow
from .db.database import Database
from .ciphers import file_operations, substitution

from .ui.add_account_ui import Ui_Dialog

class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialise the ui, databse and style of the app upon first startup

        :param self: The instance of the class
        """
        super(MainWindow, self).__init__()

        # Set up GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up db
        self.db = Database()
        self.db.create_table()

        # Set up initial page load
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.vault_btn_2.setChecked(True)

        # Connect the add button click signal
        self.ui.add_btn.clicked.connect(self.open_add_from)

    def on_vault_btn_1_toggled(self):
        """
        Change to database page
        """
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_vault_btn_2_toggled(self):
        """
        Change to database page
        """
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_favourites_btn_1_toggled(self):
        """
        Change to favourites page
        """
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_favourites_btn_2_toggled(self):
        """
        Change to favourites page
        """
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_accounts_btn_1_toggled(self):
        """
        Change to all accounts page
        """
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_accounts_btn_2_toggled(self):
        """
        Change to all accoutns page
        """
        self.ui.stackedWidget.setCurrentIndex(2)

    """
    Note: i should break this into two functions.
    One function to iterate over all of the data
    The second function to insert data into the table each iteration

    Keep in mind that these function will be used with the search capbility as well.

    I also need an effective way to display these account list
        - On intiial load, you will need to load all of them (i.e iterate over all data)
        - But when the user adds an account, I only need append that account to the list 
            (not iterate ovr all again)
        - The same applies for the edit (just update those specific details)
        - And delete will shift everything below it up one cell
    """
    def display_accounts(self, data):
        """
        Display account data in UI table
        """
        # Clear existing rows
        self.ui.account_table.setRowCount(0)

        # Iterate through each account tuple in the data list
        for account in data:
            # Insert new row into the table
            new_row_count = self.ui.account_table.rowCount()
            self.ui.account_table.insertRow(new_row_count)
            
            # Extract necessary fields from account tuple
            account_name = account[1]  # Account name
            category = account[6]  # Category

            # Set table items (adjust column indices as needed)
            self.ui.account_table.setItem(new_row_count, 0, QTableWidgetItem(str(new_row_count)))
            self.ui.account_table.setItem(new_row_count, 1, QTableWidgetItem(str(account_name)))
            self.ui.account_table.setItem(new_row_count, 2, QTableWidgetItem(str(category)))
            
            # Put button in last column
            self.edit_btn = QPushButton("Edit")
            self.edit_btn.setObjectName("edit_btn")
            layout = QHBoxLayout()
            layout.addWidget(self.edit_btn)
            layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            layout.setContentsMargins(0,0,0,0)
            widget = QWidget()
            widget.setLayout(layout)
            
            self.ui.account_table.setCellWidget(new_row_count, 3, widget)

    def extract_add_form_data(self, dialog):
        """
        Extracts the user input from the Add Account dialog form and processes it.
        
        :param dialog: The dialog instance containing the form
        """
        account_name = dialog.ui.account_input.toPlainText()
        username = dialog.ui.username_input.toPlainText()
        url = dialog.ui.url_input.toPlainText()
        cipher = dialog.ui.cipher_choice.currentText()
        cipher_key = dialog.ui.key_input.toPlainText()
        group = dialog.ui.group_input.toPlainText()

        print(f"Account Name: {account_name}")
        print(f"Username: {username}")
        print(f"URL: {url}")
        print(f"Cipher: {cipher}")
        print(f"Cipher Key: {cipher_key}")
        print(f"Group: {group}")

        # Close form
        dialog.accept()

        # Create and save cipher map txt file
        cipher = substitution.gen_substitution_mapping()
        cipher_location = file_operations.save_substitution_mapping(cipher)

        # Implement Add account here (need to have Id generation logic here as well)

    def open_add_from(self):      
        """
        Display the add account form pop up
        """
        dialog = QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)

        # Connect the 'create_btn' to extract data
        dialog.ui.create_btn.clicked.connect(lambda: self.extract_add_form_data(dialog))

        dialog.exec_()

    # Close Db when app closes
    def closeEvent(self, event):        
        """
        Close connection to databse when app closes

        :param event: The close event
        """
        self.db.close_connection()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Loading style file
    with open("passcipher/ui/static/style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
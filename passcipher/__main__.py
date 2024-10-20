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
        self.ui.add_btn.clicked.connect(self.add_account_form)

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

    def create_edit_btn(self):
        """
        Create edit button

        :return widget: Newly created edit button widget
        """
        # Create edit button
        self.edit_btn = QPushButton("Edit")
        self.edit_btn.setObjectName("edit_btn")
        self.edit_btn.clicked.connect(self.edit_account)

        # Position button
        layout = QHBoxLayout()
        layout.addWidget(self.edit_btn)
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        layout.setContentsMargins(0,0,0,0)
        widget = QWidget()
        widget.setLayout(layout)
        
        return widget

    def display_account(self, data):
        """
        Display new account to the end row of the Ui table
        """
        new_row = self.ui.account_table.rowCount() + 1
        self.ui.account_table.setRowCount(new_row)

        # Get the group data
        print(f'group id = {data[6]}')
        group_data = self.db.get_data('groups', {'id': data[6]})
        
        # Get the group name
        if group_data and len(group_data) > 0:
            # Get the first tuple from the result
            group = group_data[0]
            # Get the groupname variable from tuple
            group_name = group[1]
        else:
            group_name = "Unknown Group"
        
        # Extract necessary fields from account tuple
        account_name = data[1]

        # Set row items
        self.ui.account_table.setItem(new_row - 1, 0, QTableWidgetItem(str(new_row)))
        self.ui.account_table.setItem(new_row - 1, 1, QTableWidgetItem(str(account_name)))
        self.ui.account_table.setItem(new_row - 1, 2, QTableWidgetItem(str(group_name)))
        self.ui.account_table.setCellWidget(new_row - 1, 3, self.create_edit_btn())

    def display_accounts(self):
        """
        Display accounts in the Ui table
        """
        self.ui.account_table.setRowCount(0)
        data = self.db.get_data('accounts')

        for account in data:
            self.display_account(account)

    def edit_account(self):
        """
        Display the edit account form pop up
        """
        button = self.sender()
        row = self.ui.account_table.indexAt(button.parent().pos()).row()
        
        print(f'edit button clicked. Row = {row}')

    def save_account(self, dialog):
        """
        Extracts the user input from the Add Account dialog form and save it.
        
        :param dialog: The dialog instance containing the form
        """
        # Extract from data
        account_name = dialog.ui.account_input.toPlainText()
        username = dialog.ui.username_input.toPlainText()
        url = dialog.ui.url_input.toPlainText()
        cipher = dialog.ui.cipher_choice.currentText()
        notes = dialog.ui.notes_input.toPlainText()
        group_name = dialog.ui.group_input.toPlainText()

        # Create and save cipher map txt file
        cipher = substitution.gen_substitution_mapping()
        cipher_location = file_operations.save_substitution_mapping(cipher)

        # Check if group exists
        group_data = self.db.get_data('groups', {'group_name': group_name})
        if not group_data:
            group_id = self.db.add_group((group_name,))
        else:
            # Get the first tuple from the result
            group = group_data[0]
            # Get the groupname variable from tuple
            group_id = group[0]
        
        # Create account entry
        account = (account_name, username, url, cipher_location, notes, group_id)

        # Add account to accounts db table
        account_id = self.db.add_account(account)

        # Add account to accounts Ui table
        self.display_account((account_id, account_name, username, url, cipher_location, notes, group_id))

        # Close form
        dialog.accept()

    def add_account_form(self):      
        """
        Display the add account form pop up
        """
        dialog = QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)

        # Connect the 'create_btn' to extract data
        dialog.ui.create_btn.clicked.connect(lambda: self.save_account(dialog))

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
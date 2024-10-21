import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QDialog, QTableWidgetItem, QPushButton, \
    QHBoxLayout, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
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

        # Setup variables
        self.category_page = None

        # Connect the add button click signal
        self.ui.add_btn.clicked.connect(self.add_account_form)

    def on_vault_btn_1_toggled(self):
        """
        Change to database page
        """
        self.ui.stackedWidget.setCurrentIndex(0)
        self.uncheck_category_icons()
        self.category_page = None

    def on_vault_btn_2_toggled(self):
        """
        Change to database page
        """
        self.ui.stackedWidget.setCurrentIndex(0)
        self.uncheck_category_icons()
        self.category_page = None

    def on_favourites_btn_1_toggled(self):
        """
        Change to favourites page
        """
        self.ui.stackedWidget.setCurrentIndex(1)
        self.uncheck_category_icons()
        self.category_page = None

    def on_favourites_btn_2_toggled(self):
        """
        Change to favourites page
        """
        self.ui.stackedWidget.setCurrentIndex(1)
        self.uncheck_category_icons()
        self.category_page = None

    def on_accounts_btn_1_toggled(self):
        """
        Change to all accounts page
        """
        self.ui.stackedWidget.setCurrentIndex(1)
        self.display_all_accounts()
        self.uncheck_category_icons()
        self.category_page = None

    def on_accounts_btn_2_toggled(self):
        """
        Change to all accoutns page
        """
        self.ui.stackedWidget.setCurrentIndex(1)
        self.display_all_accounts()
        self.uncheck_category_icons()
        self.category_page = None
        

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
    
    def update_category_icon(self, checked, button):
        """
        Update the icon based on the checked state of the button
        """
        if checked:
            button.setIcon(QIcon("passcipher/ui/static/icon/category(on).png"))
        else:
            button.setIcon(QIcon("passcipher/ui/static/icon/category(off).png"))

    def uncheck_category_icons(self):
        """
        Update the icon based of the category buttons to unchecked state
        """
        # Ensure the category button for this group is toggled and icon is updated
        for i in range(6, self.ui.sidebar_btns_2.count()):
            btn = self.ui.sidebar_btns_2.itemAt(i).widget()
            btn.setChecked(False)
            self.update_category_icon(False, btn)
    
    def create_category_btn(self, category_name):
        """
        Create category button

        :return widget: Newly created category button widget
        """
        # Create category button
        self.category_btn = QPushButton(category_name)
        self.category_btn.setObjectName("category_btn")
        
        # Connect to function
        self.category_btn.clicked.connect(lambda: self.category_list(category_name))
        
        # Attatch icon
        icon = QIcon("passcipher/ui/static/icon/category(off).png")
        self.category_btn.setIcon(icon)

        # Set the button to be checkable and auto-exclusive
        self.category_btn.setCheckable(True)
        self.category_btn.setAutoExclusive(True)

        # Connect button to update icon when checked
        self.category_btn.toggled.connect(lambda checked: self.update_category_icon(checked, self.category_btn))

        # Create button
        self.ui.sidebar_btns_2.addWidget(self.category_btn)

    def display_account(self, data):
        """
        Display new account to the end row of the Ui table
        """
        new_row = self.ui.account_table.rowCount() + 1
        self.ui.account_table.setRowCount(new_row)

        # Get the group data
        group_data = self.db.get_data('groups', {'id': data[6]})
        
        # Get the group name
        if group_data and len(group_data) > 0:
            # Get the first tuple from the result
            group_name = group_data[0][1]
        else:
            group_name = "Unknown Group"
        
        # Extract necessary fields from account tuple
        account_name = data[1]

        # Set row items
        self.ui.account_table.setItem(new_row - 1, 0, QTableWidgetItem(str(new_row)))
        self.ui.account_table.setItem(new_row - 1, 1, QTableWidgetItem(str(account_name)))
        self.ui.account_table.setItem(new_row - 1, 2, QTableWidgetItem(str(group_name)))
        self.ui.account_table.setCellWidget(new_row - 1, 3, self.create_edit_btn())

    def display_all_accounts(self):
        """
        Display all accounts in the Ui table
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
            self.create_category_btn(group_name)
        else:
            # Get the first tuple from the result
            group_id = group_data[0][0]
        
        # Create account entry
        account = (account_name, username, url, cipher_location, notes, group_id)

        # Add account to accounts db table
        account_id = self.db.add_account(account)

        # Add account to accounts Ui table (if applicable)
        current_page_index = self.ui.stackedWidget.currentIndex()
        if current_page_index == 1:
            # Check what sidebar button is checked
            for i in range(0, self.ui.sidebar_btns_2.count()):
                btn = self.ui.sidebar_btns_2.itemAt(i).widget()
                # Ensure the widget is a QPushButton (or any other widget type that can be checked)
                if isinstance(btn, QPushButton) and btn.isChecked():
                    btn_name = btn.text()
                    print(btn_name)
                    break

            # All Accounts Page
            if btn_name == 'All Items':
                self.display_account((account_id, account_name, username, url, cipher_location, notes, group_id))
            # Favourites Accounts Page
            elif btn_name == 'Favourites':
                self.display_account((account_id, account_name, username, url, cipher_location, notes, group_id))
            # Category Accounts Page
            elif group_name == self.category_page:
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

    def category_list(self, category_name):
        """
        Display the accounts under certain category
        """
        # Clear existing accounts displayed in the table
        self.ui.account_table.setRowCount(0)

        # Fetch the group data corresponding to the category_name
        group_data = self.db.get_data('groups', {'group_name': category_name})
        if not group_data:
            print(f'No group found for {category_name}')
            return

        # Get the group ID from the group data
        group_id = group_data[0][0]

        # Fetch accounts associated with this group_id
        accounts = self.db.get_data('accounts', {'group_id': group_id})

        for account in accounts:
            self.display_account(account)

        # Change to account list page (accounts page)
        self.ui.stackedWidget.setCurrentIndex(1)

        # Ensure the category button for this group is toggled and icon is updated
        for i in range(6, self.ui.sidebar_btns_2.count()):
            btn = self.ui.sidebar_btns_2.itemAt(i).widget()
            if btn.text() == category_name:
                btn.setChecked(True)
                self.category_page = category_name
                self.update_category_icon(True, btn)
            else:
                btn.setChecked(False)
                self.update_category_icon(False, btn)

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
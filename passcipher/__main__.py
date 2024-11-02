import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QDialog, QTableWidgetItem, QPushButton, \
    QHBoxLayout, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from .ui.sidebar_ui import Ui_MainWindow
from .db.database import Database
from .ciphers import file_operations, substitution

from .ui.add_account_ui import Ui_Dialog as add_Dialog
from .ui.edit_account_ui import Ui_Dialog as edit_Dialog

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

        # Display category buttons
        self.init_category_btns()

        # Setup variables
        self.category_page = None

        # Connect the add button click signal
        self.ui.add_btn.clicked.connect(self.add_account_form)

    ##############################
    # Functions for Page Change
    ##############################

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
        
    ##############################
    # Functions for Ui
    ##############################

    def init_category_btns(self):
        """
        Display Category buttons on initial app startup
        """
        group_data = self.db.get_data('groups')
        for group_data in group_data:
            self.create_category_btn(group_data[1])

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

    def get_checked_btn(self):
        """
        Get the name of the checked sidebar button.
        
        :return: The name of the checked button or None if no button is checked
        """
        for i in range(self.ui.sidebar_btns_2.count()):
            btn = self.ui.sidebar_btns_2.itemAt(i).widget()
            if isinstance(btn, QPushButton) and btn.isChecked():
                return btn.text()
        return None
    
    def add_account_form(self):      
        """
        Display the add account form pop up
        """
        dialog = QDialog()
        dialog.ui = add_Dialog()
        dialog.ui.setupUi(dialog)

        # Connect the 'create_btn' to extract data
        dialog.ui.create_btn.clicked.connect(lambda: self.save_account(dialog))

        dialog.exec_()

    def edit_account_form(self, account_details, group_name, row):      
        """
        Display the edit account form pop up
        """
        dialog = QDialog()
        dialog.ui = edit_Dialog()
        dialog.ui.setupUi(dialog)

        # Populate fields with account details
        dialog.ui.account_input.setPlainText(f'{account_details[1]}')
        dialog.ui.username_input.setPlainText(f'{account_details[2]}')
        dialog.ui.url_input.setPlainText(f'{account_details[3]}')
        dialog.ui.notes_input.setPlainText(f'{account_details[5]}')
        dialog.ui.group_input.setPlainText(f'{group_name}')

        # Connect the 'create_btn' to extract data
        dialog.ui.save_btn.clicked.connect(lambda: self.save_changes(dialog, group_name, account_details[0], row))

        dialog.exec_()

    ##############################
    # Functions for Accounts
    ##############################

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

    def display_all_accounts(self, groupId=None):
        """
        Display all accounts in the Ui table
        """
        self.ui.account_table.setRowCount(0)
        # Get specific group accounts
        if groupId:
            data = self.db.get_data('accounts', {'group_id': groupId})
        # Get all accounts
        else:
            data = self.db.get_data('accounts')

        for account in data:
            self.display_account(account)

    def edit_account(self):
        """
        Display the edit account form pop up
        """
        # Get button properties
        button = self.sender()
        btn_name = self.get_checked_btn()
        if btn_name is None:
            print('No Button is checked')
            return

        # Get page and row index
        current_page_index = self.ui.stackedWidget.currentIndex()
        row = self.ui.account_table.indexAt(button.parent().pos()).row()

        if current_page_index == 1:
            if btn_name == 'All Items':
                print('all items')
            elif btn_name == 'Favourites':
                print('favourites')
            elif btn_name == self.category_page:
                # Get Group Id and all accounts with that group Id
                groupId = self.get_group(btn_name)
                accounts_data = self.db.get_data('accounts', {'group_id': groupId})

                # Get selected account details
                selected_account = accounts_data[row]
                print(selected_account)

                # Call edit account pop up
                self.edit_account_form(selected_account, btn_name, row)

    def generate_cipher(self, cipher_choice):
        """
        Generate chosen cipher mapping and save file
        
        :param cipher_choice: The chosen cipher
        :return: The location of the saved file
        """
        # Generate chosen Cipher
        if cipher_choice == 'Substitution Cipher':
            print('substitution chosen')
            cipher = substitution.gen_substitution_mapping()
        else:
            print('other cipher chosen')
            #### CHANGE TO APPROPRIATE CIPHER LOGIC FUNCTION WHEN IVE MADE IT #####
            cipher = substitution.gen_substitution_mapping()

        # Save cipher map txt file and return location
        return file_operations.save_substitution_mapping(cipher)

    def get_group(self, group_name):
        """
        Get the Id associated with group
        
        :param group_name: The name of the group
        :return: The Id associated with the group
        """
        # Check if group exists
        group_data = self.db.get_data('groups', {'group_name': group_name})
        if not group_data:
            print('group doesnt exist')
            return None
        # Get the first tuple from the result
        return group_data[0][0]

    def create_group(self, group_name):
        """
        Add group entry into groups table
        
        :param group_name: The name of the group
        :return: The Id associated with the group
        """
        # Create group
        group_id = self.db.add_group((group_name,))
        self.create_category_btn(group_name)

        return group_id
    
    def extract_account_details(self, dialog):
        """
        Extract account data from the add account dialog form.
        
        :param dialog: The dialog instance containing the form
        :return: Dictionary of account data
        """
        account_name = dialog.ui.account_input.toPlainText()
        username = dialog.ui.username_input.toPlainText()
        url = dialog.ui.url_input.toPlainText()
        cipher_choice = dialog.ui.cipher_choice.currentText()
        cipher_location = self.generate_cipher(cipher_choice)
        notes = dialog.ui.notes_input.toPlainText()
        group_name = dialog.ui.group_input.toPlainText()

        return {
            'account_name': account_name,
            'username': username,
            'url': url,
            'cipher_location': cipher_location,
            'notes': notes,
            'group_name': group_name
        }

    def update_ui_on_account_save(self, account_id, account, input_group):
        """
        Update the UI based on the current page and category when an account is saved.
        
        :param account_id: The ID of the newly saved account
        :param account: The account details tuple
        :param group_id: The group ID to which the account belongs
        """
        current_page_index = self.ui.stackedWidget.currentIndex()
        btn_name = self.get_checked_btn()
        if btn_name is None:
            print('No Button is checked')
            return

        # Convert account data to a tuple with account_id prepended
        account_with_id = (account_id,) + account

        if current_page_index == 1:
            if btn_name == 'All Items':
                self.display_account(account_with_id)
            elif btn_name == 'Favourites':
                self.display_account(account_with_id)
            elif input_group == self.category_page:
                self.display_account(account_with_id)

    def save_account(self, dialog):
        """
        Extracts the user input from the Add Account dialog form and save it.
        
        :param dialog: The dialog instance containing the form
        """
        # Extract and proces dialog inputs
        account_data = self.extract_account_details(dialog)
        groupId = self.get_group(account_data['group_name'])
        if not groupId:
            # Create group
            groupId = self.create_group(account_data['group_name'])

        # Create account entry
        account = (
            account_data['account_name'],
            account_data['username'],
            account_data['url'],
            account_data['cipher_location'],
            account_data['notes'],
            groupId
        )

        # Add account to accounts db table
        account_id = self.db.add_account(account)

        # Handle UI display based on the current page and category
        self.update_ui_on_account_save(account_id, account, account_data['group_name'])

        # Close form
        dialog.accept()

    def save_changes(self, dialog, group_name, accountId, row):
        """
        Extracts the user input from the Add Account dialog form and save it.
        
        :param dialog: The dialog instance containing the form
        """
        # Get original group Id
        original_groupId = self.get_group(group_name)

        # Extract and proces dialog inputs
        account_data = self.extract_account_details(dialog)
        groupId = self.get_group(account_data['group_name'])
        if not groupId:
            # Create group
            groupId = self.create_group(account_data['group_name'])

        # Create account entry
        account = (
            account_data['account_name'],
            account_data['username'],
            account_data['url'],
            account_data['cipher_location'],
            account_data['notes'],
            groupId
        )

        # Convert account data to a tuple with account_id prepended
        update_account_data =  account + (accountId,) 

        # Update account in accounts db table
        self.db.update_account(update_account_data)

        # Update Current Page
        self.display_all_accounts(original_groupId)

        # Close form
        dialog.accept()
    
    ##############################
    # Functions for Categories
    ##############################

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
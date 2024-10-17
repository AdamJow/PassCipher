import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from .ui.sidebar_ui import Ui_MainWindow
from .db.database import Database
from .ciphers import file_operations, substitution

class MainWindow(QMainWindow):
    def __init__(self):
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

        self.ui.sort_btn.clicked.connect(self.on_button_click)

    # Functions for changing pages
    def on_vault_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_vault_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_favourites_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_favourites_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_accounts_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_accounts_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    # Testing inital logic
    def on_button_click(self):
        substitution_mapping = substitution.gen_substitution_mapping()
        file_operations.save_substitution_mapping(substitution_mapping)

    # Close Db when app closes
    def closeEvent(self, event):        
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
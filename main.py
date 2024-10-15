import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.MainWindow import Ui_MainWindow
from db.database import Database
from ciphers import file_operations, substitution

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.db = Database()
        self.db.create_table()

        self.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Button pressed!")

        substitution_mapping = substitution.gen_substitution_mapping()
        print("Substitution Mapping:")
        for original, substituted in substitution_mapping.items():
            print(f"{original}: {substituted}")

        file_operations.save_substitution_mapping(substitution_mapping)

    def closeEvent(self, event):        
        self.db.close_connection()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
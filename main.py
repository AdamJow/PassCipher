import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# Import the generated UI class
from gui.MainWindow import Ui_MainWindow

# Import the modules from ciphers package
from ciphers import file_operations, substitution

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Add custom logic here
        self.pushButton.clicked.connect(self.on_button_click)  # Connect button to function

    def on_button_click(self):
        # This function runs when the button is clicked
        print("Button pressed!")

        substitution_mapping = substitution.gen_substitution_mapping()
        print("Substitution Mapping:")
        for original, substituted in substitution_mapping.items():
            print(f"{original}: {substituted}")

        file_operations.save_substitution_mapping(substitution_mapping)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
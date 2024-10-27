import sys
from PyQt6.QtWidgets import QApplication
from src.Controller import MyMainWindow

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
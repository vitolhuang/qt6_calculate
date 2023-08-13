import sys
from PySide6 import QtWidgets
from controller import CalculatorController

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorController()
    window.view.show()
    sys.exit(app.exec())
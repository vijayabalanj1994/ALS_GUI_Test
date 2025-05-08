import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application_Login.login import LoginForm
from Persons.add_person import AddPerson
from Main.UI.main_window import Ui_m_window


class MainWindow(qtw.QMainWindow, Ui_m_window):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_Quit.triggered.connect(self.close)
        self.action_AddPerson.triggered.connect(self.open_add_person)

        self.form = LoginForm()
        self.form.login_success.connect(self.show)
        self.form.show()

    @qtc.Slot()
    def open_add_person(self):
        self.form = AddPerson()
        self.form.exec()



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
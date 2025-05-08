import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Persons.UI.add_person_window import Ui_d_Person

class AddPerson(qtw.QDialog, Ui_d_Person):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.gb_Person.setTitle("Add Person")
        self.lb_Message.clear()
        self.le_FirstName.setFocus()
        self.pb_Close.clicked.connect(self.reject)
        self.pb_Sudmit.clicked.connect(self.process_entry)

    @qtc.Slot()
    def process_entry(self):

        self.lb_Message.setText("New person added")
        self.le_FirstName.clear()
        self.le_LastName.clear()

        self.le_FirstName.setFocus()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = AddPerson()
    window.show()
    sys.exit(app.exec())
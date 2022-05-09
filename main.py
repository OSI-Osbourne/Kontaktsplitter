import sys
from Controller import Finder
from ui.MainWindow import Ui_MainWindow
from ui.Dialog import Ui_Dialog as Form
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.btnCancel.clicked.connect(self.close)
        self.btnRefreshInfo.clicked.connect(self.refresh)
        self.btnSplitContact.clicked.connect(self.split_contact)
        self.actionTitel_bearbeiten.triggered.connect(self.open_dialog)

        self.toolBtnGender.clicked.connect(self.inoutGender.setReadOnly)
        self.toolBtnSalut.clicked.connect(self.inoutSalutation.setReadOnly)
        self.toolBtnTitles.clicked.connect(self.inoutTitle.setReadOnly)
        self.toolBtnFirstname.clicked.connect(self.inoutFirstname.setReadOnly)
        self.toolBtnLastname.clicked.connect(self.inoutLastname.setReadOnly)


    def open_dialog(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form()
        dialog.ui.setupUi(dialog)
        dialog.ui.load_data()
        dialog.ui.btnCancel.clicked.connect(dialog.close)
        dialog.ui.btnSave.clicked.connect(dialog.ui.save_data)
        dialog.ui.btnSave.clicked.connect(dialog.close)
        dialog.ui.btnNewRow.clicked.connect(dialog.ui.insert_row)
        dialog.ui.btnDeleteRow.clicked.connect(dialog.ui.remove_row)
        dialog.exec_()
        dialog.show()

    def refresh(self):
        self.inputContact.setText("")
        self.inoutGender.setText("")
        self.inoutSalutation.setText("")
        self.inoutTitle.setText("")
        self.inoutFirstname.setText("")
        self.inoutLastname.setText("")
        self.inoutGenSalutation.setText("")

    def refresh_split(self):
        self.inoutGender.setText("")
        self.inoutSalutation.setText("")
        self.inoutTitle.setText("")
        self.inoutFirstname.setText("")
        self.inoutLastname.setText("")
        self.inoutGenSalutation.setText("")

    def split_contact(self):
        contact_info = self.inputContact.text()
        contact_dict = Finder.find(contact_info)

        self.refresh_split()

        #set gender, salut and firstname
        if contact_dict.gender:
            self.inoutGender.setText(contact_dict.gender)
        else:
            self.inoutGender.setText("–")

        if contact_dict.salutation:
            self.inoutSalutation.setText(contact_dict.salutation)
        else:
            self.inoutSalutation.setText("–")

        if contact_dict.prename:
            self.inoutFirstname.setText(contact_dict.prename)
        else:
            self.inoutFirstname.setText("–")

        #set lastname depending on extra
        if contact_dict.name_extra:
            self.inoutLastname.setText(contact_dict.name_extra + " " + contact_dict.name)
        elif contact_dict.name and not contact_dict.name_extra:
            self.inoutLastname.setText(contact_dict.name)
        else:
            self.inoutLastname.setText("–")

        #set titles
        if contact_dict.titles:
            for title in contact_dict.titles:
                self.inoutTitle.setText(self.inoutTitle.text() + " " + title + " ")
        else:
            self.inoutTitle.setText("–")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    """print(str(Finder.find("Frau Sandra Berger")))
    print(str(Finder.find("Herr Dr. Sandro Gutmensch")))
    print(str(Finder.find("Professor Heinreich Freiherr vom Wald")))
    print(str(Finder.find("Mrs. Doreen Faber")))
    print(str(Finder.find("Mme. Charlotte Noir")))
    print(str(Finder.find("Estobar y Gonzales")))
    print(str(Finder.find("Frau Prof. Dr. rer. nat. Maria von Leuthäuser-Schnarrenberger")))
    print(str(Finder.find("Herr Dipl. Ing. Max von Müller")))
    print(str(Finder.find("Dr. Russwurm, Winfried")))
    print(str(Finder.find("Dr. von Russwurm, Winfried")))
    print(str(Finder.find("Herr Dr.-Ing. Dr. rer. nat. Dr. h.c. mult. Paul Steffens")))"""


if __name__ == '__main__':
    main()

import sys
from Controller import Finder, FrontendHelper
from ui.MainWindow import Ui_MainWindow
from ui.Dialog_Title import Ui_Dialog_Title as Form_Title
from ui.Dialog_Female_Salut import Ui_Dialog_Female_Salut as Form_Female_Salut
from ui.Dialog_Male_Salut import Ui_Dialog_Male_Salut as Form_Male_Salut
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.btnCancel.clicked.connect(self.close)
        self.btnRefreshInfo.clicked.connect(self.refresh)
        self.btnSplitContact.clicked.connect(self.split_contact)
        self.actionTitel_bearbeiten.triggered.connect(lambda: self.open_dialog("title", Form_Title, FrontendHelper.TITLES_FILE))
        self.actionWeibliche_Anreden_bearbeiten.triggered.connect(self.open_dialog_female_salut)
        #self.actionWeibliche_Anreden_bearbeiten.triggered.connect(lambda: self.open_dialog("female_salut", Form_Female_Salut, FrontendHelper.FEMALE_FILE))
        self.actionMaennliche_Anreden_bearbeiten.triggered.connect(lambda: self.open_dialog("male_salut", Form_Male_Salut, FrontendHelper.MALE_FILE))

        self.toolBtnGender.clicked.connect(self.inoutGender.setReadOnly)
        self.toolBtnSalut.clicked.connect(self.inoutSalutation.setReadOnly)
        self.toolBtnTitles.clicked.connect(self.inoutTitle.setReadOnly)
        self.toolBtnFirstname.clicked.connect(self.inoutFirstname.setReadOnly)
        self.toolBtnLastname.clicked.connect(self.inoutLastname.setReadOnly)

    def open_dialog(self, app, form, file):
        app = QtWidgets.QDialog()
        print(app)
        app.ui = form()
        print(app.ui)
        app.ui.setupUi(app)
        FrontendHelper.load_data(app.ui, file)
        app.ui.btnCancel.clicked.connect(app.close)
        app.ui.btnSave.clicked.connect(lambda: FrontendHelper.save_data(app.ui, file))
        app.ui.btnSave.clicked.connect(app.close)
        app.ui.btnNewRow.clicked.connect(lambda: FrontendHelper.insert_row(app.ui))
        app.ui.btnDeleteRow.clicked.connect(lambda: FrontendHelper.remove_row(app.ui))
        app.exec_()
        app.show()

    """def open_dialog_title(self):
        dialog_title = QtWidgets.QDialog()
        dialog_title.ui = Form_Title()
        dialog_title.ui.setupUi(dialog_title)
        FrontendHelper.load_data(dialog_title.ui, FrontendHelper.TITLES_FILE)
        dialog_title.ui.btnCancel.clicked.connect(dialog_title.close)
        #dialog_title.ui.btnSave.clicked.connect(dialog_title.ui.save_data)
        dialog_title.ui.btnSave.clicked.connect(dialog_title.close)
        #dialog_title.ui.btnNewRow.clicked.connect(dialog_title.ui.insert_row)
        #dialog_title.ui.btnDeleteRow.clicked.connect(dialog_title.ui.remove_row)
        dialog_title.exec_()
        dialog_title.show()"""

    def open_dialog_female_salut(self):
        dialog_female_salut = QtWidgets.QDialog()
        print(dialog_female_salut)
        dialog_female_salut.ui = Form_Female_Salut()
        print(dialog_female_salut.ui)
        dialog_female_salut.ui.setupUi(dialog_female_salut)
        FrontendHelper.load_data(dialog_female_salut.ui, FrontendHelper.FEMALE_FILE)
        dialog_female_salut.ui.btnCancel.clicked.connect(dialog_female_salut.close)
        #dialog_female_salut.ui.btnSave.clicked.connect(dialog_female_salut.ui.save_data)
        dialog_female_salut.ui.btnSave.clicked.connect(dialog_female_salut.close)
        #dialog_female_salut.ui.btnNewRow.clicked.connect(dialog_female_salut.ui.insert_row)
        #dialog_female_salut.ui.btnDeleteRow.clicked.connect(dialog_female_salut.ui.remove_row)
        dialog_female_salut.exec_()
        dialog_female_salut.show()

    """def open_dialog_male_salut(self):
        dialog_male_salut = QtWidgets.QDialog()
        dialog_male_salut.ui = Form_Male_Salut()
        dialog_male_salut.ui.setupUi(dialog_male_salut)
        dialog_male_salut.ui.load_data()
        dialog_male_salut.ui.btnCancel.clicked.connect(dialog_male_salut.close)
        dialog_male_salut.ui.btnSave.clicked.connect(dialog_male_salut.ui.save_data)
        dialog_male_salut.ui.btnSave.clicked.connect(dialog_male_salut.close)
        dialog_male_salut.ui.btnNewRow.clicked.connect(dialog_male_salut.ui.insert_row)
        dialog_male_salut.ui.btnDeleteRow.clicked.connect(dialog_male_salut.ui.remove_row)
        dialog_male_salut.exec_()
        dialog_male_salut.show()"""

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

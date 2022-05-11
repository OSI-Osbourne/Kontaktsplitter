import sys
from Controller import Finder, FrontendHelper
from ui.MainWindow import Ui_MainWindow
from ui.Dialog_Title import Ui_Dialog_Title as Form_Title
from ui.Dialog_Female_Salut import Ui_Dialog_Female_Salut as Form_Female_Salut
from ui.Dialog_Male_Salut import Ui_Dialog_Male_Salut as Form_Male_Salut
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.fill_combo(FrontendHelper.LETTER_ADDRESS_FILE)

        self.btnCancel.clicked.connect(self.close)
        self.btnRefreshInfo.clicked.connect(self.refresh)
        self.btnSplitContact.clicked.connect(self.split_contact)
        self.actionModify_Title.triggered.connect(partial(self.open_dialog, Form_Title, FrontendHelper.TITLES_FILE))
        self.actionModify_Female_Salut.triggered.connect(partial(self.open_dialog, Form_Female_Salut,
                                                                          FrontendHelper.FEMALE_FILE))
        self.actionModify_Male_Salut.triggered.connect(partial(self.open_dialog, Form_Male_Salut,
                                                                           FrontendHelper.MALE_FILE))
        self.btnGenSalut.clicked.connect(partial(self.gen_salut, address_dict))
        self.toolBtnGender.clicked.connect(self.inoutGender.setReadOnly)
        self.toolBtnSalut.clicked.connect(self.inoutSalutation.setReadOnly)
        self.toolBtnTitles.clicked.connect(self.inoutTitle.setReadOnly)
        self.toolBtnFirstname.clicked.connect(self.inoutFirstname.setReadOnly)
        self.toolBtnLastname.clicked.connect(self.inoutLastname.setReadOnly)

    def fill_combo(self, file):
        global address_dict
        address_dict = FrontendHelper.load_json(file)
        for language in address_dict:
            self.drpdwnLanguage.addItem(language)

    def gen_salut(self, addresses):
        pattern = self.drpdwnLanguage.currentText()
        gender = self.inoutGender.text()

        self.inoutGenSalutation.setText("")

        for address in addresses[pattern]:
            if address["gender"] == gender:
                suggested_address = address["address"]
                break
            else:
                suggested_address = ""
        if self.inoutSalutation.text() == "–":
            self.inoutGenSalutation.setText(suggested_address)
        elif self.inoutTitle.text() == "–":
            self.inoutGenSalutation.setText(suggested_address + " " + self.inoutSalutation.text() + " " +
                                            self.inoutLastname.text())
        elif self.inoutSalutation == "M" or self.inoutSalutation == "Mme":
            self.inoutGenSalutation.setText(suggested_address + " " + self.inoutTitle.text() + " " +
                                            self.inoutLastname.text())
        else:
            self.inoutGenSalutation.setText(suggested_address + " " + self.inoutSalutation.text() + " " +
                                            self.inoutTitle.text() + " " + self.inoutLastname.text())
        print(suggested_address)
        print(self.inoutSalutation.text())
        print(self.inoutTitle.text())
        print(self.inoutLastname.text())
        print(self.inoutGenSalutation.text())


    def open_dialog(self, form, file):
        app = QtWidgets.QDialog()
        app.ui = form()
        app.ui.setupUi(app)
        FrontendHelper.load_data(app.ui, file)
        app.ui.btnCancel.clicked.connect(app.close)
        app.ui.btnSave.clicked.connect(partial(FrontendHelper.save_data, app.ui, file))
        app.ui.btnSave.clicked.connect(app.close)
        app.ui.btnNewRow.clicked.connect(partial(FrontendHelper.insert_row, app.ui))
        app.ui.btnDeleteRow.clicked.connect(partial(FrontendHelper.remove_row, app.ui))
        app.exec_()
        app.show()

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


if __name__ == '__main__':
    main()

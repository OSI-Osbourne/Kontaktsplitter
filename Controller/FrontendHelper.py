from PyQt5 import QtWidgets
from Controller.Finder import load_list, save_list

TITLES_FILE = "Models/titles.txt"
FEMALE_FILE = "Models/female_salutations.txt"
MALE_FILE = "Models/male_salutations.txt"

def load_data(dialog, file):
    data = load_list(file)
    dialog.tableWidget.setRowCount(len(data))
    row = 0
    for entry in data:
        if entry != "":
            dialog.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(entry))
            row += 1
        else:
            dialog.tableWidget.removeRow(row)

def save_data(dialog, file):
    new_data = []
    rows = dialog.tableWidget.rowCount()
    for row in range(rows):
        try:
            new_data.append(dialog.tableWidget.item(row, 0).text() + '\n')
        except:
            pass
    save_list(new_data, file)


def insert_row(dialog):
    rows = dialog.tableWidget.rowCount()
    dialog.tableWidget.insertRow(rows)

def remove_row(dialog):
    curr_row = dialog.tableWidget.currentRow()
    dialog.tableWidget.removeRow(curr_row)

def close_dialog(dialog):
    dialog.close()
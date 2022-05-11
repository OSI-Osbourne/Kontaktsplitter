from PyQt5 import QtWidgets
import json

TITLES_FILE = "Models/titles.txt"
EXTRAS_FILE = "Models/name_extras.txt"
FEMALE_FILE = "Models/female_salutations.txt"
MALE_FILE = "Models/male_salutations.txt"
LETTER_ADDRESS_FILE = "Models/letter_address.json"

def load_json(file):
    with open(file, encoding='utf-8') as f:
        address_dict = json.load(f)
    return address_dict

def load_list(file):
    list = []
    with open(file) as f:
        for line in f:
            list.append(line.replace('\n', ''))
    return list


def save_list(output, file):
    with open(file, 'w') as f:
        f.writelines(output)

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

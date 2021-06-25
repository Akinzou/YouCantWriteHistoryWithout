from PyQt5 import QtWidgets, uic, QtCore, QtGui


app = QtWidgets.QApplication([])
dlg = uic.loadUi("GUI/Main.ui")

def changeLanguagePL():
    dlg.Polish.setEnabled(False)
    dlg.English.setEnabled(True)
    dlg.WriteHistory.setText("Napisz historię!")

def changeLanguageEn():
    dlg.Polish.setEnabled(True)
    dlg.English.setEnabled(False)
    dlg.WriteHistory.setText("Write history!")

def checkTextEdit():
    print(dlg.plainTextEdit.toPlainText())
    if dlg.plainTextEdit.toPlainText():
        dlg.WriteHistory.setEnabled(True)
    else:
        dlg.WriteHistory.setEnabled(False)

dlg.Polish.clicked.connect(changeLanguagePL)
dlg.English.clicked.connect(changeLanguageEn)
dlg.plainTextEdit.textChanged.connect(checkTextEdit)
dlg.show()
app.exec()
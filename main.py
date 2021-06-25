from PyQt5 import QtWidgets, uic, QtCore, QtGui


app = QtWidgets.QApplication([])
dlg = uic.loadUi("GUI/Main.ui")
dlg.setWindowTitle("YCWHW")

def changeLanguagePL():
    dlg.Polish.setEnabled(False)
    dlg.English.setEnabled(True)
    dlg.WriteHistory.setText("Napisz historię!")
    dlg.WithOut.setText("Bez:")

def changeLanguageEn():
    dlg.Polish.setEnabled(True)
    dlg.English.setEnabled(False)
    dlg.WriteHistory.setText("Write history!")
    dlg.WithOut.setText("Without:")

def checkTextEdit():
    if dlg.plainTextEdit.toPlainText() and dlg.WithOutText.toPlainText():
        dlg.WriteHistory.setEnabled(True)
    else:
        dlg.WriteHistory.setEnabled(False)

def writeHistory():
    text = []
    same = []
    history = []

    for i in dlg.plainTextEdit.toPlainText():
        text.append(str(i))

    for x in dlg.WithOutText.toPlainText():
        history.append(str(x))

    for z in history:
        for y in text:
            if ((y == z) and (y not in same)):
                same.append(y)
    print(text)
    print(history)
    print(same)

dlg.Polish.clicked.connect(changeLanguagePL)
dlg.English.clicked.connect(changeLanguageEn)
dlg.WriteHistory.clicked.connect(writeHistory)
dlg.plainTextEdit.textChanged.connect(checkTextEdit)
dlg.WithOutText.textChanged.connect(checkTextEdit)
dlg.show()
app.exec()
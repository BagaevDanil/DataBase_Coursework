from PyQt5 import QtCore, QtGui, QtWidgets
from form_type1 import Ui_FormType1
from constants import *
from style import *

class Ui_FormType5(Ui_FormType1):
    def createWidget(self, Widget):
        super().createWidget(Widget)
        self.pushButton.setText('Изменить')
        self.pushButton.setGeometry(QtCore.QRect(SCROLL_WIDTH + 20, 110, 140, 30))

        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(SCROLL_WIDTH + 20, 60, 140, 30))

        self.pushButtonUpdate2 = QtWidgets.QPushButton(Widget)
        self.pushButtonUpdate2.setGeometry(QtCore.QRect(SCROLL_WIDTH + 20, 150, 140, 30))
        self.pushButtonUpdate2.setStyleSheet(BUTTON_STYLE)
        self.pushButtonUpdate2.setText('Обновить')
        self.pushButtonUpdate2.clicked.connect(self.clickUpdate)

    def changeRow(self, id, data):
        pass

    def clickUpdate(self):
        self.updateComboBox()
        rows = self.getRowsForUpdateTable()
        self.updateTable(rows)

    def clickOK(self):
        id = self.list_id[self.comboBox.currentIndex()]
        data = self.lineEdit.text()
        self.changeRow(id, data)

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormType5()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
from form_type1 import Ui_FormType1
from constants import *
from style import *

class Ui_FormType4(Ui_FormType1):
    def createWidget(self, Widget):
        super().createWidget(Widget)
        self.pushButton.setText('Удалить')

        self.pushButtonUpdate2 = QtWidgets.QPushButton(Widget)
        self.pushButtonUpdate2.setGeometry(QtCore.QRect(SCROLL_WIDTH + 20, 100, 140, 30))
        self.pushButtonUpdate2.setStyleSheet(BUTTON_STYLE)
        self.pushButtonUpdate2.setText('Обновить')
        self.pushButtonUpdate2.clicked.connect(self.clickUpdate)

    def deleteRow(self, id):
        pass

    def clickOK(self):
        id = self.list_id[self.comboBox.currentIndex()]
        self.deleteRow(id)
        
    def clickUpdate(self):
        self.updateComboBox()
        rows = self.getRowsForUpdateTable()
        self.updateTable(rows)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormType4()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
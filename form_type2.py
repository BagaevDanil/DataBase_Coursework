from PyQt5 import QtCore, QtGui, QtWidgets
from form_type1 import Ui_FormType1

class Ui_FormType2(Ui_FormType1):

    def createWidget(self, Widget):
        super().createWidget(Widget)

        self.comboBox2 = QtWidgets.QComboBox(Widget)
        self.comboBox2.setGeometry(QtCore.QRect(560, 70, 200, 30))
        self.comboBox2.setObjectName("comboBox2")
        for item in self.listItemsComboBox2:
            self.comboBox2.addItem(item)

        self.pushButton.setGeometry(QtCore.QRect(560, 120, 140, 30))

    def getRowsForUpdateTable(self, idRoute, id2):
        return []

    def clickOK(self):
        id = self.list_id[self.comboBox.currentIndex()]
        id2 = self.comboBox2.currentIndex()
        rows = self.getRowsForUpdateTable(id, id2)
        self.updateTable(rows)
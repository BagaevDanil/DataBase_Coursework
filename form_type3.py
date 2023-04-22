from PyQt5 import QtCore, QtGui, QtWidgets
from form_type1 import Ui_FormType1
from constants import *
from style import *

class Ui_FormType3(Ui_FormType1):

    def createWidget(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 600)

        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(3, 3, 500, WINDOW_HIEGHT - 5))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 409, 189))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_2.setSpacing(1)


        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout.addWidget(self.lineEdit_1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)


        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(540, 55, 351, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.lineEdit_Name.setStyleSheet(LINE_EDIT_STYLE)
        self.horizontalLayout_2.addWidget(self.lineEdit_Name)

        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(540, 90, 351, 30))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_O = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_O.setStyleSheet(LINE_EDIT_STYLE)
        self.lineEdit_O.setObjectName("lineEdit_O")
        self.horizontalLayout_3.addWidget(self.lineEdit_O)

        self.layoutWidget_3 = QtWidgets.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(540, 165, 351, 30))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_Ex = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_Ex.setObjectName("lineEdit_Ex")
        self.lineEdit_Ex.setStyleSheet(LINE_EDIT_STYLE)
        self.horizontalLayout_4.addWidget(self.lineEdit_Ex)
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(800, 560, 90, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(BUTTON_STYLE)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 250, 150, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(BUTTON_STYLE)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 300, 150, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(BUTTON_STYLE)


        self.layoutWidget_4 = QtWidgets.QWidget(Form)
        self.layoutWidget_4.setGeometry(QtCore.QRect(540, 200, 351, 30))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setStyleSheet(COMBO_BOX_STYLE)

        self.horizontalLayout_6.addWidget(self.comboBox_2)
        self.layoutWidget_5 = QtWidgets.QWidget(Form)
        self.layoutWidget_5.setGeometry(QtCore.QRect(540, 130, 351, 30))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)

        self.comboBox = QtWidgets.QComboBox(self.layoutWidget_5)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setStyleSheet(COMBO_BOX_STYLE)

        self.horizontalLayout_7.addWidget(self.comboBox)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(540, 20, 351, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_FName = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_FName.setStyleSheet(LINE_EDIT_STYLE)
        self.lineEdit_FName.setStyleSheet(LINE_EDIT_STYLE)
        self.lineEdit_FName.setObjectName("lineEdit_FName")
        self.horizontalLayout.addWidget(self.lineEdit_FName)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Имя"))
        self.label_3.setText(_translate("Form", "Отчество"))
        self.label_4.setText(_translate("Form", "Опыт"))
        self.pushButton.setText(_translate("Form", "Назад"))
        self.pushButton_2.setText(_translate("Form", "Дабавить"))
        self.pushButton_3.setText(_translate("Form", "Обнрвить"))
        self.label_6.setText(_translate("Form", "Класс"))
        self.comboBox_2.setItemText(0, _translate("Form", "1"))
        self.comboBox_2.setItemText(1, _translate("Form", "2"))
        self.comboBox_2.setItemText(2, _translate("Form", "3"))
        self.comboBox_2.setItemText(3, _translate("Form", "4"))
        self.comboBox_2.setItemText(4, _translate("Form", "5"))
        self.comboBox_2.setItemText(5, _translate("Form", "6"))
        self.comboBox_2.setItemText(6, _translate("Form", "7"))
        self.comboBox_2.setItemText(7, _translate("Form", "8"))
        self.comboBox_2.setItemText(8, _translate("Form", "9"))
        self.comboBox_2.setItemText(9, _translate("Form", "10"))
        self.label_7.setText(_translate("Form", "Автобус"))
        self.comboBox.setItemText(0, _translate("Form", "Автобус"))
        self.label.setText(_translate("Form", "Фамилия"))

    def getRowsForUpdateTable(self):
        return []

    def getAddInTable(self, full_name, bus_id, experience, class_num):
        return []

    def connectBut(self):
        self.pushButton.clicked.connect(self.closeMe)
        self.pushButton_3.clicked.connect(self.clickUpdate)
        self.pushButton_2.clicked.connect(self.clickOK)

    def clickUpdate(self):
        rows = self.getRowsForUpdateTable()
        self.updateTable(rows)

    def clickOK(self):
        id = self.list_id[self.comboBox.currentIndex()]
        name = self.lineEdit_Name.text()
        fName = self.lineEdit_FName.text()
        oName = self.lineEdit_O.text()
        ex = self.lineEdit_Ex.text()
        class_num = self.comboBox_2.currentIndex() + 1
        self.getAddInTable(f'{fName} {name} {oName}', id, ex, class_num)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormType3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
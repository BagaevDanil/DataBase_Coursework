from PyQt5 import QtCore, QtGui, QtWidgets
from style import *
from constants import *

class Ui_FormType1(object):
    windowTitle = 'CommonForm'
    beAll = False

    def __init__(self, ParentForm = None):
        super().__init__()
        self.ParentForm = ParentForm

    def closeMe(self):
        if self.ParentForm is not None:
            self.ParentForm.show()
        self.Widget.close()
        
        
    def addItem(self):
        horizontalLayout = QtWidgets.QHBoxLayout()
        lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)

        horizontalLayout.addWidget(lineEdit_1)
        horizontalLayout.addWidget(lineEdit_2)
        horizontalLayout.addWidget(lineEdit_3)
        horizontalLayout.addWidget(lineEdit_4)

        self.verticalLayout_2.addLayout(horizontalLayout)
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def getRowsForUpdateComboBox(self):
        return []

    def updateComboBox(self):
        rows = self.getRowsForUpdateComboBox() 
        self.comboBox.clear() 
        
        self.list_id = []
        if self.beAll:
            self.comboBox.addItem(f'Все')
            self.list_id.append(-1)

        for row in rows:
            num = row['value']
            id = row['id']
            self.comboBox.addItem(f'{num}  (id:{id})')
            self.list_id.append(id)
    
    def clickOK(self):
        id = self.list_id[self.comboBox.currentIndex()]
        rows = self.getRowsForUpdateTable(id)
        self.updateTable(rows)

    def update(self, DB):
        self.DB = DB
        self.updateComboBox()
        self.clearTable()

    def getRowsForUpdateTable(self, idRoute):
        return []

    def updateTable(self, rows):
        self.clearTable()
        keys = []
        if rows:
            keys = rows[0].keys()

        for row in rows:
            horizontalLayout = QtWidgets.QHBoxLayout()
            for key in keys:
                val = row[key]
                lineEdit = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
                lineEdit.setText(str(val))
                lineEdit.setMinimumSize(QtCore.QSize(0, 80))
                lineEdit.setMaximumSize(QtCore.QSize(1000, 80))
                lineEdit.setStyleSheet(ITEM_HEAD_AREA_STYLE if rows.index(row) == 0 else  ITEM_AREA_STYLE)
                horizontalLayout.addWidget(lineEdit)

            self.verticalLayout_2.insertLayout(self.verticalLayout_2.count() - 1, horizontalLayout)

    def clearTable(self):
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        

    def setupUi(self, Widget):
        self.Widget = Widget

        self.createWidget(Widget)
        self.connectBut()
        self.retranslateUi(Widget)

        QtCore.QMetaObject.connectSlotsByName(Widget)

    def connectBut(self):
        self.pushButtonBack.clicked.connect(self.closeMe)  
        self.pushButton.clicked.connect(self.clickOK)

    def createWidget(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(WINDOW_WIDTH, WINDOW_HIEGHT)

        self.scrollArea = QtWidgets.QScrollArea(Widget)
        self.scrollArea.setGeometry(QtCore.QRect(3, 3, SCROLL_WIDTH, WINDOW_HIEGHT - 5))
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

        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(SCROLL_WIDTH + 20, 60, 140, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('Ок')
        self.pushButton.setStyleSheet(BUTTON_STYLE)
        
        self.comboBox = QtWidgets.QComboBox(Widget)
        self.comboBox.setGeometry(QtCore.QRect(SCROLL_WIDTH + 20, 20, 200, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet(COMBO_BOX_STYLE)
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")

        self.pushButtonBack = QtWidgets.QPushButton(Widget)
        self.pushButtonBack.setGeometry(QtCore.QRect(WINDOW_WIDTH - 120, 550, 100, 30))
        self.pushButton.setObjectName("pushButtonBack")
        self.pushButtonBack.setText('Назад')
        self.pushButtonBack.setStyleSheet(BUTTON_STYLE)
        

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(self.windowTitle)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_FormType1()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from form_ex import FormEx1, FormEx2, FormEx3, FormEx4, FormEx5

from db_connecter import TMyDB
from constants import *

class Ui_FormMainMenu(object):
    def __init__(self, DB):
        super().__init__()
        self.DB = DB

    '''
    Добавить сюда коннектор
    '''
    def connectBut(self):
        self.pushButton_1.clicked.connect(lambda : self.openForm(self.Form_1, self.ui_1))
        self.pushButton_2.clicked.connect(lambda : self.openForm(self.Form_2, self.ui_2))
        self.pushButton_3.clicked.connect(lambda : self.openForm(self.Form_3, self.ui_3))
        self.pushButton_4.clicked.connect(lambda : self.openForm(self.Form_4, self.ui_4))
        self.pushButton_5.clicked.connect(lambda : self.openForm(self.Form_5, self.ui_5))

    '''
    Добавить сюда форму
    '''
    def setupForms(self):
        self.Form_1 = QtWidgets.QWidget()
        self.ui_1 = FormEx1(self.Form)
        self.ui_1.setupUi(self.Form_1)

        self.Form_2 = QtWidgets.QWidget()
        self.ui_2 = FormEx2(self.Form)
        self.ui_2.setupUi(self.Form_2)

        self.Form_3 = QtWidgets.QWidget()
        self.ui_3 = FormEx3(self.Form)
        self.ui_3.setupUi(self.Form_3)

        self.Form_4 = QtWidgets.QWidget()
        self.ui_4 = FormEx4(self.Form)
        self.ui_4.setupUi(self.Form_4)

        self.Form_5 = QtWidgets.QWidget()
        self.ui_5 = FormEx5(self.Form)
        self.ui_5.setupUi(self.Form_5)
        # ...

    def openForm(self, form, ui):
        ui.update(self.DB)
        form.show()
        self.Form.close()

    def createWidget(self, Form):
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_1 = QtWidgets.QGroupBox(Form)
        self.groupBox_1.setObjectName("groupBox_1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout_4.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.verticalLayout.addWidget(self.groupBox_1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_6.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_6.addWidget(self.pushButton_10)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addLayout(self.verticalLayout_2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Главное меню"))
        self.groupBox_1.setTitle(_translate("Form", "Сведения"))
        self.pushButton_1.setText(_translate("Form", "Список водителей, работающих на определенном маршруте"))
        self.pushButton_2.setText(_translate("Form", "Номера автобусов, обслуживающих данный маршрут\n"""))
        self.pushButton_3.setText(_translate("Form", "Когда начинается или заканчивается движение автобусов \nна всех или отдельных маршрутах"))
        self.pushButton_4.setText(_translate("Form", "Какова протяженность всех или определенных маршрутов \nавтобусов"))
        self.pushButton_5.setText(_translate("Form", "На каких автобусах работает водитель"))
        self.groupBox_2.setTitle(_translate("Form", "Изменения"))
        self.pushButton_6.setText(_translate("Form", "Прием на работу нового водителя"))
        self.pushButton_7.setText(_translate("Form", "Списание старого автобуса"))
        self.pushButton_8.setText(_translate("Form", "Изменение протяженности маршрута"))
        self.groupBox_3.setTitle(_translate("Form", "Справки и отчеты"))
        self.pushButton_9.setText(_translate("Form", " Справки о протяженности маршрута"))
        self.pushButton_10.setText(_translate("Form", " Отчета по автопарку"))

    def setupUi(self, Form):
        self.Form = Form

        Form.setObjectName("Form")
        Form.resize(800, 600)

        self.setupForms()
        self.createWidget(Form)
        self.retranslateUi(Form)
        self.connectBut()

        QtCore.QMetaObject.connectSlotsByName(Form)

    


if __name__ == "__main__":
    '''
    Connect with DaatBase
    '''
    DB = TMyDB(HOST, PORT, USER, PASS, DB_NAME)

    '''
    Create application and start-window
    '''
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormMainMenu(DB)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

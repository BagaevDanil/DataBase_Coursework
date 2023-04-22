from PyQt5 import QtCore, QtGui, QtWidgets
from form_ex import FormEx1, FormEx2, FormEx3, FormEx4, FormEx5, FormEx6, FormEx7, FormEx8

from db_connecter import TMyDB
from constants import *

import tkinter as tk
from tkinter import messagebox as mbox
from tkinter import filedialog as fd

from style import *

class Ui_FormMainMenu(object):
    def __init__(self, DB):
        super().__init__()
        self.DB = DB

    def writeFromDict(self, headText, label, data, file):
        file.write(f'{headText} : \n\n')
        keys = label.keys()
        for item in data:
            for key in keys:
                file.write(f'    {label[key]} : {item[key]}\n')
            file.write('\n')

    def makeReport(self):
        file_path = fd.asksaveasfilename(defaultextension = "txt")
        try:
            with open(file_path, 'w') as file:
                # Bus
                label, data = self.DB.makeReportGetBus()
                self.writeFromDict(
                    headText='Количество автобусов и их тип',
                    label=label,
                    data=data,
                    file=file
                )

                # Route
                label, data = self.DB.makeReportGetRoute()
                self.writeFromDict(
                    headText='Номера маршрутов, время начала движения и интервал',
                    label=label,
                    data=data,
                    file=file
                )

                # Driver
                label, data = self.DB.makeReportGetDriver()
                self.writeFromDict(
                    headText='ФИО водителей и их класс',
                    label=label,
                    data=data,
                    file=file
                )
            mbox.showinfo('Отчет', 'Отчет готов!')
        except Exception as ex:
            mbox.showerror('Отчет', 'Ошибка, отчет не сохранен')

        


    '''
    Добавить сюда коннектор
    '''
    def connectBut(self):
        self.pushButton_1.clicked.connect(lambda : self.openForm(self.Form_1, self.ui_1))
        self.pushButton_2.clicked.connect(lambda : self.openForm(self.Form_2, self.ui_2))
        self.pushButton_3.clicked.connect(lambda : self.openForm(self.Form_3, self.ui_3))
        self.pushButton_4.clicked.connect(lambda : self.openForm(self.Form_4, self.ui_4))
        self.pushButton_5.clicked.connect(lambda : self.openForm(self.Form_5, self.ui_5))
        self.pushButton_6.clicked.connect(lambda : self.openForm(self.Form_6, self.ui_6))
        self.pushButton_7.clicked.connect(lambda : self.openForm(self.Form_7, self.ui_7))
        self.pushButton_8.clicked.connect(lambda : self.openForm(self.Form_8, self.ui_8))
        self.pushButton_9.clicked.connect(lambda : self.openForm(self.Form_4, self.ui_4))
        self.pushButton_10.clicked.connect(self.makeReport)

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

        self.Form_6 = QtWidgets.QWidget()
        self.ui_6 = FormEx6(self.Form)
        self.ui_6.setupUi(self.Form_6)

        self.Form_7 = QtWidgets.QWidget()
        self.ui_7 = FormEx7(self.Form)
        self.ui_7.setupUi(self.Form_7)

        self.Form_8 = QtWidgets.QWidget()
        self.ui_8 = FormEx8(self.Form)
        self.ui_8.setupUi(self.Form_8)
        # ...

    def openForm(self, form, ui):
        ui.update(self.DB)
        form.show()
        self.Form.close()

    def createWidget(self, Form):
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 500, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout_4.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
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
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
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
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(610, 120, 170, 33))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(520, 10, 260, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Главное меню"))
        self.groupBox.setTitle(_translate("Form", "Сведения"))
        self.groupBox_2.setTitle(_translate("Form", "Изменения"))
        self.pushButton_1.setText(_translate("Form", "Список водителей, работающих на определенном маршруте"))
        self.pushButton_2.setText(_translate("Form", "Номера автобусов, обслуживающих данный маршрут\n"""))
        self.pushButton_3.setText(_translate("Form", "Когда начинается или заканчивается движение автобусов \nна всех или отдельных маршрутах"))
        self.pushButton_4.setText(_translate("Form", "Какова протяженность всех или определенных маршрутов \nавтобусов"))
        self.pushButton_5.setText(_translate("Form", "На каких автобусах работает водитель"))
        self.groupBox_2.setTitle(_translate("Form", "Изменения"))
        self.pushButton_6.setText(_translate("Form", "Прием на работу нового водителя"))
        self.pushButton_7.setText(_translate("Form", "Списание старого автобуса"))
        self.pushButton_8.setText(_translate("Form", "Изменение протяженности маршрута"))
        self.pushButton_9.setText(_translate("Form", " Справки о протяженности маршрута"))
        self.pushButton_10.setText(_translate("Form", " Отчета по автопарку"))
        self.pushButton.setText(_translate("Form", "Войти в аккуанут"))
        self.label.setText(_translate("Form", "Логин"))
        self.label_2.setText(_translate("Form", "Пароль"))

        self.pushButton_1.setStyleSheet(BUTTON_STYLE)
        self.pushButton_2.setStyleSheet(BUTTON_STYLE)
        self.pushButton_3.setStyleSheet(BUTTON_STYLE)
        self.pushButton_4.setStyleSheet(BUTTON_STYLE)
        self.pushButton_5.setStyleSheet(BUTTON_STYLE)
        self.pushButton_6.setStyleSheet(BUTTON_STYLE)
        self.pushButton_7.setStyleSheet(BUTTON_STYLE)
        self.pushButton_8.setStyleSheet(BUTTON_STYLE)
        self.pushButton_9.setStyleSheet(BUTTON_STYLE)
        self.pushButton_10.setStyleSheet(BUTTON_STYLE)
        self.pushButton.setStyleSheet(BUTTON_STYLE)


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

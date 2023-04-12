from form_main import Ui_FormMainMenu
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from db_connecter import TMyDB
from constants import *

if __name__ == "__main__":

    '''
    Connect with DaatBase
    '''
    DB = TMyDB(HOST, PORT, USER, PASS, DB_NAME)


    '''
    Create application and start-window
    '''
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_FormMainMenu(DB)
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
    
from form_type1 import Ui_FormType1
from form_type2 import Ui_FormType2
from form_type3 import Ui_FormType3
from form_type4 import Ui_FormType4
from form_type5 import Ui_FormType5

class FormEx1(Ui_FormType1):
    def __init__(self, ParentForm=None):
        super().__init__(ParentForm)
        '''
        Название
        '''
        self.windowTitle = 'Задание №1'

    def getRowsForUpdateComboBox(self):
        '''
        Подставить метод, который возращает список, 
        где каждый элемент -- словарь вида:
        '''
        return self.DB.ex1_GetListRoute() 
    
    def getRowsForUpdateTable(self, idRoute):
        '''
        Подставить метод, который возращает список, 
        где каждый элемент -- словарь строки (rows):
        '''
        return self.DB.ex1_GetListDriver(idRoute)


class FormEx2(Ui_FormType1):
    def __init__(self, ParentForm=None):
        super().__init__(ParentForm)
        self.windowTitle = 'Задание №2'
    
    def getRowsForUpdateComboBox(self):
        return self.DB.ex2_GetListRoute() # {key : '', value : ''}
    
    def getRowsForUpdateTable(self, idRoute):
        return self.DB.ex2_GetListBus(idRoute)

class FormEx3(Ui_FormType2):
    def __init__(self, ParentForm=None):
        super().__init__(ParentForm)
        self.windowTitle = 'Задание №3'
        self.listItemsComboBox2 = ['Начинается', 'Заканчивается'] # Элементы во втором ComboBox, id2 -- выбранный эелемент (по порядку)
        self.beAll = True # Появляется возможность выбрать элемент 'ВСЕ' с индексом -1
    
    def getRowsForUpdateComboBox(self):
        return self.DB.ex3_GetListRoute() 
    
    def getRowsForUpdateTable(self, idRoute, id2):
        return self.DB.ex3_GetListTime(idRoute, isFinish=id2)


class FormEx4(Ui_FormType1):
    def __init__(self, ParentForm=None):
        super().__init__(ParentForm)
        self.windowTitle = 'Задание №4'
        self.beAll = True
    
    def getRowsForUpdateComboBox(self):
        return self.DB.ex4_GetListRoute() 
    
    def getRowsForUpdateTable(self, idRoute):
        return self.DB.ex4_GetListDist(idRoute)

class FormEx5(Ui_FormType1):
    def __init__(self, ParentForm=None):
        super().__init__(ParentForm)
        self.windowTitle = 'Задание №5'
    
    def getRowsForUpdateComboBox(self):
        return self.DB.ex5_GetListDriver() 
    
    def getRowsForUpdateTable(self, idRoute):
        return self.DB.ex5_GetListBus(idRoute)


class FormEx6(Ui_FormType3):
    def __init__(self, ParentForm=None):
        super().__init__(ParentForm)
        self.windowTitle = 'Задание №6'
    
    def getRowsForUpdateComboBox(self):
        return self.DB.ex6_GetListBus() 
    
    def getRowsForUpdateTable(self):
        return self.DB.ex6_GetDrivers()

    def getAddInTable(self, full_name, bus_id, experience, class_num):
        self.DB.ex6_AddDrivers(full_name, bus_id, experience, class_num)


class FormEx7(Ui_FormType4):
    def __init__(self, ParentForm=None):
        super().__init__(ParentForm)
        self.windowTitle = 'Задание №7'

    def getRowsForUpdateComboBox(self):
        return self.DB.ex7_GetListBus() 
    
    def getRowsForUpdateTable(self):
        return self.DB.ex7_GetListBusTable() 
    
    def deleteRow(self, id):
        self.DB.ex7_deleteBus(id) 


class FormEx8(Ui_FormType5):
    def __init__(self, ParentForm=None):
        super().__init__(ParentForm)
        self.windowTitle = 'Задание №8'

    def getRowsForUpdateComboBox(self):
        return self.DB.ex8_GetRoute() 
    
    def getRowsForUpdateTable(self):
        return self.DB.ex8_GetRouteTable() 
    
    def changeRow(self, id, data):
        self.DB.ex8_changeDist(id, data) 
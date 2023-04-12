from form_type1 import Ui_FormType1
from form_type2 import Ui_FormType2

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
        {value (значения, из которых состоит ComboBox) :  id (id этого элемента в таблице)}
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
        return self.DB.ex2_GetListRoute() 
    
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
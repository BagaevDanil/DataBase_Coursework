ITEM_AREA_STYLE = '''
    QTextBrowser {
    color: black;
    border: 1px solid black;
    border-radius: 0px;
    background-color: white
    } 
'''

ITEM_HEAD_AREA_STYLE = '''
    QTextBrowser {
    color: black;
    border: 2px solid black;
    border-radius: 0px;
    background-color: rgb(197,203,255,255)
    } 
'''

LINE_EDIT_STYLE = '''
    QLineEdit {
    color: black;
    padding: .5em 2em;
    border: 1px solid black;
    border-radius: 4px;
    background-color: white;
    } 
'''

BUTTON_STYLE = '''
    QPushButton {
    color: black;
    font-size: 13px;
    text-decoration: none;
    padding: .5em 2em;
    outline: none;
    border: 1px solid black;
    border-radius: 4px;
    background-color: white;
    } 
    QPushButton::hover{ background: rgb(235, 235, 235) }
    QPushButton:pressed { background: rgb(221, 221, 221) }
'''


COMBO_BOX_STYLE = '''
    QComboBox {
        border: 1px solid black;
        border-radius: 4px;
        padding: 1px 18px 1px 3px;
        min-width: 6em;
        font-size: 13px;
    }

    QComboBox:editable {
        background: white;
    }

    QComboBox:!editable, QComboBox::drop-down:editable {
        background: white;
    }

   
    QComboBox:!editable:on, QComboBox::drop-down:editable:on {
        background: grey;
    }

    QComboBox:on {
        padding-top: 3px;
        padding-left: 4px;
    }

    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;

        
    }

    QComboBox QAbstractItemView {
        border: 2px solid white;
        selection-background-color: lightgray;
        background: white;
    }
'''
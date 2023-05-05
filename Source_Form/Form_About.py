import sys
sys.path.append('..')

import Source_Ui.UI_About as UI_About
from PyQt5 import QtGui


class Form_About(UI_About.Ui_Ui_AboutWindow):
    def setupUi(self, form_Cloud):
        super().setupUi(form_Cloud)
        form_Cloud.setWindowIcon(QtGui.QIcon('img/icon/icon_About.ico'))
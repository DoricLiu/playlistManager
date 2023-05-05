import cgitb
cgitb.enable(format='text')
import Source_Form.Form_Main as form_main
import Source_Other.DialogClass as DialogClass

from PyQt5 import QtWidgets

if __name__ == '__main__':
    import sys
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    app.aboutToQuit.connect(app.deleteLater)
    MainWindow = DialogClass.VideoWindow()
    ui = form_main.Form_Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
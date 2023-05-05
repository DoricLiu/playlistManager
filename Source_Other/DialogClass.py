from PyQt5 import QtCore, QtGui, QtWidgets

class VideoDialog(QtWidgets.QDialog):

    def setupUi(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        
    def mouseMoveEvent(self, event):
        m_pos = event.globalPos()
        m_pos = m_pos - QtWidgets.QWidget.mapToGlobal(self, QtCore.QPoint(
            0, 0))
        if event.buttons() == QtCore.Qt.LeftButton and m_pos.y() < 20:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def mousePressEvent(self, event):
        m_pos = event.globalPos()
        m_pos = m_pos - QtWidgets.QWidget.mapToGlobal(self, QtCore.QPoint(
            0, 0))
        if event.button() == QtCore.Qt.LeftButton and m_pos.y() < 20:
            self.dragPosition = event.globalPos(
            ) - self.frameGeometry().topLeft()
            QtWidgets.QApplication.postEvent(self, QtCore.QEvent(174))
            event.accept()

class VideoWindow(QtWidgets.QMainWindow):
    def setupUi(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)

    def mouseMoveEvent(self, event):
        m_pos = event.globalPos()
        m_pos = m_pos - QtWidgets.QWidget.mapToGlobal(self, QtCore.QPoint(
            0, 0))
        if event.buttons() == QtCore.Qt.LeftButton and m_pos.y() < 20:
            try:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
            except Exception as e:
                print('')

    def mousePressEvent(self, event):
        m_pos = event.globalPos()
        m_pos = m_pos - QtWidgets.QWidget.mapToGlobal(self, QtCore.QPoint(
            0, 0))
        if event.button() == QtCore.Qt.LeftButton and m_pos.y() < 20:
            self.dragPosition = event.globalPos() - self.frameGeometry(
            ).topLeft()
            QtWidgets.QApplication.postEvent(self, QtCore.QEvent(174))
            event.accept()
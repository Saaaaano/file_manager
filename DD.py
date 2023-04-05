from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class MyLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFixedSize(400, 400)
        self.setStyleSheet('''
            border: 2px dashed #aaa
        ''')

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            mime_data = QtCore.QMimeData()
            file_path = 'C://Users/sasan/Pictures/SW20.png'
            file = open(file_path, 'rb')
            file_data = file.read()
            file.close()
            mime_data.setData('application/octet-stream', file_data)
            drag = QtGui.QDrag(self)
            drag.setMimeData(mime_data)
            drag.setPixmap(QtGui.QPixmap(file_path).scaled(
                200, 200, QtCore.Qt.KeepAspectRatio))
            drag.exec_(QtCore.Qt.MoveAction)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.setPixmap(QtGui.QPixmap(file_path).scaled(
                400, 400, QtCore.Qt.KeepAspectRatio))
            event.accept()
        else:
            event.ignore()


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('ファイルドラッグ＆ドロップ')
        layout = QtWidgets.QVBoxLayout()
        self.label = MyLabel()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())

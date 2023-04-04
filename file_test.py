# - * - coding: utf8 - * -

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):  # QMainWindowクラスを使用します。

    def __init__(self):
        super().__init__()
        self.title = '素材管理'
        self.width = 500
        self.height = 400
        self.initUI()

    def initUI(self):

        # メニューバー
        exitAction = QAction('&終了', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('画面を閉じる')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&ファイル')
        fileMenu.addAction(exitAction)  # fileMenuにアクションを追加します。

        self.setWindowTitle(self.title)
        # setGeometry(x,y,横幅,高さ)
        self.setGeometry(0, 0, self.width, self.height)
        # ステータスバーを表示
        self.statusBar().showMessage('ここがステータスバーだよ')
        self.show()


def main():
    app = QApplication(sys.argv)
    gui = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

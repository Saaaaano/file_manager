import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, qApp, QScrollArea, QAction
from PIL.ImageQt import Image, ImageQt


class ImageViewer(QMainWindow):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.initUI()

    def initUI(self):

        #--- メニューバー ---#
        exitAction = QAction('&終了', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('画面を閉じる')
        exitAction.triggered.connect(qApp.quit)

        settingsAction = QAction('&設定', self)
        settingsAction.setShortcut('Ctrl+S')
        settingsAction.setStatusTip('設定画面を表示する')
        settingsAction.triggered.connect(self.show_settings)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&ファイル')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(settingsAction)

        # スクロール可能なウィジェットを作成
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.scroll_widget = QtWidgets.QWidget(scroll_area)
        scroll_area.setWidget(self.scroll_widget)

        # 画像を表示するグリッドレイアウトを作成
        layout = QtWidgets.QGridLayout(self.scroll_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(0)

        # フォルダ内のファイルを一覧表示する
        row = 0
        col = 0
        for file_name in os.listdir(self.path):
            if file_name.endswith(('.png', '.jpg', '.bmp', '.gif')):
                file_path = os.path.join(self.path, file_name)
                # 画像をリサイズ
                img = Image.open(file_path)
                img.thumbnail((100 , 100))
                # 画像を表示するラベルを作成
                qimage = ImageQt(img.convert('RGBA'))
                pixmap = QPixmap.fromImage(qimage)
                label = QtWidgets.QLabel(self.scroll_widget)
                label.setMargin(10)
                label.setPixmap(pixmap)
                layout.addWidget(label, row, col)

                # マウスイベントを追加
                label.enterEvent = lambda event, label=label: label.setStyleSheet('background-color: lightgray')
                label.leaveEvent = lambda event, label=label: label.setStyleSheet('')
                # ダブルクリックイベントを追加
                label.mouseDoubleClickEvent = lambda event, path=file_path: self.open_file(path)
                col += 1
                if col == 5:
                    row += 1
                    col = 0

        self.scroll_widget.setLayout(layout)

        # レイアウトを設定
        central_widget = QtWidgets.QWidget(self)
        main_layout = QtWidgets.QVBoxLayout(central_widget)
        main_layout.addWidget(scroll_area)
        self.setCentralWidget(central_widget)

        # ウィンドウのサイズを指定
        self.setMinimumSize(640, 480)

    def show_settings(self):
        print('設定画面を表示する')

    def open_file(self, file_path):
        # ファイルを開く
        os.startfile(file_path)


if __name__ == '__main__':
    # PyQt5アプリケーションを初期化
    app = QtWidgets.QApplication([])

    # 画像を表示するウィンドウを作成
    path = r'D:\素材\背景'
    viewer = ImageViewer(path)
    viewer.show()

    # PyQt5のイベントループを開始
    app.exec_()

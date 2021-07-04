from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QIcon, QPixmap

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Janela do sistema')
        self.setGeometry(300, 100, 800, 600) # x, y, w, h -> esq, topo, largura, altrua
        self.setMinimumHeight(100)
        self.setMinimumWidth(400)
        self.setMaximumHeight(900)
        self.setMaximumWidth(1000)
        self.setToolTip('Janela de Login')

        self.setAutoFillBackground(True)
        self.setStyleSheet('background-color: #00bfff;')

        appIcon = QIcon('imgs/logo.png')
        self.setWindowIcon(appIcon)

        self.set_img()

    def set_img(self):
        # Primeiro Ícone
        icone1 = QIcon('imgs/icon_check.png')
        label1 = QLabel('Palavra', self)
        pixmap1 = icone1.pixmap(100, 100, QIcon.Active)

        label1.setPixmap(pixmap1)

        # Segundo Ícone
        icone2 = QIcon('imgs/icon_check.png')
        label2 = QLabel('Palavra', self)
        label2.move(100, 0)
        pixmap2 = icone2.pixmap(100, 100, QIcon.Disabled)

        label2.setPixmap(pixmap2)

        # Terceiro Ícone
        icone3 = QIcon('imgs/icon_check.png')
        label3 = QLabel('Palavra', self)
        label3.move(200, 0)
        pixmap3 = icone3.pixmap(100, 100, QIcon.Selected)

        label3.setPixmap(pixmap3)

myApp = QApplication(sys.argv)

janela = Window()
janela.show()
myApp.exec_()
sys.exit(0)

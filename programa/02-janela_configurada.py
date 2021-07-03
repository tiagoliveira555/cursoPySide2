from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon

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

        appIcon = QIcon('imgs/logo.png')
        self.setWindowIcon(appIcon)


myApp = QApplication(sys.argv)

janela = Window()
janela.show()
myApp.exec_()
sys.exit(0)

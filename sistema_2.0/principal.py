from PySide2.QtWidgets  import QApplication, QWidget, QPushButton
from PySide2.QtGui import QFont

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Syscad :: Janela Principal')
        self.setGeometry(300,300,1000,700)
        self.setStyleSheet('background-color: rgb(7, 104, 114)')

        self.define_formulario()

    def define_formulario(self):
        self.fonte = QFont('_fonts/Raleway-Light.ttf')
        self.fonte.setPointSize(10)

        self.btn_cadastrar = QPushButton('Cadastrar', self)
        self.btn_cadastrar.setFont(self.fonte)
        self.btn_cadastrar.setGeometry(0, 0, 170, 50)
        self.btn_cadastrar.setStyleSheet('color: white')
        self.btn_cadastrar.clicked.connect(self.exibir_frame_cadastro)

        self.btn_pesquisar = QPushButton('Pesquisar', self)
        self.btn_pesquisar.setFont(self.fonte)
        self.btn_pesquisar.setGeometry(0, 50, 170, 50)
        self.btn_pesquisar.setStyleSheet('color: white')
        self.btn_pesquisar.clicked.connect(self.exibir_frame_pesquisa)

        self.btn_relatorio = QPushButton('Relatório', self)
        self.btn_relatorio.setFont(self.fonte)
        self.btn_relatorio.setGeometry(0, 100, 170, 50)
        self.btn_relatorio.setStyleSheet('color: white')
        self.btn_relatorio.clicked.connect(self.exibir_frame_relatorio)

        self.btn_editar = QPushButton('Editar', self)
        self.btn_editar.setFont(self.fonte)
        self.btn_editar.setGeometry(0, 150, 170, 50)
        self.btn_editar.setStyleSheet('color: white')
        self.btn_editar.clicked.connect(self.exibir_frame_editar)

    def exibir_frame_cadastro(self):
        print('Cadastrar')

    def exibir_frame_pesquisa(self):
        print('Pesquisar')

    def exibir_frame_relatorio(self):
        print('Relatório')

    def exibir_frame_editar(self):
        print('Editar')

def executa():
    myApp = QApplication.instance()
    if myApp is None:
        myApp = QApplication(sys.argv)

    window = Window()
    window.show()

    myApp.exec_()


executa()

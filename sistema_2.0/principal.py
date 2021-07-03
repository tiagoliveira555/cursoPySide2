from PySide2.QtWidgets  import QApplication, QWidget, QPushButton, QFrame
from PySide2.QtGui import QFont

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Syscad :: Janela Principal')
        self.setGeometry(200, 150, 1024, 576)
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

        '''
        FRAME DE CADASTRO ===========================================
        Frame não visível e só aparece quando clico no botão Cadastrar
        '''

        global frm_cadastro
        self.frm_cadastro = QFrame(self)
        self.frm_cadastro.setGeometry(170, 0, 854, 576)
        self.frm_cadastro.setStyleSheet('background-color: white')
        self.frm_cadastro.setVisible(False)

        '''
        FRAME DE PESQUISAR ===========================================
        Frame não visível e só aparece quando clico no botão Pesquisar
        '''

        global frm_pesquisar
        self.frm_pesquisar = QFrame(self)
        self.frm_pesquisar.setGeometry(170, 0, 854, 576)
        self.frm_pesquisar.setStyleSheet('background-color: yellow')
        self.frm_pesquisar.setVisible(False)

        '''
        FRAME DE RELATORIO ===========================================
        Frame não visível e só aparece quando clico no botão Relatório
        '''

        global frm_relatorio
        self.frm_relatorio = QFrame(self)
        self.frm_relatorio.setGeometry(170, 0, 854, 576)
        self.frm_relatorio.setStyleSheet('background-color: green')
        self.frm_relatorio.setVisible(False)

        '''
        FRAME DE EDITAR ===========================================
        Frame não visível e só aparece quando clico no botão Editar
        '''

        global frm_editar
        self.frm_editar = QFrame(self)
        self.frm_editar.setGeometry(170, 0, 854, 576)
        self.frm_editar.setStyleSheet('background-color: red')
        self.frm_editar.setVisible(False)

        global meus_frames
        self.meus_frames = (self.frm_cadastro, self.frm_pesquisar,
                            self.frm_relatorio, self.frm_editar)


    def ocultar_frames(self):
        global meus_frames
        for f in self.meus_frames:
            if f.isVisible() == True:
                f.setVisible(False)


    def exibir_frame_cadastro(self):
        global frm_cadastro
        self.ocultar_frames()
        self.frm_cadastro.setVisible(True)


    def exibir_frame_pesquisa(self):
        global frm_pesquisar
        self.ocultar_frames()
        self.frm_pesquisar.setVisible(True)


    def exibir_frame_relatorio(self):
        global frm_relatorio
        self.ocultar_frames()
        self.frm_relatorio.setVisible(True)


    def exibir_frame_editar(self):
        global frm_editar
        self.ocultar_frames()
        self.frm_editar.setVisible(True)


def executa():
    myApp = QApplication.instance()
    if myApp is None:
        myApp = QApplication(sys.argv)

    window = Window()
    window.show()

    myApp.exec_()


executa()

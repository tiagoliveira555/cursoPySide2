from PySide2.QtWidgets  import (QApplication, QWidget, QPushButton, QFrame,
QLabel, QLineEdit, QTableView, QHeaderView)
from PySide2.QtGui import QFont

from modelo import CustomTableModel
import banco as b

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

        self.lbl_nome = QLabel('Nome', self.frm_cadastro)
        self.lbl_nome.setGeometry(15, 50, 60, 16)

        self.lbl_end = QLabel('Endereço', self.frm_cadastro)
        self.lbl_end.setGeometry(15, 90, 60, 16)

        self.lbl_cpf = QLabel('CPF', self.frm_cadastro)
        self.lbl_cpf.setGeometry(15, 130, 60, 16)

        self.txt_nome = QLineEdit(self.frm_cadastro)
        self.txt_nome.setGeometry(80, 50, 750, 22)

        self.txt_end = QLineEdit(self.frm_cadastro)
        self.txt_end.setGeometry(80, 90, 750, 22)

        self.txt_cpf = QLineEdit(self.frm_cadastro)
        self.txt_cpf.setGeometry(80, 130, 120, 22)

        self.btn_limpar = QPushButton('Limpar', self.frm_cadastro)
        self.btn_limpar.setGeometry(20, 520, 115, 22)

        self.btn_gravar = QPushButton('Gravar', self.frm_cadastro)
        self.btn_gravar.setGeometry(710, 520, 115, 22)


        '''
        FRAME DE PESQUISAR ===========================================
        Frame não visível e só aparece quando clico no botão Pesquisar
        '''

        global frm_pesquisar
        self.frm_pesquisar = QFrame(self)
        self.frm_pesquisar.setGeometry(170, 0, 854, 576)
        self.frm_pesquisar.setStyleSheet('background-color: white')
        self.frm_pesquisar.setVisible(False)

        self.lbl_nome = QLabel('Nome', self.frm_pesquisar)
        self.lbl_nome.setGeometry(15, 50, 55, 16)

        self.txt_nome = QLineEdit(self.frm_pesquisar)
        self.txt_nome.setGeometry(80, 50, 600, 22)

        self.btn_pesquisar = QPushButton('Pesquisar', self.frm_pesquisar)
        self.btn_pesquisar.setGeometry(710, 50, 80, 22)

        '''
        FRAME DE RELATORIO ===========================================
        Frame não visível e só aparece quando clico no botão Relatório
        '''

        global frm_relatorio
        self.frm_relatorio = QFrame(self)
        self.frm_relatorio.setGeometry(170, 0, 854, 576)
        self.frm_relatorio.setStyleSheet('background-color: white')
        self.frm_relatorio.setVisible(False)

        dados = b.consulta()
        self.modelo = CustomTableModel(dados)

        self.tabela = QTableView(self.frm_relatorio)
        self.tabela.setGeometry(15, 20, 820, 540)
        self.tabela.setModel(self.modelo)
        self.tabela.setColumnWidth(0, 50)
        self.tabela.setColumnWidth(1, 300)
        self.tabela.setColumnWidth(2, 300)

        self.titulos = self.tabela.horizontalHeader()
        self.titulos.setSectionResizeMode(QHeaderView.Interactive)
        self.titulos.setStretchLastSection(True)


        '''
        FRAME DE EDITAR ===========================================
        Frame não visível e só aparece quando clico no botão Editar
        '''

        global frm_editar
        self.frm_editar = QFrame(self)
        self.frm_editar.setGeometry(170, 0, 854, 576)
        self.frm_editar.setStyleSheet('background-color: white')
        self.frm_editar.setVisible(False)

        self.campo_busca = QLineEdit(self.frm_editar)
        self.campo_busca.setGeometry(15, 15, 110, 22)
        self.campo_busca.setPlaceholderText('000.000.000-00')

        self.lbl_nome_edit = QLabel('Nome', self.frm_editar)
        self.lbl_nome_edit.setGeometry(15, 50, 60, 16)

        self.lbl_end_edit = QLabel('Endereço', self.frm_editar)
        self.lbl_end_edit.setGeometry(15, 90, 60, 16)

        self.lbl_cpf_edit = QLabel('CPF', self.frm_editar)
        self.lbl_cpf_edit.setGeometry(15, 130, 60, 16)

        self.txt_nome_edit = QLineEdit(self.frm_editar)
        self.txt_nome_edit.setGeometry(80, 50, 750, 22)

        self.txt_end_edit = QLineEdit(self.frm_editar)
        self.txt_end_edit.setGeometry(80, 90, 750, 22)

        self.txt_cpf_edit = QLineEdit(self.frm_editar)
        self.txt_cpf_edit.setGeometry(80, 130, 750, 22)

        self.btn_gravar_edit = QPushButton('Gravar', self.frm_editar)
        self.btn_gravar_edit.setGeometry(710, 520, 115, 22)


        '''
        ============================================================
        '''

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

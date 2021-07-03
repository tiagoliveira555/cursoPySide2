from PySide2.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton,
QLabel, QMessageBox)
from PySide2.QtGui import QFont, QIcon

import controle as c
import sys


class Window(QWidget):
    global logou, tentativas
    logou = False
    tentativas = 0

    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 600)
        self.setWindowTitle('Syscad :: Login')
        self.setAutoFillBackground(True)
        self.setStyleSheet('background-color:white;')

        self.definir_formulario()
        self.definir_imagens()

    def definir_formulario(self):
        global txt_usuario, txt_senha

        fonte = QFont('_fonts/Raleway-Medium.ttf')
        fonte.setPointSize(11)

        txt_usuario = QLineEdit(self)
        txt_usuario.setPlaceholderText('Usuário')
        txt_usuario.setFont(fonte)
        txt_usuario.setGeometry(10, 240, 381, 41)

        txt_senha = QLineEdit(self)
        txt_senha.setPlaceholderText('Senha')
        txt_senha.setFont(fonte)
        txt_senha.setGeometry(10, 320, 381, 41)
        txt_senha.setEchoMode(QLineEdit.EchoMode.Password)

        btn_logar = QPushButton('Logar', self)
        btn_logar.setFont(fonte)
        btn_logar.setGeometry(10, 390, 381, 41)
        btn_logar.setStyleSheet('background-color: rgb(7, 105, 114);color: white')
        btn_logar.clicked.connect(self.validar_login)

    def definir_imagens(self):
        appIcon = QIcon('_imgs/fav_icon.png')
        img_login = QIcon('_imgs/icon_login.png')
        img_base = QIcon('_imgs/icon_login_base.png')

        pixmap_logo = img_login.pixmap(191, 191)
        pixmap_base = img_base.pixmap(400, 220)

        label_logo = QLabel('Logo', self)
        label_logo.setPixmap(pixmap_logo)
        label_logo.move(100, 10)

        label_base = QLabel('Base', self)
        label_base.setPixmap(pixmap_base)
        label_base.setGeometry(0, 440, 411, 161)

        self.setWindowIcon(appIcon)

    def validar_login(self):
        global tentativas

        us = txt_usuario.text()
        pw = txt_senha.text()

        if c.validar_usuario(us, pw):
            logou = True
            self.close()
        else:
            if tentativas < 3:
                msg = QMessageBox()
                msg.setText('Login ou senha incorretos')
                msg.exec()
                tentativas += 1
                if tentativas == 3:
                    sys.exit()


def executa():
    global logou

    myApp = QApplication.instance()

    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = Window()
    janela.show()
    myApp.exec_()
    return logou

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.montar_formulario()


    def montar_formulario(self):
        btn1 = QPushButton('Ok', self)
        btn1.move(50, 100)
        btn1.clicked.connect(self.acao_do_botao)


    def acao_do_botao(self):
        info = QMessageBox.question(self, 'Confirmação',
        'Parabéns, você clicou no botão',
        QMessageBox.Yes | QMessageBox.No)

        if info == QMessageBox.Yes:
            print('Você clicou no botão Sim!')
        else:
            print('Você clicou no botão Não!')


myApp = QApplication(sys.argv)

janela = Window()
janela.show()
myApp.exec_()
sys.exit(0)

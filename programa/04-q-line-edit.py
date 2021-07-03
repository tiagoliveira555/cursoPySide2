from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PySide2.QtGui  import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 250, 300)
        self.setWindowTitle('Jenela QLineEdit')

        self.montar_formulario()


    def montar_formulario(self):
        fonte = QFont('fonts/Raleway-Medium.ttf')
        fonte.setPointSize(11)

        lbl_nome = QLabel('Nome', self)
        lbl_nome.move(20, 20)
        lbl_nome.setFont(fonte)

        campo1 = QLineEdit(self)
        campo1.move(20, 50)
        campo1.setFont(fonte)

        campo2 = QLineEdit(self)
        campo2.move(20, 90)
        campo2.setFont(fonte)
        campo2.setPlaceholderText('Digite sua senha')
        campo2.setEchoMode(QLineEdit.EchoMode.Password)


myApp = QApplication(sys.argv)

janela = Window()
janela.show()
myApp.exec_()
sys.exit(0)

import view_login as vl

import sys

def carrega_sistema():
    logou = vl.executa()
    if logou: # if logou == True:
        print('abre a parte principal do sistema')


carrega_sistema()

sys.exit(0)

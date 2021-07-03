import view_login as vl
import principal as p

import sys

def carrega_sistema():
    logou = vl.executa()
    if logou: # if logou == True:
        p.executa()


carrega_sistema()

sys.exit(0)

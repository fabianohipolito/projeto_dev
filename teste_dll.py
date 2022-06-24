import ctypes
import sys
from time import sleep
from unittest.util import strclass
#from weakref import ref

library = ctypes.WinDLL("C:\Users\f4qrkbr\OneDrive - Fiserv Corp\Automacao\Teste_dll\CliSiTef64I.dll")



P = str("192.168.54.233")
D = str("ARFISV01")
pterminalID = str("AR000001")



ret = int(library.ConfiguraIntSiTefInterativoEx("192.168.54.233", "ARFISV01", "AR000001", 0, "[CUIT=30712192662;CUITISV=30712192662]"))
if ret != 0:
    print ("Erro na inicializacao da DLL ", ret)
else:
    print ("CONFIG OK\n")

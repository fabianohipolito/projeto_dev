import random
from datetime import date, datetime
from re import U, X
from time import time
import re
import json

#pago = random.randint(1, 9 )

chavesl = "U+007B"
x = u'\ud800'
cuit = int(input("Informe o numero do cuit: "))
aspas = ('"{}"'.format(cuit))
#print("{{{}}}".format(aspas))
j = str ('{"SEVersion": {"Number": "2"},"Merchant": {"SiTefCode": "ARGMP000","DocumentMerchant":} {}, "DocumentMerchantType": "CUIT"}'.format(3))
#print('"{"SEVersion": {"Number": "2"},"Merchant": {"SiTefCode": "ARGMP000","DocumentMerchant":, "DocumentMerchantType": "CUIT"}'.format(aspas))
print(j)




      
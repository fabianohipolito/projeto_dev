from lib2to3.pytree import convert
import random
from datetime import date, datetime
from time import time
import time
from xml.sax.handler import DTDHandler
from time import sleep

# Menu geral
print('''
        [1] - Transacción de Venta                     
        [2] - Transacción de Anulación de la Venta     
        ''')
fiserv = int(input("Escolha uma opção:  "))


comprovante = random.randint(10, 99) # Gera os dois ultimos automaticamente do Número de la factura, TAG 004
host = random.randint(1000, 9999) # Gera os quatro digitos do Código de autorización del host, TAG 023 para transações com efetivo
payment = random.randint(10, 99) # Gera automaticamente os dois ultimos digitos do Código Identificador del pago, TAG 025 e do PaymentID do JSON.
dt = date.today() # Pega data local.
#hr = datetime.now() # Pega a hora exata da maquina.
data = dt.strftime("%Y%m%d") # Formata a data em AAAAMMDD
hora = time.strftime('%H%M%S') # FOrmata a hora em HHMMSS


cuit = int(input("Informe o numero do cuit: ")) # Infoma na tela para usuario digitar o numero do cuit e coleta o que foi digitado.
codigo = str(input("Informe o codigo da loja: ")) # Solicita ao usuario para digitar o codigo da loja.
mpm = codigo.upper() # Coloca todo as letras do comercio que foi digitado em letra maiuscula

#TAG
two = '00200011' #Tag 002 do envio de dados
four = '0040001300010000000' #Tag 004 do envio de dados
five = '00500008' #Tag 005 do envio de dados
six = '00600006' #Tag 006 do envio de dados
seven = '00700001' #Tag 007 do envio de dados
nine = '00900001' #Tag 009 do envio de dados
thirteen = '0130000512100' #Tag 013 do envio de dados
fourteen = '01400001' #Tag 014 do envio de dados
fifteen = '01500002VI' #Tag 015 do envio de dados
twenty =  '020000011' #Tag 020 do envio de dados
twentyone = '021000012' #Tag 021 do envio de dados
twentytwo = '022000011' #Tag 022 do envio de dados
twentytree = '02300006555555' #Tag 023 do envio de dados
twentyfive_T = '02500009TFISERV' #Tag 025 do envio de dados
twentyfive_E = '02500009EFISERV' #Tag 025 do envio de dados
#twentyfive_a = '02500008'
twentyfour = '02400004' #Tag 024 do envio de dados
normal = 'N' # Tipo de Operación Fiscal "Normal" da TAG 009
annulment = 'A' # Tipo de Operación Fiscal "Normal" da TAG 009
cash = 'E' # Tipo de pago "Efetivo" da TAG 014
card = 'T' # Tipo de pago "Tarjeta" da TAG 014
credito = 'C' 
debito = 'D'
cardbrand_c = 'VI' # Codigo da bandeira Visa
cardbrand_d = 'MA' # Codigo da bandeira Maestro

#JSON
ct = '"{}"'.format(cuit) # Adiciona aspas duplas no cuit digitado.
cf = '{}"'.format(comprovante) # Adiciona aspas duplas no cuit digitado.
cd = '"{}"'.format(mpm) # Adiciona aspas duplas no cuit digitado.
dt = '"{}"'.format(data) # Adiciona aspas duplas no cuit digitado.
tm = '"{}"'.format(hora) # Adiciona aspas duplas no cuit digitado.
py = '{}"'.format(payment) # Adiciona aspas duplas no cuit digitado.
cbc = '"{}"'.format(cardbrand_c) # Adiciona aspas duplas no cuit digitado.
cbd = '"{}"'.format(cardbrand_d) # Adiciona aspas duplas no cuit digitado.
se = '{\"SEVersion\":{\"Number\":\"2\"},\"Merchant\":{\"SiTefCode\":'
dc = ',\"DocumentMerchant\":'
fv = ',\"DocumentMerchantType\":\"CUIT\"},\"SaleTicketType\"'
sl = ':\"SALE\"'
rt = ':\"RETURN\"'
cnc = ':\"CANCELLED\"'
merchant = ',\"merchantId\":'
ex = ',\"Terminal\":\"AR000001\",\"Invoice\":[{\"InvoiceNumber\":{\"Type\":\"B\",\"FiscalPointSaleNumber\":\"00001\",\"Number\":\"000000'
id  = ',\"InvoiceDeliveryMethod\":\"ELECTRONIC_INVOICE\",\"documentType\"'
ef = ':\"EFACTURA\"}'
nc = ':\"NC_EFACTURA\"}'
dat = ',\"Date\":'
ti = ',\"Time\":'
doc = ',"PriceList":"Publico","Customer":{"Name":"","FiscalSituation":"","DocumentType":"","Number":""},"Products":[{"ProductSKU":"ARTICULOS","ProductDescription":"Articulos Varios","Quantity":"1","Price":"121.00","DiscountPercentage":"0","DiscountAmount":"0","Amount":"121.00"}],"PaymentValues":[{"PaymentCode":"Fiserv","PaymentDescription":"Pesos","CardBrand":" "'
doc_card = ',"PriceList":"Publico","Customer":{"Name":"","FiscalSituation":"","DocumentType":"","Number":""},"Products":[{"ProductSKU":"ARTICULOS","ProductDescription":"Articulos Varios","Quantity":"1","Price":"121.00","DiscountPercentage":"0","DiscountAmount":"0","Amount":"121.00"}],"PaymentValues":[{"PaymentCode":"Fiserv","PaymentDescription":"Pesos","CardBrand":'
doc_T = ',"PriceList":"Publico","Customer":{"Name":"","FiscalSituation":"","DocumentType":"","Number":""},"Products":[{"ProductSKU":"ARTICULOS","ProductDescription":"Articulos Varios","Quantity":"2","Price":"121.00","DiscountPercentage":"0","DiscountAmount":"0","Amount":"121.00"}],"PaymentValues": [{"PaymentCode":"Fiserv","PaymentDescription":"Tarjeta de Credito","CardBrand":"VI"'
cancel = ',"PriceList": "","Products": [{"ProductSKU": "","ProductDescription": "","Quantity": "0","Price": "0","DiscountPercentage": "0","DiscountAmount": "0","Amount": "0"}],"PaymentValues": [{"PaymentCode": "","PaymentDescription": "","CardBrand": "","Date": "0","Time": "0","Type": "","Symbol ": "$","Amount": "0","NSUSitef": "","PaymentID": "0"}],"SubTotal": "0","DiscountPercentage": "0","DiscountAmount": "0","IVA": [{"Percentage": "0","Amount": "0"}],"OtherTaxes": "0","AmountTotal": "0"}]}'
doc_E = '},{"PaymentCode":"Fiserv","PaymentDescription":"Efetivo","CardBrand":""'
pc_E = ',"Type":"Pesos","Symbol":"$","Amount":"121.00","NSUSitef":" ","PaymentID":"EFISERV'
pc_card = ',"Type":"TARJETA CREDITO","Symbol":"$","Amount":"121.00","NSUSitef":" ","PaymentID":"TFISERV'
pc_deb = ',"Type":"TARJETA DEBITO","Symbol":"$","Amount":"121.00","NSUSitef":" ","PaymentID":"TFISERV'
sw = '}],"SubTotal":"100.00","DiscountPercentage":"0","DiscountAmount":"0","IVA":[{"Percentage":"21.00","Amount":"21.00"}],"OtherTaxes":"0","AmountTotal":"121.00"}]}'
sw_2 = '}],"SubTotal":"200.00","DiscountPercentage":"0","DiscountAmount":"0","IVA":[{"Percentage":"21.00","Amount":"42.00"}],"OtherTaxes":"0","AmountTotal":"242.00"}]}'
if fiserv == 1:

        print ('''
            [1] - Transacción de Venta con Efectivo 
            [2] - Transacción de Venta con Credito
            [3] - Transacción de Venta con Debito
            [4] - Transacción de Venta con Efectivo y Tarjeta 
            [5] - Factura cancelada durante una venta (problema de energía por ejemplo)
            [6] - Cambio del medio de pago de la transacción
                      
        ''')
        menu2 = int(input("Escolha uma opção:  "))
#Efetivo
        if menu2  == 1:
                tag = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01033'.format(two, cuit, four, comprovante, five, data, six, hora, nine, normal, thirteen, fourteen, cash, twentyfive_E, payment))
                js = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format( se, cd, dc, ct, fv, sl, merchant, ct, ex, cf, id, ef, dat, dt, ti, tm, doc, dat, dt, ti, tm, pc_E, py, sw))
                print('{}{}'.format(tag, js))

#Transação de Credito
        elif menu2 == 2:
                tg = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01044'.format(two, cuit, four, comprovante, five, data, six, hora, seven, credito, nine, normal, thirteen, fourteen, card, fifteen, twenty, twentyone, twentytwo, twentytree, twentyfour, host, twentyfive_T, payment))
                json_card = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(se, cd, dc, ct, fv, sl,  merchant, ct, ex, cf, id, ef, dat, dt,  ti, tm, doc_card, cbc, dat, dt, ti, tm, pc_card, py, sw))
                print('{}{}'.format(tg, json_card))
        
#Transação de Debito
        elif menu2 == 3:
                tg = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01043'.format(two, cuit, four, comprovante, five, data, six, hora, seven, debito, nine, normal, thirteen, fourteen, card, fifteen, twenty, twentyone, twentytwo, twentytree, twentyfour, host, twentyfive_T, payment))
                json_card = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(se, cd, dc, ct, fv,  sl, merchant, ct, ex, cf, id, ef, dat, dt, ti, tm, doc_card, cbd,  dat, dt, ti, tm, pc_deb, py, sw))
                print('{}{}'.format(tg, json_card))
#Transação de Tarjeta e Efetivo
        elif menu2 == 4:
                tg = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01248'.format(two, cuit, four, comprovante, five, data, six, hora, seven, credito, nine, normal, thirteen, fourteen, card, fifteen, twenty, twentyone, twentytwo, twentytree, twentyfour, host, twentyfive_T, payment, thirteen, fourteen, cash, twentyfive_E, payment))
                json_card = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(se, cd, dc, ct, fv, sl,  merchant, ct, ex, cf, id, ef, dat, dt,  ti, tm, doc_T,  dat, dt, ti, tm,  pc_card, py, doc_E, dat, dt, ti, tm, pc_E, py, sw_2))
                print('{}{}'.format(tg, json_card))
 #Factura cancelada durante una venta.
        elif menu2 == 5:
                
                #Json de cancelamento
                json_card = ('ANF00890{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(se, cd, dc, ct, fv, cnc, merchant, ct, ex, cf, id, ef, dat, dt, ti, tm, cancel ))
                print('{}\n'.format(json_card))
                sleep(2)
                tiempo = time.strftime('%H%M%S')
                tmp = '"{}"'.format(tiempo) # Adiciona aspas duplas no cuit digitado.
                comp = cf

                tag = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01033'.format(two, cuit, four, comprovante, five, data, six, tiempo, nine, normal, thirteen, fourteen, cash, twentyfive_E, payment))
                js = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format( se, cd, dc, ct, fv, sl, merchant, ct, ex, comp, id, ef, dat, dt, ti, tmp, doc, dat, dt, ti, tm, pc_E, py, sw))
                print('{}{}'.format(tag, js))

        elif menu2 == 6:
                comp = cf
                tag = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01033'.format(two, cuit, four, comprovante, five, data, six, hora, nine, normal, thirteen, fourteen, cash, twentyfive_E, payment))
                js = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format( se, cd, dc, ct, fv, sl, merchant, ct, ex, cf, id, ef, dat, dt, ti, tm, doc, dat, dt, ti, tm, pc_E, py, sw))
                print('{}{}\n'.format(tag, js))
                sleep(2)
                tiempo = time.strftime('%H%M%S')
                tmp = '"{}"'.format(tiempo) # Adiciona aspas duplas no cuit digitado.
                json_card = ('ANF00890{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(se, cd, dc, ct, fv, cnc, merchant, ct, ex, comp, id, ef, dat, dt, ti, tmp, cancel ))
                print('{}\n'.format(json_card))
                sleep(2)
                tiempo = time.strftime('%H%M%S')
                tmp = '"{}"'.format(tiempo) # Adiciona aspas duplas no cuit digitado.
                tg = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01044'.format(two, cuit, four, comprovante, five, data, six, tiempo, seven, credito, nine, normal, thirteen, fourteen, card, fifteen, twenty, twentyone, twentytwo, twentytree, twentyfour, host, twentyfive_T, payment))
                json_card = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(se, cd, dc, ct, fv, sl,  merchant, ct, ex, cf, id, ef, dat, dt,  ti, tmp, doc_card, cbc, dat, dt, ti, tmp, pc_card, py, sw))
                print('{}{}'.format(tg, json_card))

#Menu segundario
elif fiserv == 2:
        print('''        
            [1] - Transacción de Anulación de la Venta de Crédito
            [2] - Transacción de Anulación de la Venta de Dédito
            [3] - Transacción de Anulación de la Venta de Efetivo
            [4] - Transacción de Anulación de la Venta de Efectivo y Tarjeta 
            [5] - Factura cancelada durante una anulación (problema de energía por ejemplo)
        ''')
        anul = int(input("Escolha uma opção:  "))
        
        #Anulação de Credito
        if anul == 1:
                an = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01048'.format(two, cuit, four, comprovante, five, data, six, hora, seven, credito, nine, annulment, thirteen, fourteen, card, fifteen, twenty, twentyone, twentytwo, twentytree, twentyfour,  host, twentyfive, payment))
                sp = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(se, cd, dc, ct, fv, rt, merchant, ct, ex, cf, id, nc, dat, dt, ti, tm, doc_card, cbc, dat, dt, ti, tm, pc_card, py, sw))
                print('{}{}'.format(an, sp))
        #Anulação de Debito
        elif anul == 2:
                an = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01038'.format(two, cuit, four, comprovante, five, data, six, hora, seven, debito, nine, annulment, thirteen, fourteen, card, fifteen, twenty, twentyone, twentytwo, twentytree, twentyfour, host, twentyfive,  payment))
                sp = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(se, cd, dc, ct, fv, rt, merchant, ct, ex, cf, id, nc, dat, dt, ti, tm, doc_card, cbc, dat, dt, ti, tm, pc_deb, py, sw))
                print('{}{}'.format(an, sp))
                
        #Anulação com Efetivo        
        elif anul == 3:
                an = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01037'.format(two, cuit, four, comprovante, five, data, six, hora,  cash, nine, annulment, thirteen, fourteen, cash,  payment))
                sp = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(se, cd, dc, ct, fv, rt, merchant, ct, ex, cf, id, nc, dat, dt, ti, tm, doc, dat, dt, ti, tm, pc, py, sw))
                print('{}{}'.format(an, sp))

        #Anulação de Efetivo e tarjeta.
        elif anul == 4:
                an = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01253'.format(two, cuit, four, comprovante, five, data, six, hora, seven, credito, nine, annulment, thirteen, fourteen, card, fifteen, twenty, twentyone, twentytwo, twentytree, twentyfour, host, twentyfive_T, payment, thirteen, fourteen, cash, twentyfive_E, payment))
                sp = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(se, cd, dc, ct, fv, rt,  merchant, ct, ex, cf, id, nc, dat, dt,  ti, tm, doc_T,  dat, dt, ti, tm,  pc_card, py, doc_E, dat, dt, ti, tm, pc_E, py, sw_2))
                print('{}{}'.format(an, sp))
        
        elif anul == 5:
                #Json de cancelamento
                json_card = ('ANF00893{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(se, cd, dc, ct, fv, cnc, merchant, ct, ex, cf, id, nc, dat, dt, ti, tm, cancel ))
                print('{}\n'.format(json_card))
                sleep(5)
                tiempo = time.strftime('%H%M%S')
                tmp = '"{}"'.format(tiempo) # Adiciona aspas duplas no cuit digitado.
                comp = cf

                tag = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}ANF01036'.format(two, cuit, four, comprovante, five, data, six, tiempo, nine, annulment, thirteen, fourteen, cash, twentyfive_E, payment))
                js = ('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format( se, cd, dc, ct, fv, rt, merchant, ct, ex, comp, id, nc, dat, dt, ti, tmp, doc, dat, dt, ti, tm, pc_E, py, sw))
                print('{}{}'.format(tag, js))
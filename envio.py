import random
from datetime import date, datetime
from time import time
import json

comprovante = random.randint(10, 99)
dt = date.today()
hr = datetime.now()
data = dt.strftime("%Y%m%d")
hora = hr.strftime('%H%M%S')
host = random.randint(1000, 9999)
payment = random.randint(10, 99)

cuit = int(input("Informe o numero do cuit: "))
#cotas = int(input("Informe o numero de cotas: "))
codigo = str(input("Informe o codigo da loja: "))
mpm = codigo.upper()

ct = '"{}"'.format(cuit)
cf = '{}"'.format(comprovante)
cd = '"{}"'.format(mpm)
dt = '"{}"'.format(data)
tm = '"{}"'.format(hora)
py = '{}"'.format(payment)
se = '{\"SEVersion\":{\"Number\":\"2\"},\"Merchant\":{\"SiTefCode\":'
dc = ',\"DocumentMerchant\":'
fv = ',\"DocumentMerchantType\":\"CUIT\"},\"SaleTicketType\":\"SALE\",\"merchantId\":'
ex = ',\"Terminal\":\"AR000001\",\"Invoice\":[{\"InvoiceNumber\":{\"Type\":\"B\",\"FiscalPointSaleNumber\":\"00001\",\"Number\":\"0000000'
id  = ',\"InvoiceDeliveryMethod\":\"ELECTRONIC_INVOICE\",\"documentType\":\"EFACTURA\"}'
dat = ',\"Date\":'
ti = ',\"Time\":'
doc = ',"PriceList":"Publico","Customer":{"Name":"","FiscalSituation":"","DocumentType":"","Number":""},"Products":[{"ProductSKU":"ARTICULOS","ProductDescription":"Articulos Varios","Quantity":"1","Price":"121.00","DiscountPercentage":"0","DiscountAmount":"0","Amount":"121.00"}],"PaymentValues":[{"PaymentCode":"P","PaymentDescription":"Pesos","CardBrand":" "'
pc = ',"Type":"Pesos","Symbol":"$","Amount":"121.00","NSUSitef":" ","PaymentID":"FISERV'
sw = '}],"SubTotal":"100.00","DiscountPercentage":"0","DiscountAmount":"0","IVA":[{"Percentage":"21.00","Amount":"21.00"}],"OtherTaxes":"0","AmountTotal":"121.00"}]}'

print('00200011{}00400014000010000000{}00500008{}00600006{}00900001N013000051210001400001E02500008FISERV{}ANF01028{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(cuit, comprovante, data, hora,  payment, se, cd, dc, ct, fv, ct, ex, cf, id, dat, dt, ti, tm, doc, dat, dt, ti, tm, pc, py, sw))

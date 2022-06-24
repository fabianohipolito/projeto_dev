from datetime import date, datetime
from time import time
import time

dt = date.today()
data = dt.strftime("%d%m%Y") 
hora = time.strftime('%H%M%S')

#payment = date
py = '{}{}"'.format(data, hora)
t = '02500009EFISERV'
print ('{}{}'.format(t, py))
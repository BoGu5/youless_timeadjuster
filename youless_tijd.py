import requests
import time
from bs4 import BeautifulSoup
from time import sleep

#set youless IP
yl_ip = '192.168.1.143'



url = 'http://'+yl_ip+'/S'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "lxml")
table = soup.find('table')

list_of_cells = []                          

for row in table.findAll('tr'): 
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)

print (list_of_cells)
yl_tijdstring = list_of_cells[0]
print ('huidige tijd op youless: ',yl_tijdstring)

nu = time.localtime()
nu_dag = nu.tm_mday
nu_maand = nu.tm_mon
nu_jaar = nu.tm_year - 2000
nu_uur = nu.tm_hour
nu_minuut = nu.tm_min

#datumy l_dag, yl_maand, yl_jaar
yl_datum = yl_tijdstring[0:8]
print(yl_datum)
yl_dag, yl_maand, yl_jaar = yl_datum.split('-')

#tijd yl_uur, yl_minuut 
yl_tijd = yl_tijdstring[9:14]
print(yl_tijd)
yl_uur, yl_minuut = yl_tijd.split(':')

#typecast naar int
yl_dag = int(yl_dag)
yl_maand = int(yl_maand)
yl_jaar = int(yl_jaar)
yl_uur = int(yl_uur)
yl_minuut = int(yl_minuut)


print('dag',yl_dag,'maand',yl_maand,'jaar',yl_jaar,'uur',yl_uur,'minuut',yl_minuut)


verschil_dag = yl_dag - nu_dag
verschil_maand = yl_maand - nu_maand
verschil_jaar = yl_jaar - nu_jaar
verschil_uur = yl_uur - nu_uur
verschil_minuut = yl_minuut - nu_minuut

print('dag:',verschil_dag,'maand:',verschil_maand,'jaar:',verschil_jaar,'uur:',verschil_uur,'minuut:',verschil_minuut)

corrigeer_up_dag_url = 'http://'+yl_ip+'/S?t=du'
corrigeer_up_maand_url = 'http://'+yl_ip+'/S?t=Mu'
corrigeer_up_jaar_url = ''
corrigeer_up_uur_url = 'http://'+yl_ip+'/S?t=hu'
corrigeer_up_minuut_url = 'http://'+yl_ip+'/S?t=mu'

corrigeer_down_dag_url = 'http://'+yl_ip+'/S?t=dd'
corrigeer_down_maand_url = 'http://'+yl_ip+'/S?t=Md'
corrigeer_down_jaar_url = ''
corrigeer_down_uur_url = 'http://'+yl_ip+'/S?t=hd'
corrigeer_down_minuut_url = 'http://'+yl_ip+'/S?t=md'

#dag
if verschil_dag == 0:
    print('dagen klaar')
else:
    if verschil_dag < 0:
        aantal = verschil_dag*-1
        while aantal > 0:
            print('dag omhoog')
            requests.get(corrigeer_up_dag_url)
            sleep(1)
            aantal -= 1
    if verschil_dag > 0:
        aantal = verschil_dag
        while aantal > 0:
            print('dag omlaag')
            requests.get(corrigeer_down_dag_url)
            sleep(1)
            aantal -= 1

#maand
if verschil_maand == 0:
    print('maanden klaar')
else:
    if verschil_maand < 0:
        aantal = verschil_maand*-1
        while aantal > 0:
            print('maand omhoog')
            requests.get(corrigeer_up_maand_url)
            sleep(1)
            aantal -= 1
    if verschil_minuut > 0:
        aantal = verschil_maand
        while aantal > 0:
            print('maand omlaag')
            requests.get(corrigeer_down_maand_url)
            sleep(1)
            aantal -= 1

#jaar
if verschil_jaar == 0:
    print('jaren klaar')
else:
    if verschil_jaar < 0:
        aantal = (verschil_jaar*-1)*12
        while aantal > 0:
            print(aantal,'maanden omhoog')
            requests.get(corrigeer_up_maand_url)
            sleep(1)
            aantal -= 1
    if verschil_minuut > 0:
        aantal = verschil_jaar*12
        while aantal > 0:
            print(aantal,'maanden omlaag')
            requests.get(corrigeer_down_maand_url)
            sleep(1)
            aantal -= 1

#uur
if verschil_uur == 0:
    print('uren klaar')
else:
    if verschil_uur < 0:
        aantal = verschil_uur*-1
        while aantal > 0:
            print('uur omhoog')
            requests.get(corrigeer_up_uur_url)
            sleep(1)
            aantal -= 1
    if verschil_uur > 0:
        aantal = verschil_uur
        while aantal > 0:
            print('uur omlaag')
            requests.get(corrigeer_down_uur_url)
            sleep(1)
            aantal -= 1
            
#minuut
if verschil_minuut == 0:
    print('minuten klaar')
else:
    if verschil_minuut < 0:
        aantal = verschil_minuut*-1
        while aantal > 0:
            print('minuut omhoog')
            requests.get(corrigeer_up_minuut_url)
            sleep(1)
            aantal -= 1
    if verschil_minuut > 0:
        aantal = verschil_minuut
        while aantal > 0:
            print('minuut omlaag')
            requests.get(corrigeer_down_minuut_url)
            sleep(1)
            aantal -= 1

        



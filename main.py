import requests
from bs4 import BeautifulSoup

print('Iekopējiet sludinājuma saiti:')
adrese = input()

sludinājums = requests.get(adrese)

if sludinājums.status_code == 200:
    saturs = BeautifulSoup(sludinājums.content, "html.parser")

    #Pārbauda vai sludinājuma termiņš nav beidzies (vai satur bildi - https://i.ss.lv/img/a_lv.gif)
    info = saturs.find_all(src="https://i.ss.lv/img/a_lv.gif")
    if len(info)!=0:
        print("Sludinājuma termiņš ir beidzies")
        exit()
    
    #Atrod dzīvokļa cenu
    cena = saturs.find(class_="ads_price")
    print(cena.string)
        
    
else:
    print("Saite nedarbojas")